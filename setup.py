from distutils.core import setup
import py2exe
import Cryptodome
import argparse
import sys
import os
from glob import glob

sys.path.append("C:")
data_files = [
    ("msvcp100", glob(r'.\*.dll'))]
setup(
    data_files=data_files,
    windows=['main.py']
)
