"""Blueprint for HacsMigration."""
import logging
from shutil import copy2

from custom_components.hacs.hacsbase import HacsBase

_LOGGER = logging.getLogger('custom_components.hacs.migration')


class HacsMigration(HacsBase):
    """HACS data migration handler."""

    old = None

    async def validate(self):
        """Check the current storage version to determine if migration is needed."""
        self.data["hacs"]["schema"] = self.const.STORAGE_VERSION
        self.old = await self.storage.get()

        if not self.old:
            # Could not read the current file, it probably does not exist.
            # Running full scan.
            await self.update_repositories()

        elif not self.old["hacs"].get("schema"):
            # Creating backup.
            source = "{}/.storage/hacs".format(self.config_dir)
            destination = "{}.none".format(source)
            _LOGGER.info("Backing up current file to '%s'", destination)
            copy2(source, destination)

            # Run migration.
            await self.from_none_to_1()

        elif self.old["hacs"].get("schema") == self.const.STORAGE_VERSION:
            pass

        else:
            # Should not get here, but do a full scan just in case...
            await self.update_repositories()

    async def from_none_to_1(self):
        """Migrate from None (< 0.4.0) to storage version 1."""
        _LOGGER.info("Starting migration of HACS data from None to 1.")

        for item in self.old["elements"]:
            repodata = self.old["elements"][item]
            if repodata.get("isinstalled"):
                # Register new repository
                _LOGGER.info("Migrating %s", repodata["repo"])
                repository, setup_result = await self.register_new_repository(repodata["element_type"], repodata["repo"])

                if setup_result:
                    # Set old values
                    repository.version_installed = repodata["installed_version"]
