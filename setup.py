from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="artiq_toptica_dlcpro",
    install_requires=required,
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "aqctl_artiq_toptica_dlcpro = artiq_toptica_dlcpro.aqctl_artiq_toptica_dlcpro:main",
        ],
    },
)
