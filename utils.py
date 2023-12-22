import os
import inspect

DATA_FILE_NAME = "input.txt"

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def read_data():
    for frame in inspect.stack():
        if "day" in frame.filename:
            path = os.path.join(os.path.dirname(frame.filename), DATA_FILE_NAME)
            return read_file(path)
    return None