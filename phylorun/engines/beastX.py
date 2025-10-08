import os
from pathlib import Path
import subprocess
from typing import Optional
from phylorun.engines.engine import Engine
from xml.etree import ElementTree

from loguru import logger


class BEASTX(Engine):
    def name(self) -> str:
        """Returns the name of the engine as used in the CLI."""
        return "beastx"

    def can_run_analysis(self, analysis_file: Path) -> bool:
        """Checks if BEAST X can run the analysis in the given file."""
        try:
            xml = ElementTree.parse(analysis_file)
        except ElementTree.ParseError:
            logger.debug("No BEAST X file: no XML file.")
            return False

        root = xml.getroot()

        if root is None or root.tag.lower() != "beast":
            logger.debug("No BEAST X file: no root BEAST tag.")
            return False

        if not root.attrib.get("version", "").startswith("1.") and not root.attrib.get(
            "version", ""
        ).startswith("10."):
            logger.debug("No BEAST X file: wrong version (likely for BEAST 2).")
            return False

        if not any(child.tag.lower() == "mcmc" for child in root):
            logger.debug("No BEASTX file: no <mcmc> tag.")
            return False

        logger.debug("BEAST X file found.")

        return True

    def run_local_analysis(
        self,
        analysis_file: Path,
        engine_path: Optional[str] = None,
        additional_cli_args: Optional[list[str]] = None,
    ):
        """Runs the analysis in the given file using the locally installed engine."""
        engine_path = engine_path or self._find_binary_path()
        if not engine_path:
            raise Exception("No BEAST X binary found.")

        additional_cli_args = additional_cli_args or []

        subprocess.run([engine_path, *additional_cli_args, analysis_file])

    def _find_binary_path(self) -> Optional[str]:
        if path := os.environ.get("BEAST"):
            return path

        possible_paths = (
            list(Path("/Applications").glob("BEAST X*/bin/beast"))
            + list(Path("/Applications").glob("BEAST X*/bin/beast"))
            + list(Path("~").glob("beast*/bin/beast"))
        )
        possible_paths = sorted(possible_paths)

        if not possible_paths:
            return None

        return str(possible_paths[-1])

    def run_containerized_analysis(
        self, analysis_file: Path, additional_cli_args: Optional[list[str]] = None
    ):
        """Runs the analysis in the given file in a container. This does not require the
        engine to be installed on the system."""
        logger.info("Run container BEAST X")
        raise NotImplementedError
