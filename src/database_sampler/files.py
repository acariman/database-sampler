import logging
from pathlib import Path

import yaml


def get_settings(path: str = "etc/settings.yml"):
    path = Path(path)

    if not path.exists():
        msg = f"Settings file does not exist: {path}"
        logging.error(msg)
        raise msg

    with open(path) as f:
        settings = yaml.safe_load(f)

    return settings
