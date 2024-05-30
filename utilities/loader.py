from os import path

def load_input(source_path: str, filename: str) -> list[str]:
    full_path = path.join(source_path, filename)

    if not path.exists(full_path):
        raise RuntimeError(f"Provided path {full_path} not valid")

    lines = []
    with open(full_path) as input_file:
        lines.extend([line.rstrip() for line in input_file])
    return lines

