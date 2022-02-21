from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in unizone_app/__init__.py
from unizone_app import __version__ as version

setup(
	name="unizone_app",
	version=version,
	description="custome app for unizone",
	author="akshay",
	author_email="akshay@pseudocode.co",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
