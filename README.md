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

To run the project we have a few commands neccessary:

1. Setup a virtual environment: `python3 -m venv venv`
2. Activate it: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Install packages: `pip install -e .`

# Running the tests:

The run-tests command (when not using browserstack), creates an allure report to give a better visual output of test results. It clears the current result state and overwrites it with the next run. To run the tests without this reporter we have to run the other commands such as "behave" or "pytest"(dependent on the tests you want to run)

GUI:

- Run tests using behave directly`behave`
- Run tests with test runner which produces report using Allure `run-tests gui`

These commands will run the full BDD suite of tests, the "run-tests" command can only be run if the 'pip install -e .' command is run because this installs the package neccesary to run the command
(If any changes are made to the project structure and we want to run the tests using 'run-tests', a fresh 'pip install -e .' is needed for the project to relocate the relevant features)
To run individual feature we can run behave 'path to feature'

API:

- Run full collection: `pytest tests/api`
- Run specific file: `pytest tests/api/'fileName'`
- Run test using test runner which uses Allure to create report `run-tests api`

BrowserStack:

- `run-tests gui --browserstack`
- `browserstack-sdk behave`

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
- Mobile - Through the browserstack guide, playwright with browserstack cannot be used to emulate an iPhone or iOS and any attempts with android result in the device and chrome browser being spun up but the tests not beginning. I experienced a similar issue when attempting this with Playwright and typescript, I put it down to an issue with playwright not being fantastic when working with browserstack

The following links can help adjust browsers and OS if need be:

- https://www.browserstack.com/docs/automate/playwright/browsers-and-os
- https://www.browserstack.com/list-of-browsers-and-platforms/playwright
