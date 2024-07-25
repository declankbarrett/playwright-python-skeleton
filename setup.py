from setuptools import setup, find_packages

setup(
    name="python-bdd-project",
    version="1.0.0",
    description="A Python project with BDD tests using Behave and Playwright",
    author="Your Name",
    packages=find_packages(where='tests'),
    install_requires=[
        "behave",
        "playwright",
        "pytest",  # Ensure pytest is included for API tests
    ],
    entry_points={
        "console_scripts": [
            "run-tests=tests.test_runner:main",  # Single entry point for both types of tests
        ],
    },
)