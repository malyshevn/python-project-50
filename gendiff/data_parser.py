import json
import yaml
import os


def load_data(file_path):
    _, extension = os.path.splitext(file_path)
    extension = extension.lower()

    if extension == '.json':
        with open(file_path) as file:
            return json.load(file)
    elif extension == '.yaml' or extension == '.yml':
        with open(file_path) as file:
            return yaml.load(file, Loader=yaml.Loader)
    else:
        raise ValueError(f'Unsupported file format: {extension}')

# не совсем понял замечание, поэтому толком ничего не изменил в функции парсера
