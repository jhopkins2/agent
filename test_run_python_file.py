from functions.run_python_file import run_python_file

def main():
    
    tests=[
            ("calculator", "main.py"),
            ("calculator", "main.py", ["3 + 5"]),
            ("calculator", "tests.py"),
            ("calculator", "../main.py"),
            ("calculator", "nonexistent.py"),
            ("calculator", "lorem.txt"),
          ]

    for test in tests:

        if len(test) == 2:
            result = run_python_file(test[0], test[1])
        
        if len(test) > 2:
            result = run_python_file(test[0], test[1], *test[2:])

        print("--------------------------------------------------------")
        print(result)

if __name__ == "__main__":
    main()
