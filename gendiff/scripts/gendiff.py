from gendiff import generate_diff, parser


def main():
    first_file, second_file, format_name = parser()
    print(generate_diff(first_file, second_file, format_name))


if __name__ == "__main__":
    main()
