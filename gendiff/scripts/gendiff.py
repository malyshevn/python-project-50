from gendiff.parser import parser, load_data
from gendiff.generate_diff import generate_diff
from gendiff.formatters.stylish import format_stylish
from gendiff.create_diff import create_diff, key_changes


def main():
    args = parser()
    data = create_diff(load_data(args.first_file), load_data(args.second_file))
    return format_stylish(data)

if __name__ == "__main__":
    main()