from setuptools import setup

setup(
    name='batteryratecap',
    version='0.1.0',    
    description='A Python package for batter rate capability analysis',
    url='https://github.com/BatteryDesign/BatteryRateCap.git',
    author='Chih-Hsuan Hung, Praise Anyanwu, Kevin Martinez-Chavez, Matthew J. Canin,and Kevin G. Lee',
    author_email='dhung@uw.edu',
    license='MIT',
    packages=['fitcaprate','data_converter','visualization','correlationtest'],
)