import sys

builtins = ["exit", "type", "echo"]

def main():
    while True:
        sys.stdout.write("$ ")
        command = input()

        if command == "exit":
            break

        if command.startswith("echo"):
            print(command[5:])

        if command.startswith("type"):
            cmd = command[5:].strip()

            if cmd in builtins:
                print(f"{cmd} is a shell builtin")
            else:
                print(f"{cmd}: not found")




if __name__ == "__main__":
    main()
