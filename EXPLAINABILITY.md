# Explainability

## Inputs and Data Sources

The agent accepts resume and job information supplied directly by the caller. It does not retrieve candidate records or external employment data.

### Input Requirements

Each tool validates required fields, types, and unexpected fields.

### Failure Handling

Malformed input is rejected rather than replaced with assumptions.

## Decision and Reasoning

Screening uses deterministic set comparisons for explicit skills and numeric comparison for supplied experience requirements.

### Rules Applied

- Only explicitly supplied skills are compared.
- Missing skills are not inferred.
- Experience is compared only from supplied numeric values.
- Scores are reproducible.
- Protected characteristics are not used as screening criteria.

### Expected Outputs

Outputs include matched skills, missing skills, explicit percentage calculations, and an explanation of the evidence basis.

## Limits and Constraints

The agent cannot verify resume claims, employment history, education, certifications, references, or external records. A match score is an analytical indicator, not a hiring decision.

### Constraints

Results depend entirely on supplied information and the selected requirements.

### Known Issues

Skill matching is lexical after normalization and does not establish semantic equivalence between different skill names.

### Unsupported Behavior

The agent does not infer protected characteristics, fabricate qualifications, contact candidates, or make autonomous employment decisions.

## Tool Documentation

### screen-resume

#### Inputs

`candidate_skills` and `required_skills`.

#### Decision

Computes exact normalized skill overlap and percentage of required skills matched.

#### Outputs

Matched skills, missing skills, and match percentage.

#### Failure Handling

Rejects malformed input and unexpected fields.

#### Limits

Does not verify skill proficiency or semantic equivalence.

### match-candidate

#### Inputs

Candidate years, required years, candidate skills, and required skills.

#### Decision

Combines deterministic skill and experience percentages.

#### Outputs

Skill, experience, and overall match percentages.

#### Failure Handling

Rejects invalid types and unexpected fields.

#### Limits

Does not validate employment history or candidate claims.

### build-screening-report

#### Inputs

Candidate name, match percentage, matched skills, and missing skills.

#### Decision

Formats supplied screening evidence into a structured report.

#### Outputs

A reproducible screening report.

#### Failure Handling

Rejects invalid types and unexpected fields.

#### Limits

The report is documentation of supplied analysis, not an employment recommendation.
