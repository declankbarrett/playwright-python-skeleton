import subprocess
import sys
import os

def run_gui_tests():
    if os.getenv('USE_BROWSERSTACK'):
        subprocess.run(["browserstack-sdk", "behave", "tests/gui/features"])
    else:
        subprocess.run(["behave", "tests/gui/features"])

def run_api_tests():
    subprocess.run(["pytest", "tests/api"])

def run_accessibility_tests():
    subprocess.run(["behave", "tests/gui/accessibility/features"])    

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python test_runner.py [gui|api] [--browserstack]")
        sys.exit(1)

    test_type = sys.argv[1]
    use_browserstack = len(sys.argv) == 3 and sys.argv[2] == '--browserstack'

    if use_browserstack:
        os.environ['USE_BROWSERSTACK'] = '1'

    if test_type == "gui":
        run_gui_tests()
    elif test_type == "api":
        run_api_tests()
    elif test_type == "accessibility":
        run_accessibility_tests()
    else:
        print("Unknown test type. Use 'gui' or 'api' or 'accessibility.")
        sys.exit(1)

if __name__ == "__main__":
    main()
