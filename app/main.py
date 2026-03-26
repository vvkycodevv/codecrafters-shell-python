import sys
import os
import subprocess

builtins = ["exit", "type", "echo"]

def main():
    while True:
        sys.stdout.write("$ ")
        command = input()

        if command == "exit":
            break

        if command == "echo" or command.startswith("echo "):
            print(command[5:])

        elif command.startswith("type"):
            cmd = command[5:].strip()

            if cmd in builtins:
                print(f"{cmd} is a shell builtin")

            else:
                for directory in os.environ.get("PATH").split(os.pathsep):
                     full_path = os.path.join(directory, cmd)

                     if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        print(f"{cmd} is {full_path}")
                        break

                else:
                    print(f"{cmd}: not found")

        else:
            exe = command.split()
            for directory in os.environ.get("PATH").split(os.pathsep):
                full_path = os.path.join(directory, exe[0])
                
                if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                    subprocess.run(exe)
                    break
        
                else:
                    print(f"{command}: not found")




if __name__ == "__main__":
    main()
