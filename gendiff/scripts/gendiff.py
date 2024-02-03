from gendiff.generate_diff import generate_difference
from gendiff.cli import parser


def main():
    first_file, second_file, format_name = parser()
    print(generate_difference(first_file, second_file, format_name))


if __name__ == "__main__":
    main()
