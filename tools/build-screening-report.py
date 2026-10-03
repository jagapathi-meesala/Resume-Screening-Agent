import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from contracts.tool_contract import ToolContract
CONTRACT = ToolContract(["candidate_name", "match_percent", "matched_skills", "missing_skills"], {"candidate_name": str, "match_percent": (int,float), "matched_skills": list, "missing_skills": list})
def build_report(data):
    CONTRACT.validate(data)
    return {"candidate":data["candidate_name"],"match_percent":float(data["match_percent"]),"matched_skills":data["matched_skills"],"missing_skills":data["missing_skills"],"basis":"caller-supplied resume and job data only"}
