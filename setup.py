from distutils.core import setup
from setuptools import find_packages


setup(name= 'du82dady',
      version='0.1',
     author= 'DSSS',
     author_email= 'shamama.safdar@fau.de',
     packages= find_packages(),
     install_requires= ['numpy', 'Pillow', 'ipywidgets'])
