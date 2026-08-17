#!/usr/bin/env python3
"""
wf_lint.py — Working Forward cross-layer coherence linter.

Valida um produto WF (estrutura L0-L5) contra:
  1. Schemas JSON Schema (validação estrutural, se jsonschema instalado)
  2. Lints de coerência entre camadas (o "sistema imunológico" do framework)

Uso:
    python tools/wf_lint.py examples/products/aurora-tax
    python tools/wf_lint.py <produto> --level commit   # só falha em checks nível commit

Saída: relatório por check; exit code 1 se houver falha no nível selecionado.
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("wf_lint precisa de pyyaml: pip install pyyaml")

try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False

# ---------------------------------------------------------------- infra

LAYER_FILES = {
    "vision": "L0-vision/vision.yaml",
    "journey": "L1-journey/journey.yaml",
    "blueprint": "L2-service/blueprint.yaml",
    "domain": "L3-domain/domain.yaml",
    "experience": "L4-experience/experience.yaml",
}

# checks nível "commit" (bloqueiam merge) vs "advisory" (avisam)
COMMIT_LEVEL = {"refs-resolve", "edge-coverage", "validation-pedigree", "spec-anchoring"}

ID_PATTERN = re.compile(r"\b((?:CUST|PROB|TEN|FAQ|NG|ACT|JRN|MOM|BCK|POL|EDG|EVT|CMD|RCT|AGG|CTX|FLW|VAL|SCR)-[A-Za-z0-9][A-Za-z0-9-]*)\b")


class Report:
    def __init__(self):
        self.results = []  # (check, level, ok, messages)

    def add(self, check, ok, messages, level):
        self.results.append((check, level, ok, messages))

    def render(self, fail_level):
        failed = False
        for check, level, ok, messages in self.results:
            mark = "✔" if ok else ("✖" if level == "commit" else "⚠")
            print(f"{mark} [{level:8s}] {check}")
            for m in messages:
                print(f"      - {m}")
            if not ok and (fail_level == "all" or level == "commit"):
                failed = True
        return failed


def load_yaml(path: Path):
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def walk_ids(node, found: set):
    """Coleta todo valor de campo 'id' recursivamente."""
    if isinstance(node, dict):
        if "id" in node and isinstance(node["id"], str):
            found.add(node["id"])
        for v in node.values():
            walk_ids(v, found)
    elif isinstance(node, list):
        for v in node:
            walk_ids(v, found)


def walk_refs(node, refs: list, path=""):
    """Coleta toda string que parece um ID WF em campos que NÃO são 'id'."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "id":
                continue
            walk_refs(v, refs, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk_refs(v, refs, f"{path}[{i}]")
    elif isinstance(node, str):
        for m in ID_PATTERN.findall(node):
            refs.append((m, path))


# ---------------------------------------------------------------- checks

def check_schemas(product: Path, layers: dict, report: Report):
    if not HAS_JSONSCHEMA:
        report.add("schemas", True, ["jsonschema não instalado — validação estrutural pulada"], "advisory")
        return
    import json
    schema_dir = Path(__file__).resolve().parent.parent / "schemas"
    msgs, ok = [], True
    for name, data in layers.items():
        if data is None:
            continue
        schema_path = schema_dir / f"{name}.schema.json"
        if not schema_path.exists():
            continue
        schema = json.load(open(schema_path, encoding="utf-8"))
        validator = jsonschema.Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
        for e in errors[:10]:
            ok = False
            loc = "/".join(str(p) for p in e.path) or "<raiz>"
            msgs.append(f"{name}.yaml @ {loc}: {e.message}")
    report.add("schemas", ok, msgs or ["todos os artefatos passam nos schemas"], "commit" if not ok else "advisory")


def check_refs_resolve(layers: dict, spec_texts: dict, report: Report):
    all_ids = set()
    for data in layers.values():
        if data:
            walk_ids(data, all_ids)
    # estados de fluxo também são alvos referenciáveis (targets de transição)
    msgs, ok = [], True
    for name, data in layers.items():
        if not data:
            continue
        refs = []
        walk_refs(data, refs)
        for ref, path in refs:
            if ref not in all_ids:
                ok = False
                msgs.append(f"{name}.yaml: '{ref}' referenciado em {path} não existe em nenhuma camada")
    for spec_name, text in spec_texts.items():
        for ref in set(ID_PATTERN.findall(text)):
            if ref not in all_ids:
                ok = False
                msgs.append(f"{spec_name}: '{ref}' não existe em nenhuma camada")
    report.add("refs-resolve", ok, msgs or [f"{len(all_ids)} IDs declarados, todas as referências resolvem"], "commit")


def check_hard_questions(layers: dict, spec_texts: dict, report: Report):
    vision = layers.get("vision")
    if not vision:
        report.add("hard-questions", True, ["sem vision.yaml — pulado"], "advisory")
        return
    layer_blobs = {
        "L1": yaml.dump(layers.get("journey") or {}),
        "L2": yaml.dump(layers.get("blueprint") or {}),
        "L3": yaml.dump(layers.get("domain") or {}),
        "L4": yaml.dump(layers.get("experience") or {}),
        "L5": "\n".join(spec_texts.values()),
    }
    msgs, ok = [], True
    for hq in vision.get("hard_questions", []):
        owner = hq.get("owner_layer")
        hid = hq.get("id")
        blob = layer_blobs.get(owner, "")
        if owner == "L0":
            continue  # respondida na própria visão
        if hid not in blob:
            ok = False
            msgs.append(f"{hid} ('{hq.get('q','')[:60]}...') endereçada a {owner} mas nenhum elemento de {owner} a referencia")
    report.add("hard-questions", ok, msgs or ["toda hard question foi consumida pela camada dona"], "advisory")


def check_edge_coverage(layers: dict, report: Report):
    blueprint, experience = layers.get("blueprint"), layers.get("experience")
    if not blueprint or not experience:
        report.add("edge-coverage", True, ["camadas L2/L4 ausentes — pulado"], "advisory")
        return
    exp_blob = yaml.dump(experience)
    msgs, ok = [], True
    for bp in blueprint.get("blueprints", []):
        for edge in bp.get("edge_cases", []):
            eid = edge.get("id")
            if edge.get("accepted_risk"):
                continue
            if eid not in exp_blob:
                ok = False
                msgs.append(f"{eid} ('{edge.get('case','')[:60]}') sem estado/transição em L4 e sem accepted_risk")
    report.add("edge-coverage", ok, msgs or ["todo edge case coberto no L4 ou aceito com dono"], "commit")


def check_event_closure(layers: dict, report: Report):
    domain, experience = layers.get("domain"), layers.get("experience")
    if not domain:
        report.add("event-closure", True, ["sem domain.yaml — pulado"], "advisory")
        return
    produced = set()
    for cmd in domain.get("commands", []):
        produced.update(cmd.get("produces", []))
    emitted = {e["id"] for e in domain.get("events", []) if e.get("emitted_by")}
    consumed = {r.get("when") for r in domain.get("reactions", [])}
    exp_blob = yaml.dump(experience or {})
    msgs, ok = [], True
    for ev in domain.get("events", []):
        eid = ev["id"]
        if eid not in produced and eid not in emitted:
            ok = False
            msgs.append(f"{eid}: nenhum comando produz e nenhum backstage emite (evento órfão de origem)")
        if eid not in consumed and eid not in exp_blob:
            ok = False
            msgs.append(f"{eid}: nenhuma reaction consome e nenhum fluxo escuta (evento órfão de destino)")
    report.add("event-closure", ok, msgs or ["todo evento tem emissor e consumidor"], "advisory")


def check_validation_pedigree(layers: dict, report: Report):
    experience = layers.get("experience")
    if not experience:
        report.add("validation-pedigree", True, ["sem experience.yaml — pulado"], "advisory")
        return
    known = set()
    for lname in ("blueprint", "vision"):
        if layers.get(lname):
            walk_ids(layers[lname], known)
    msgs, ok = [], True
    for val in experience.get("validations", []):
        src = val.get("derived_from", "")
        if not src or not any(k in src for k in known):
            ok = False
            msgs.append(f"{val.get('id')}: derived_from='{src}' não aponta pra policy/edge case conhecido")
    report.add("validation-pedigree", ok, msgs or ["toda validação tem pedigree"], "commit")


def check_spec_anchoring(spec_texts: dict, layers: dict, report: Report):
    if not spec_texts:
        report.add("spec-anchoring", True, ["sem specs — pulado"], "advisory")
        return
    all_ids = set()
    for data in layers.values():
        if data:
            walk_ids(data, all_ids)
    msgs, ok = [], True
    clause_re = re.compile(r"^\s*(WHEN|IF|WHILE|WHERE|THE SYSTEM SHALL)", re.MULTILINE)
    for name, text in spec_texts.items():
        # blocos de cláusula: parágrafos que contêm keywords EARS
        paragraphs = [p for p in text.split("\n\n") if clause_re.search(p)]
        for p in paragraphs:
            refs = [r for r in ID_PATTERN.findall(p) if r in all_ids]
            if not refs:
                ok = False
                first = p.strip().splitlines()[0][:70]
                msgs.append(f"{name}: cláusula sem referência a camada anterior → '{first}...'")
    report.add("spec-anchoring", ok, msgs or ["toda cláusula EARS ancorada em ≥1 ID"], "commit")


def check_non_goals(layers: dict, spec_texts: dict, report: Report):
    vision = layers.get("vision")
    if not vision or not vision.get("non_goals"):
        report.add("non-goals", True, ["sem non_goals declarados — pulado"], "advisory")
        return
    # heurística: um NG só pode aparecer em contexto de recusa/bloqueio.
    # aqui checamos apenas que os NG-* referenciados existem (refs-resolve cobre)
    # e reportamos onde cada non-goal é citado, pra revisão humana.
    msgs = []
    blob_sources = {**{k: yaml.dump(v) for k, v in layers.items() if v}, **spec_texts}
    for ng in vision.get("non_goals", []):
        ngid = ng["id"]
        cited = [name for name, blob in blob_sources.items() if ngid in blob and name != "vision"]
        if cited:
            msgs.append(f"{ngid} citado em: {', '.join(cited)} — confirme que é contexto de recusa, não de feature")
    report.add("non-goals", True, msgs or ["nenhum non-goal citado fora do L0"], "advisory")


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description="Working Forward cross-layer linter")
    ap.add_argument("product", help="diretório do produto (contendo L0-vision/, L1-journey/, ...)")
    ap.add_argument("--level", choices=["all", "commit"], default="all",
                    help="'commit' só falha em checks nível commit; 'all' falha em qualquer check")
    args = ap.parse_args()

    product = Path(args.product)
    if not product.is_dir():
        sys.exit(f"diretório não encontrado: {product}")

    layers = {name: load_yaml(product / rel) for name, rel in LAYER_FILES.items()}
    spec_dir = product / "L5-specs"
    spec_texts = {}
    if spec_dir.is_dir():
        for f in sorted(spec_dir.glob("*.md")):
            spec_texts[f.name] = f.read_text(encoding="utf-8")

    present = [n for n, d in layers.items() if d is not None]
    print(f"Working Forward lint — {product.name}")
    print(f"camadas presentes: {', '.join(present)}; specs: {len(spec_texts)}\n")

    report = Report()
    check_schemas(product, layers, report)
    check_refs_resolve(layers, spec_texts, report)
    check_hard_questions(layers, spec_texts, report)
    check_edge_coverage(layers, report)
    check_event_closure(layers, report)
    check_validation_pedigree(layers, report)
    check_spec_anchoring(spec_texts, layers, report)
    check_non_goals(layers, spec_texts, report)

    print()
    failed = report.render(args.level)
    print("\nresultado:", "FALHOU" if failed else "OK")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
