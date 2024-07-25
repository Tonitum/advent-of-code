from abc import abstractmethod, ABCMeta
from utilities.loader import load_input

class Day(metaclass=ABCMeta):
    def get_input_lines(self, file_path:str, file_name:str) -> list[str]:
        return load_input(file_path, file_name)

    @abstractmethod
    def process_input(self, file_path: str, file_name: str) -> int:
        return
