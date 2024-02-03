import json
import yaml
import os


def get_extension(file):
    _, extension = os.path.splitext(file)
    return extension[1:]


def load_data(file_path):
    ext = get_extension(file_path)

    if ext == 'json':
        with open(file_path) as file:
            return json.load(file)
    elif ext == 'yaml' or ext == 'yml':
        with open(file_path) as file:
            return yaml.load(file, Loader=yaml.Loader)
    else:
        raise ValueError(f'Unsupported file format: {ext}')
