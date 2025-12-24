from functions.write_file import write_file

def main():
    tests = [
                ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
                ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
                ("calculator", "/tmp/temp.txt", "this should not be allowed"),

            ]

    for current, filename, content in tests:
        print("------------------------------------------")
        print(f"Result: {write_file(current, filename, content)}")

if __name__ == "__main__":
    main()
