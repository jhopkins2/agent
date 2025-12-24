from functions.get_files_info import get_files_info

def main():
    tests = [   
             ("calculator", ".", "- main.py: file_size=719 bytes, is_dir=False\n- tests.py: file_size=1331 bytes, is_dir=False\n- pkg: file_size=44 bytes, is_dir=True"),
             ("calculator", "pkg", "- calculator.py: file_size=1721 bytes, is_dir=False\n- render.py: file_size=376 bytes, is_dir=False"),
             ("calculator", "/bin", 'Error: Cannot list "/bin" as it is outside the permitted working directory'),
             ("calculator", "../", 'Error: Cannot list "../" as it is outside the permitted working directory'),
            ]

    for current, target, answer in tests:
        result = get_files_info(current, target)
        print(f"Result for '{target}' directory:")
        print(result)

        if result == answer:
            print("Result matches with answer")
        else:
            print("Result does not match with answer")

if __name__ == "__main__":
    main()
