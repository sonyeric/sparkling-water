# encoding: utf-8
# module pySparkling
# from (pysparkling)
"""
pySparkling - The Sparkling-Water Python Package
=====================
"""
import zipfile
from codecs import open
from os import path

here = path.dirname(path.abspath(path.dirname(__file__)))
if '.zip' in here:
    with zipfile.ZipFile(here, 'r') as archive:
        __version__ = archive.read('version.txt')
else:
    with open(path.join(here, 'version.txt'), encoding='utf-8') as f:
        version = f.read()


# set imports from this project which will be available when the module is imported
from pysparkling.context import H2OContext
from pysparkling.conf import H2OConf

# set what is meant by * packages in statement from foo import *
__all__ = ["H2OContext", "H2OConf"]
