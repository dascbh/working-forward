# Spec: Daily regulatory radar
Feature served: [MOM-10] [MOM-11] via [FLW-RADAR] · Context: [CTX-Monitoramento]

WHEN daily ingestion completes (EVT-NormaIngerida)
THE SYSTEM SHALL display on the radar the new/amended regulations with estimated impact per client (EVT-ImpactoClassificado). [BCK-21] [BCK-22] [MOM-10]

WHILE a regulation has no impact classification for more than 24 hours
THE SYSTEM SHALL display it with a 'pending analysis' flag, never hiding it from the radar. [POL-RAD-01]

IF an official source is unavailable during the ingestion window
THEN THE SYSTEM SHALL retry with backoff and display a partial-coverage banner on the day's radar. [EDG-21]

WHEN the associate forwards a regulation
THE SYSTEM SHALL require an active owner on the account (VAL-RESP-01) and notify via CMD-NotificarResponsavel. [VAL-RESP-01] [RCT-03] [MOM-11]
