from pathlib import Path
ROOT=Path(__file__).parents[1]
required=['agent.yaml','SOUL.md','README.md','EXPLAINABILITY.md','RULES.md','DUTIES.md','AGENTS.md']
for f in required:
 assert (ROOT/f).exists(), f
for d in ['skills/resume-screening','skills/candidate-matching','skills/screening-reporting','tools','tests']:
 assert (ROOT/d).is_dir(), d
print(f'READINESS AUDIT: PASS\nChecked {len(required)} required files and 5 directories.')
