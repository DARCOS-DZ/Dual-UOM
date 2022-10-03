from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dual_uom/__init__.py
from dual_uom import __version__ as version

setup(
	name="dual_uom",
	version=version,
	description="Extends ERPNext for dual UOM uses",
	author="Darcos",
	author_email="contact@darcos.dz",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
