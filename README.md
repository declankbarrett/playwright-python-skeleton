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
GUI:

- behave
- run-tests gui
  These commands will run the full BDD suite of tests, the "run-tests" command can only be run if the 'pip install -e .' command is run because this installs the package neccesary to run the command
  (If any changes are made to the project structure and we want to run the tests using 'run-tests', a fresh 'pip install -e .' is needed for the project to relocate the relevant features)
  To run individual feature we can run behave 'path to feature'

API:

- pytest test/api (to run full collection)
- pytest test/api/'file' (to run a specific file)
- run-tests api
  (This command has the same prerequisites as the GUI version, so if our project is restructured we need to run 'pip install -e . again)

Accessibility:

- run-tests accessibility

At the moment this is set up to use the axe-core js script, but inside a python file, after looking around for alternatives including python axe-core libraries, this is the best I could come to. It reports any and all accessibility issues on the pages, so needs adjustment to only report severe issues. It creates an accessibility report however this is quite extensive due to the number of accessibility issues it found on each page.
It also uses the feature file and flow from page to page, this could be changed, but due to the optimisation of the accessibility checks themselves not being perfect, I have left this out for now. Overall it doesn't seem like python especially with playwright is a great accessibility testing tool.
