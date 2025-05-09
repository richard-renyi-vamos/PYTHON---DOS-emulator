import os
import sys

def dos_emulator():
    current_dir = os.getcwd()
    print("Welcome to PyDOS 💾🖥️ (type HELP for commands)\n")

    while True:
        command = input(f"{current_dir}> ").strip().upper()

        if command == "EXIT":
            print("Exiting PyDOS... Bye! 👋")
            break

        elif command == "DIR":
            print("\nDirectory listing:\n")
            for item in os.listdir(current_dir):
                print(item)
            print()

        elif command.startswith("CD "):
            path = command[3:].strip()
            new_dir = os.path.join(current_dir, path)
            if os.path.isdir(new_dir):
                current_dir = os.path.abspath(new_dir)
            else:
                print("Directory not found.\n")

        elif command.startswith("TYPE "):
            filename = command[5:].strip()
            filepath = os.path.join(current_dir, filename)
            if os.path.isfile(filepath):
                with open(filepath, 'r', encoding='utf-8') as file:
                    print("\n" + file.read() + "\n")
            else:
                print("File not found.\n")

        elif command == "HELP":
            print("""
Supported commands:
DIR         - List files and folders
CD [folder] - Change directory
TYPE [file] - Show file content
EXIT        - Exit the emulator
HELP        - Show this help menu
""")

        else:
            print("Unknown command. Type HELP for list of commands.\n")

# Run the emulator
if __name__ == "__main__":
    dos_emulator()
