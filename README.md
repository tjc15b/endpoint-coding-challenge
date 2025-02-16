# endpoint-coding-challenge
Endpoint Backend Coding Challenge


# Directory Tree

This script provides a basic implementation of a hierarchical file system manager, allowing you to create, move, delete, and list directories using commands.

## Features
- **CREATE**: Create directories and subdirectories.
- **MOVE**: Move directories from one location to another.
- **DELETE**: Delete directories.
- **LIST**: List the entire directory structure.

## Project Structure
- **commands.py**: Implements functions for create/move/delete/list
- **inputs.py**: Implements functions for reading and processing user input
- **directories.py**: Main execution entrypoint for the script
- **example_inputs**: Folder containing some example input text files for use with the script

## Requirements
- Python 3.7 or higher

## How to Run

First navigate to the project's root directory. Then, there are two ways to run the code/submit input values:

1. With textfile as input:

    `python3 directories.py example_inputs/input.txt`

2. With stdin as input (CTRL+D to end input):
    
    `python3 directories.py`
