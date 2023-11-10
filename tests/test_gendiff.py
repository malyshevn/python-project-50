from gendiff.scripts.gendiff import generate_diff
import yaml


def test_generate_diff():
    file1 = './tests/fixtures/file1.json'
    file2 = './tests/fixtures/file2.json'
    result = './tests/fixtures/result.json'

    generated_diff = generate_diff(file1, file2)
    with open(result, 'r') as new_result_file:
        expected_result = new_result_file.read().splitlines()

    print("Generated Diff:")
    print(generated_diff)
    print("Expected Result:")
    print(expected_result)

    assert generated_diff == expected_result


def test_generate_diff_yaml():
    file1 = './tests/fixtures/file1.yaml'
    file2 = './tests/fixtures/file2.yaml'
    result = './tests/fixtures/result.txt'

    generated_diff = generate_diff(file1, file2)
    with open(result, 'r') as new_result_file:
        expected_result = new_result_file.read().splitlines()

    print("Generated Diff:")
    print(generated_diff)
    print("Expected Result:")
    print(expected_result)

    assert generated_diff == expected_result
