import sys

def main():
    sys.stdout.write("$ ")
    command = input()
    print("{command}: command not found")
    pass


if __name__ == "__main__":
    main()
