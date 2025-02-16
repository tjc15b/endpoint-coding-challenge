directory = {}

def create(path: str):
    print(f"CREATE {path}")
    parts = path.split("/")
    current = directory

    for part in parts:
        if part not in current:
            current[part] = {}
        current = current[part]


def delete(path: str):
    print(f"DELETE {path}")
    parts = path.split("/")
    current = directory

    # traverse through the path to ensure all directories exist
    for part in parts[:-1]:
        if part not in current:
            print(f"Cannot delete {path} - {part} does not exist")
            return
        current = current[part]

    # attempt to delete the target directory
    target = parts[-1]
    if target in current:
        del current[target]
    else:
        print(f"Cannot delete {path} - {target} does not exist")


def list_dir(current=None, depth=0):
    if current is None:
        current = directory
    for key in sorted(current.keys()):  # alphabetical order
        print("  " * depth + key)  # print proper indentation + key
        list_dir(current[key], depth + 1)  # call self recursively, adding depth


def move(source: str, destination: str):
    print(f"MOVE {source} {destination}")
    src_parts = source.split("/")
    dest_parts = destination.split("/")
    current = directory

    # traverse to the parent of the source
    for part in src_parts:
        if part not in current:
            print(f"Cannot move {source} - {part} does not exist")
            return
        parent = current
        current = current[part]

    # extract the source directory
    target = src_parts[-1]
    src_dir = current

    # delete the source
    del parent[target]

    # traverse to the destination
    current = directory
    for part in dest_parts:
        if part not in current:
            current[part] = {}
        current = current[part]

    # move the directory
    current[target] = src_dir
