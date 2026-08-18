from pathlib import Path
import yaml

ROOT_DIR = Path(__file__).resolve().parent.parent

CONFIG_DIR = ROOT_DIR / "config"


def load_yaml(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_app_config():
    return load_yaml(CONFIG_DIR / "app.yaml")


def get_active_model():

    app = get_app_config()

    active_model = app["active_model"]

    return load_yaml(
        CONFIG_DIR / "models" / f"{active_model}.yaml"
    )