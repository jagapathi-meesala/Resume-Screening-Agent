import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from contracts.tool_contract import ToolContract

CONTRACT = ToolContract(["candidate_skills", "required_skills"], {"candidate_skills": list, "required_skills": list})
def screen_resume(data):
    CONTRACT.validate(data)
    candidate = {str(x).strip().lower() for x in data["candidate_skills"]}
    required = {str(x).strip().lower() for x in data["required_skills"]}
    matched = sorted(candidate & required)
    missing = sorted(required - candidate)
    score = round((len(matched) / len(required)) * 100, 2) if required else 0.0
    return {"matched_skills": matched, "missing_skills": missing, "match_percent": score}
