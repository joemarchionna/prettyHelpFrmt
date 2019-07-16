import setuptools
from setuptools import setup

setup(
    name="prettyHelpFrmt",
    version="1.0.0",
    author="Joe Marchionna",
    author_email="joemarchionna@gmail.com",
    description="Project Description",
    long_description=open("readme.md").read(),
    license=open("license.md").read(),
    packages=setuptools.find_packages(),
    url="https://github.com/joemarchionna/prettyHelpFrmt",
	install_requires=["argparse"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
)
