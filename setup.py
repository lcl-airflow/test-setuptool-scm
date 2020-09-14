from setuptools import find_packages, setup
from setuptools_scm import get_version


setup(
    name='src',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=find_packages(),
    version= get_version(),
    description='this is a dev ops demo',
    author='herman cheung',
    license='',
)

