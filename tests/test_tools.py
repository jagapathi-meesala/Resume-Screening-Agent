import importlib.util
from pathlib import Path
ROOT=Path(__file__).parents[1]
def load(name):
 p=ROOT/'tools'/f'{name}.py'; s=importlib.util.spec_from_file_location(name.replace('-','_'),p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def test_screen():
 m=load('screen-resume'); assert m.screen_resume({'candidate_skills':['Python','SQL'],'required_skills':['python','java']})['match_percent']==50.0
def test_match():
 m=load('match-candidate'); assert m.match_candidate({'candidate_years':2,'required_years':2,'candidate_skills':['python'],'required_skills':['python']})['overall_match_percent']==100.0
def test_report():
 m=load('build-screening-report'); assert m.build_report({'candidate_name':'A','match_percent':80,'matched_skills':['python'],'missing_skills':['java']})['candidate']=='A'
def test_invalid():
 m=load('screen-resume')
 try: m.screen_resume({'candidate_skills':[]})
 except ValueError: return
 assert False
def test_extra():
 m=load('screen-resume')
 try: m.screen_resume({'candidate_skills':[],'required_skills':[],'x':1})
 except ValueError: return
 assert False
