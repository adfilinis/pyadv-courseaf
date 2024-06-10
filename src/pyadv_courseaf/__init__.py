"""Demo package for live course"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pyadv-courseaf")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Adrianos Filinis"
__email__ = "adrianos.filinis@unibe.ch"

from . import algos
