# Spec: Scope triage and graceful decline
Feature served: [MOM-01] via [FLW-CONSULTA] · Context: [CTX-Consultoria]

WHEN the user submits a query
THE SYSTEM SHALL validate the text per VAL-INPUT-01 before accepting the submission. [VAL-INPUT-01] [EDG-06]

IF the query falls outside tax scope or requests a procedural filing
THEN THE SYSTEM SHALL decline it at intake with an explicit reason and a link to rephrase, without logging the query in the queue. [POL-ESC-01] [EDG-06] [NG-01] [TEN-02]
