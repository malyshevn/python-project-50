import argparse
import json

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help = 'set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))

def generate_diff(file_path_1, file_path_2):
    with open(file_path_1) as file1, open(file_path_2) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

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

    return '\n'.join(diff)

if __name__ == "__main__":
    main()