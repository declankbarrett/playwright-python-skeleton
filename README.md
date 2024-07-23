# Python - Playwright - Skeleton

This is a skeleton for a Python and Playwright testing framework. It encompasses the following aspects:
- BDD using Behave
- POM (Page object model)
- Non BDD version of test runs (for comparison)
- API Testing using playwright
- Compatibility testing
- Accessibility testing

# Prerequisites:
Please ensure you have the following installed and up to date
- Python (Can be done through HomeBrew or Python website)
- PIP (Installed with python but ensure it is up to date)

To run the project we have a few commands neccessary:
- pip install -r requirements.txt
- pip install -e .
(If these do not work, please install modules individually using PIP)

Running the tests:
- behave
- run-tests 
These commands will run the full BDD suite of tests, the "run-tests" command can only be run if the 'pip install -e .' command is run because this installs the package neccesary to run the command
To run individual feature we can run behave 'path to feature'
