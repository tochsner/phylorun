from pathlib import Path
from typing import Optional
from phylorun.engines.engine import Engine
from xml.etree import ElementTree

from loguru import logger


class BEASTX(Engine):
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
    ) -> bool:
        """Runs the analysis in the given file using the locally installed engine."""
        raise NotImplementedError

    def run_containerized_analysis(
        self, analysis_file: Path, additional_cli_args: Optional[list[str]] = None
    ) -> bool:
        """Runs the analysis in the given file in a container. This does not require the
        engine to be installed on the system."""
        raise NotImplementedError
