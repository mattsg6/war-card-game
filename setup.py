from setuptools import setup, find_packages

from cardpackage import __version__

setup(
    name='war-card-game',
    version=__version__,

    url='https://github.com/mattsg6/war-card-game',
    author='Matthew Gilmore',
    author_email='thegilmores.matt@gmail.com',

    packages=find_packages(),
    license='GNU GENERAL PUBLIC LICENSE',

    entry_points={
    'console_scripts': [
        'play-war=cardpackage.main:cmd_start',
    ],
},
)