from setuptools import setup, find_packages
import subprocess

def run_behave_tests():
    subprocess.run(["behave", "tests/features"])

setup(
    name="python-bdd-project",
    version="1.0.0",
    description="A Python project with BDD tests using Behave and Playwright",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "behave",
        "playwright"
    ],
    entry_points={
        "console_scripts": [
            "run-tests=tests.test_runner:main",
        ],
    },
)