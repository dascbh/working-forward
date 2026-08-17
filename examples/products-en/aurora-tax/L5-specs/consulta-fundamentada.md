# Spec: Substantiated answer to a query
Feature served: [MOM-03] via [FLW-CONSULTA] · Context: [CTX-Consultoria]

WHEN the system emits EVT-ConsultaRespondida
THE SYSTEM SHALL display every regulatory claim with a clickable citation verified against the primary source, with a per-citation verification badge. [POL-CIT-01] [MOM-03]

WHEN citation validation fails (EVT-CitacaoInvalidada)
THE SYSTEM SHALL transition FLW-CONSULTA to the 'reformulating' state without showing the unverified answer, informing the user that reverification is underway. [RCT-01] [POL-CIT-01]

WHEN two or more applicable regulations conflict
THE SYSTEM SHALL display all conflicting regulations and the resolution criterion applied (hierarchy, chronology, or specificity). [POL-CONF-01] [FAQ-07]

WHEN the substantiating regulation was published less than 24 hours ago
THE SYSTEM SHALL display the answer with an explicit currency caveat and schedule priority reindexing. [EDG-05] [FAQ-11]

IF processing exceeds 8 seconds (EVT-RespostaDegradada)
THEN THE SYSTEM SHALL display a partial answer with a notice and notify the user when the complete answer is available. [EDG-07] [BCK-11]

IF no provision is found to substantiate the answer
THEN THE SYSTEM SHALL declare the inability to substantiate and escalate for human review with the deadline shown. [EDG-08] [RCT-02]
