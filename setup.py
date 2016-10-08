#from distutils.core import setup
from setuptools import setup, find_packages

#dependecy_links = ["git+https://github.com/pexpect/pexpect.git#egg=pexpect-0.1"]
install_requires = ['quandl','wbpy']

setup(
    name='um',
    version='0.13',
    packages=['um',],
    install_requires=install_requires,
    entry_points = { 'console_scripts': [
        "um = um.um:cli", ],
        },
    author = "Dusty C",
    author_email = "bsdpunk@gmail.com.com",
    description = "A Modal Terminal for Financial Data",
    license = "BSD",
    keywords = "Shell cli terminal financial data",
    url = 'bsdpunk.blogspot.com'   
    )
