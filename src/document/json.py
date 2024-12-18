import json
import os

class Json:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f'File not found in path: {self.file_path}')
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data