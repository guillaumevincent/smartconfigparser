from distutils.core import setup
from smartconfigparser import __version__

setup(
    name='smartconfigparser',
    version=__version__,
    author='Guillaume Vincent',
    author_email='gvincent@oslab.fr',
    packages=['smartconfigparser', 'smartconfigparser.tests'],
    url='http://gitlab.oslab.fr/oslab/smartconfigparser.git',
    license='wtfpl - Do what the fuck you want to public license',
    description='SmartConfigParser add missing default value in ConfigParser module',
    long_description=open('README.md').read(),
    install_requires=[],
)
