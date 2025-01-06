from setuptools import setup, find_packages

setup(
    name="chenc",
    version="1.0.0",
    author="Software Witchcraft",
    author_email="hi@softwarewitchcraft.com",
    description="A script to convert text file encodings",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SoftwareWitchcraft/chenc",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "chenc=chenc.chenc:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
