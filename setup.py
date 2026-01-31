from setuptools import setup, find_packages

setup(
    name="py-scraper-rotator-x",
    version="2.4.1",
    description="Enterprise-grade scraping rotation middleware",
    author="Zenus Systems",
    packages=find_packages(),
    install_requires=[
        "requests",
        "fake-useragent",
    ],
)
