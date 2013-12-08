from distutils.core import setup

setup(
  name='pystitch',
  packages = ['pystitch'],
  package_data={'pystitch': ['data/*.csv']},
  version='0.0.1',
  description='Python tools for cross-stiching',
  author='Nathan Naze',
  author_email='nanaze@gmail.com',
  url='https://pypi.python.org/pypi/pystitch'
)
