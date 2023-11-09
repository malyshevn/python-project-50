from gendiff.parser import parser, load_data


def main():
    args = parser()
    print(generate_diff(args.file_path_1, args.file_path_2))


def generate_diff(file_path_1, file_path_2):
    data1 = load_data(file_path_1)
    data2 = load_data(file_path_2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff.append(f"  {key}: {data1[key]}")
            else:
                diff.append(f"- {key}: {data1[key]}")
                diff.append(f"+ {key}: {data2[key]}")
        elif key in data1:
            diff.append(f"- {key}: {data1[key]}")
        else:
            diff.append(f"+ {key}: {data2[key]}")

        return diff


if __name__ == "__main__":
    main()
