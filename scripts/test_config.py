from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent

config = ROOT / "config"

with open(config / "app.yaml") as f:
    app = yaml.safe_load(f)

active = app["active_model"]

with open(config / "models" / f"{active}.yaml") as f:
    model = yaml.safe_load(f)

print(model)