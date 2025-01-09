# read version from installed package
from importlib.metadata import version
__version__ = version("pycounts")
from .pycounts import load_text, clean_text, count_words
