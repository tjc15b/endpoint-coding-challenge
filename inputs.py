import sys
from commands import create, delete, list_dir, move

def read_input() -> list[str]:
    lines = []
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    lines.append(line.strip())
        except FileNotFoundError:
            print(f"Error: File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
    else: # read from stdin, end input with CTRL+D
        lines = sys.stdin.read().splitlines()
    
    return lines

def process_input(lines: list[str]):
    for line in lines:
        command_parts = line.split()
        command = command_parts[0]
        args = command_parts[1:]

        if not command_parts:
            print("Error: Empty or invalid command")
            continue

        if command == "CREATE":
            if len(args) < 1:
                print(line)
                print("Error: CREATE command requires a path")
                continue
            create(args[0])
        elif command == "DELETE":
            if len(args) < 1:
                print(line)
                print("Error: DELETE command requires a path")
                continue
            delete(args[0])
        elif command == "LIST":
            print("LIST")
            list_dir()
        elif command == "MOVE":
            if len(args) < 2:
                print(line)
                print("Error: MOVE command requires a source path and a destination path")
                continue
            move(args[0], args[1])
        else:
            print(f"Unknown command: {command}")
