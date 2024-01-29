from gendiff import generate_diff
from gendiff.cli import parser


def main():
    first_file, second_file, format_name = parser()
    print(generate_diff(first_file, second_file, format_name))


if __name__ == "__main__":
    main()
