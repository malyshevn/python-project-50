import argparse
import json
import yaml
import os


def parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        default="stylish",
                        choices=["stylish", "plain", "json"])
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format


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
