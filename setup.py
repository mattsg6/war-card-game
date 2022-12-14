from setuptools import setup, find_packages

from main import __version__

setup(
    name='war-card-game',
    version=__version__,

    url='https://github.com/mattsg6/war-card-game',
    author='Matthew Gilmore',
    author_email='thegilmores.matt@gmail.com',

    ppackages=find_packages(),

    entry_points={
    'console_scripts': [
        'play-war=main.__init__:cmd_start',
    ],
},
)