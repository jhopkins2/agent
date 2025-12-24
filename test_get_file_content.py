from functions.get_file_content import get_file_content

def main():
    tests = [
                ("calculator", "lorem.txt"),
                ("calculator", "main.py"),
                ("calculator", "pkg/calculator.py"),
                ("calculator", "/bin/cat"),
                ("calculator", "pkg/does_not_exist.py"),
            ]

    for working_dir, target_file in tests:
        result = get_file_content(working_dir, target_file)
        print("---------------------------------------------------------")
        print(f"Working Directory: {working_dir}")
        print(f"Target File: {target_file}\n")
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
