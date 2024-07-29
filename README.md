# Python - Playwright - Skeleton

This is a skeleton for a Python and Playwright testing framework. It encompasses the following aspects:

- BDD using Behave
- POM (Page object model)
- Non BDD version of test runs (for comparison)
- API Testing using playwright
- Compatibility testing - BrowserStack
- Allure as a test result reporter
- Accessibility testing

# Prerequisites:

Please ensure you have the following installed and up to date

- Python (Can be done through HomeBrew or Python website)
- PIP (Installed with python but ensure it is up to date)

To run the project we have a few commands neccessary:

- pip install -r requirements.txt
- pip install -e .
  (If these do not work, please install modules individually using PIP)

# Running the tests:

The run-tests command (when not using browserstack), creates an allure report to give a better visual output of test results. It clears the current result state and overwrites it with the next run. To run the tests without this reporter we have to run the other commands such as "behave" or "pytest"(dependent on the tests you want to run)

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

BrowserStack:

- run-tests gui --browserstack
- browserstack-sdk behave

The tests can be ran on browserstack via the 2 run commands above, you need to adjust the browserstack.yml file to include your credentials first however and ensure you have either installed the relevant libraries manually or through the requirements.txt file
They run across the following browsers and OS:

- Windows
  - Chrome
  - Edge
  - Firefox (Flaky)
- macOS
  - Chrome
  - Safari
  - Firefox
- Mobile
  Through the browserstack guide, playwright with browserstack cannot be used to emulate an iPhone or iOS and any attempts with android result in the device and chrome browser being spun up but the tests not beginning. I experienced a similar issue when attempting this with Playwright and typescript, I put it down to an issue with playwright not being fantastic when working with browserstack
  The following links can help adjust browsers and OS if need be:
- https://www.browserstack.com/docs/automate/playwright/browsers-and-os
- https://www.browserstack.com/list-of-browsers-and-platforms/playwright
