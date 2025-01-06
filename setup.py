from setuptools import setup, find_packages

setup(
    name="change_encoding",
    version="1.0.0",
    author="Software Witchcraft",
    author_email="hi@softwarewitchcraft.com",
    description="A script to convert text file encoding",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SoftwareWitchcraft/chenge_encoding",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "chenc=change_encoding.change_encoding:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
