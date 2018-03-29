from setuptools import setup, find_packages

setup(name='galileopy',
      version='0.1',
      description='A package for downloading, reading, and creating summary plots of the Galileo Orbiter mission data available on NASA PDS.',
      url='https://github.com/cdkharris/galileopy.git',
      author='Camilla D. K. Harris',
      author_email='cdha@umich.edu',
      license='MIT',
      packages=find_packages(),
      python_requires='>=3',
      zip_safe=False)
