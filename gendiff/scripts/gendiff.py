from gendiff.parser import parser, load_data
from gendiff.formatters import make_stylish, make_plain, format_json
from gendiff.create_diff import create_diff


def main():
    first_file, second_file, format = parser()
    data = create_diff(load_data(first_file), load_data(second_file))

    match format:
        case "stylish":
            return make_stylish(data)
        case "plain":
            return make_plain(data)
        case "json":
            return make_json(data)


if __name__ == "__main__":
    main()
