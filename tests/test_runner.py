import subprocess
import sys
import os
import shutil

def clear_previous_results():
    allure_results_dir = "reports"
    if os.path.exists(allure_results_dir):
        shutil.rmtree(allure_results_dir)
    os.makedirs(allure_results_dir)

def run_gui_tests():
    if os.getenv('USE_BROWSERSTACK'):
        subprocess.run(["browserstack-sdk", "behave", "tests/gui/features"])
    else:
        subprocess.run(["behave", "tests/gui/features", "--format", "allure_behave.formatter:AllureFormatter", "--outfile", "reports/allure-results"])

def run_api_tests():
    subprocess.run(["pytest", "tests/api", "--alluredir=reports/allure-results"])

def generate_allure_report():
    subprocess.run(["allure", "generate", "reports/allure-results", "-o", "reports/allure-report"])
    subprocess.run(["allure", "open", "reports/allure-report"])

def run_accessibility_tests():
    subprocess.run(["behave", "tests/gui/accessibility/features", "--format", "allure_behave.formatter:AllureFormatter", "--outfile", "reports/allure-results"])    

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python test_runner.py [gui|api] [--browserstack]")
        sys.exit(1)

    test_type = sys.argv[1]
    use_browserstack = len(sys.argv) == 3 and sys.argv[2] == '--browserstack'

    if use_browserstack:
        os.environ['USE_BROWSERSTACK'] = '1'

    clear_previous_results()

    if test_type == "gui":
        run_gui_tests()
    elif test_type == "api":
        run_api_tests()
    elif test_type == "accessibility":
        run_accessibility_tests()
    else:
        print("Unknown test type. Use 'gui' or 'api' or 'accessibility.")
        sys.exit(1)

    if not use_browserstack:
        generate_allure_report()

if __name__ == "__main__":
    main()
