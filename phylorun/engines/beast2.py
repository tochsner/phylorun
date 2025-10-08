from pathlib import Path
from typing import Optional
from phylorun.engines.engine import Engine
from xml.etree import ElementTree

from loguru import logger


class BEAST2(Engine):
    def name(self) -> str:
        """Returns the name of the engine as used in the CLI."""
        return "beast2"

    def can_run_analysis(self, analysis_file: Path) -> bool:
        """Checks if BEAST 2 can run the analysis in the given file."""
        try:
            xml = ElementTree.parse(analysis_file)
        except ElementTree.ParseError:
            logger.debug("No BEAST 2 file: no XML file.")
            return False

        root = xml.getroot()

        if root is None or root.tag.lower() != "beast":
            logger.debug("No BEAST 2 file: no root BEAST tag.")
            return False

        if not root.attrib.get("version", "").startswith("2."):
            logger.debug("No BEAST 2 file: wrong version (likely for BEAST X).")
            return False

        if not any(child.tag.lower() == "data" for child in root) and not any(
            child.tag.lower() == "alignment" for child in root
        ):
            logger.debug("No BEAST 2 file: no <data> tag.")
            return False

        if not any(child.tag.lower() == "run" for child in root):
            logger.debug("No BEAST 2 file: no <run> tag.")
            return False

        logger.debug("BEAST 2 file found.")

        return True

    def run_local_analysis(
        self,
        analysis_file: Path,
        engine_path: Optional[str] = None,
        additional_cli_args: Optional[list[str]] = None,
    ) -> bool:
        """Runs the analysis in the given file using the locally installed engine."""
        logger.info("Run local BEAST 2")
        raise NotImplementedError

    def run_containerized_analysis(
        self, analysis_file: Path, additional_cli_args: Optional[list[str]] = None
    ) -> bool:
        """Runs the analysis in the given file in a container. This does not require the
        engine to be installed on the system."""
        logger.info("Run container BEAST 2")
        raise NotImplementedError
