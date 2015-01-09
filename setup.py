#!/usr/bin/env python
from setuptools import setup

setup(
    name="Grenade",
    description="Fragment packets on arbitrary size boundaries",
    version="0.1.dev1",
    author="Joel Cornett",
    author_email="joel.cornett@gmail.com",
    url="https://github.com/jncornett/grenade",
    scripts=["grenade.py"],
    install_requires=[
        "scapy>=2.3.1",
        "netaddr>=0.7.12"
        ]
    )


