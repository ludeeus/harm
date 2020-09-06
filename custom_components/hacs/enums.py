"""Helper constants."""
# pylint: disable=missing-class-docstring
from enum import Enum


class HacsCategory(str, Enum):
    APPDAEMON = "appdaemon"
    INTEGRATION = "integration"
    LOVELACE = "lovelace"
    NETDAEMON = "netdaemon"
    PYTHON_SCRIPT = "python_script"
    THEME = "theme"


class LovelaceMode(str, Enum):
    """Lovelace Modes."""

    STORAGE = "storage"
    AUTO = "auto"
    YAML = "yaml"


class HacsStage(str, Enum):
    SETUP = "setup"
    STARTUP = "startup"
    RUNNING = "running"
    BACKGROUND = "background"


class HacsSetupTask(str, Enum):
    WEBSOCKET = "WebSocket API"
    FRONTEND = "Frontend"
    SENSOR = "Sensor"
    HACS_REPO = "Hacs Repository"
    CATEGORIES = "Additional categories"
    CLEAR_STORAGE = "Clear storage"
