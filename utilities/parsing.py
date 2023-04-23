def load_input(file_name: str) -> list:
    lines = []
    with open(file=file_name, mode="r") as file:
        lines = file.readlines()
    return lines
