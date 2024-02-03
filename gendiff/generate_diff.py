from gendiff.create_diff import create_diff
from gendiff.data_parser import load_data
from gendiff.formatters.format import choose_format


def generate_difference(file_path1, file_path2, format_name="stylish"):
    file1 = load_data(file_path1)
    file2 = load_data(file_path2)
    data = create_diff(file1, file2)
    return choose_format(data, format_name)
