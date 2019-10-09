# setup.py

import pathlib

import setuptools

PROJECT_DIR = pathlib.Path(__file__).parent

DISTRIBUTION_PACKAGE_NAME = "hello"
VERSION = "0.1.0"
DESCRIPTION = "Greetings."
CONSOLE_SCRIPTS = ["greet = greetings.cli:cli"]


INSTALL_REQUIRES = (PROJECT_DIR / "requirements.in").read_text().splitlines()

setuptools.setup(
    name=DISTRIBUTION_PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    entry_points={"console_scripts": CONSOLE_SCRIPTS},
)
