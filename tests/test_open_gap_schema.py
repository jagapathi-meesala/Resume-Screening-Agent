from pathlib import Path
import yaml
ROOT=Path(__file__).parents[1]
def test_manifest():
 d=yaml.safe_load((ROOT/'agent.yaml').read_text()); assert d['spec_version']=='0.1.0'; assert len(d['tools'])==3
