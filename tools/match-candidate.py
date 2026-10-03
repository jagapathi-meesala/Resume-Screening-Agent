import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from contracts.tool_contract import ToolContract
CONTRACT = ToolContract(["candidate_years", "required_years", "candidate_skills", "required_skills"], {"candidate_years": (int,float), "required_years": (int,float), "candidate_skills": list, "required_skills": list})
def match_candidate(data):
    CONTRACT.validate(data)
    c={str(x).strip().lower() for x in data["candidate_skills"]}; r={str(x).strip().lower() for x in data["required_skills"]}
    skill_score=(len(c&r)/len(r)*100) if r else 0.0
    experience_score=100.0 if data["candidate_years"] >= data["required_years"] else (data["candidate_years"]/data["required_years"]*100 if data["required_years"] else 100.0)
    overall=round((skill_score+experience_score)/2,2)
    return {"skill_match_percent":round(skill_score,2),"experience_match_percent":round(experience_score,2),"overall_match_percent":overall}
