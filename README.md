# Resume Screening Agent

A framework-independent agent for deterministic resume screening, candidate-job matching, and explainable screening reports.

## Scope

The agent compares caller-supplied resume information with caller-supplied job requirements. It does not retrieve candidates, contact employers, or access external recruiting systems.

## Validation

```bash
pytest -q
python3 verification/readiness_audit.py
opengap validate
```
