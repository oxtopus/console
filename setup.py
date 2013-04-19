from setuptools import find_packages, setup

from tools import __version__

setup(
  name='tools',
  packages=find_packages(),
  version=__version__,
  entry_points = {
    'console_scripts': [
      'runner = tools.runner:main',
      'example = tools.runner.example:Example',
      'foo = tools.commands:foo',
      'bar = tools.commands:bar'
    ]
  }
)