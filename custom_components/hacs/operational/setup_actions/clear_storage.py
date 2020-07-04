import os
from custom_components.hacs.hacs import get_hacs
from custom_components.hacs.helpers.functions.logger import getLogger


async def async_clear_storage():
    """Async wrapper for clear_storage"""
    hacs = get_hacs()
    await hacs.hass.async_add_executor_job(_clear_storage)


def _clear_storage():
    """Clear old files from storage."""
    hacs = get_hacs()
    logger = getLogger("startup.clear_storage")
    storagefiles = ["hacs"]
    for s_f in storagefiles:
        path = f"{hacs.system.config_path}/.storage/{s_f}"
        if os.path.isfile(path):
            logger.info(f"Cleaning up old storage file {path}")
            os.remove(path)