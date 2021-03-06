#! python3  # noqa: E265

"""
    Launch PyInstaller using a Python script.
"""

# #############################################################################
# ########## Libraries #############
# ##################################

# Standard library
from os import getenv
from pathlib import Path
import platform
import sys

# 3rd party
import PyInstaller.__main__

# package
sys.path.insert(0, str(Path(".").resolve()))
from dicogis import __about__  # noqa: E402


# #############################################################################
# ########### MAIN #################
# ##################################
package_folder = Path("dicogis")

PyInstaller.__main__.run(
    [
        "--add-binary={};bin/img/".format((package_folder / "bin/img/").resolve()),
        "--add-data={};locale/".format((package_folder / "locale/").resolve()),
        "--add-data=options_TPL.ini;.",
        "--add-data=LICENSE;.",
        "--add-data=README.md;.",
        "--clean",
        # "--debug=all",
        "--icon={}".format((package_folder / "bin/img/DicoGIS.ico").resolve()),
        "--log-level={}".format(getenv("PYINSTALLER_LOG_LEVEL", "WARN")),
        "--manifest={}".format((package_folder / "../builder/manifest.xml").resolve()),
        "--name={}_{}_{}{}_Python{}-{}".format(
            __about__.__title_clean__,
            __about__.__version__.replace(".", "-"),
            platform.system(),
            platform.architecture()[0],
            platform.python_version_tuple()[0],
            platform.python_version_tuple()[1],
        ),
        "--noconfirm",
        "--noupx",
        "--onedir",
        # "--onefile",
        "--version-file={}".format("version_info.txt"),
        "--windowed",
        str(package_folder / "DicoGIS.py"),
    ]
)
