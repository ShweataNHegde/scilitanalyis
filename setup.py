mport pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="scilit-analysis",
    version="0.0.1",
    description="Automated scoping review and analysis of scientific literature on genes. Relies on pygetpapers and ami.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ShweataNHegde/scilitanalyis",
    author="Shweata N. Hegde",
    author_email="shweata.hegde@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["scilitanalysis"],
    include_package_data=True,
    install_requires=["yake", "scispacy", "spacy", "pygetpapers", "bs4"],
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)
