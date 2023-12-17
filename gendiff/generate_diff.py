from gendiff.create_diff import create_diff
from gendiff.parser import load_data
from gendiff.formatters import make_stylish, make_plain, make_json


def generate_diff(file_path1, file_path2, format_name="stylish"):
    file1 = load_data(file_path1)
    file2 = load_data(file_path2)
    data = create_diff(file1, file2)

    match format_name:
        case 'stylish':
            return make_stylish(data)
        case 'plain':
            return make_plain(data)
        case 'json':
            return make_json(data)
