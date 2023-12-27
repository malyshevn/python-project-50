from gendiff import generate_diff, parser


def main():
    first_file, second_file, format = parser()
    print(generate_diff(first_file, second_file, format))


if __name__ == "__main__":
    main()
