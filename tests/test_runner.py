import subprocess
import sys

def run_gui_tests():
    subprocess.run(["behave", "tests/gui/features"])

def run_api_tests():
    subprocess.run(["pytest", "tests/api"])

def run_accessibility_tests():
    subprocess.run(["behave", "tests/gui/accessibility/features"])    

def main():
    if len(sys.argv) != 2:
        print("Usage: python test_runner.py [gui|api]")
        sys.exit(1)

    test_type = sys.argv[1]

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