from setuptools import setup

from main import __version__

setup(
    name='war-card-game',
    version=__version__,

    url='https://github.com/mattsg6/war-card-game',
    author='Matthew Gilmore',
    author_email='thegilmores.matt@gmail.com',

    py_modules=['main'],
)