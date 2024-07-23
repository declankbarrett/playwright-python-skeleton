import subprocess

def main():
    # Add any pre-test setup or configuration here if needed
    subprocess.run(["behave", "tests/features"])

if __name__ == "__main__":
    main()