from setuptools import setup, find_packages

setup(
    name="python-bdd-project",
    version="1.0.0",
    description="A Python project with BDD tests using Behave and Playwright",
    author="Author name",
    packages=find_packages(where='tests'),
    install_requires=[
        "behave",
        "playwright",
        "pytest",
        'browserstack-sdk',
        "allure-behave",
        "allure-pytest",  
    ],
    entry_points={
        "console_scripts": [
            "run-tests=tests.test_runner:main",  # Single entry point for all types of tests
        ],
    },
)