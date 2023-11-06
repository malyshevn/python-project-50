from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    file1 = './tests/fixtures/file1.json'
    file2 = './tests/fixtures/file2.json'
    result = './tests/fixtures/result.json'

    with open(result, 'r') as new_result:
        assert generate_diff(file1, file2) == new_result


def test_generate_diff_yaml():
    file1 = './tests/fixtures/file1.yaml'
    file2 = './tests/fixtures/file2.yaml'
    result = './tests/fixtures/result.yaml'

    with open(result, 'r') as new_result:
        assert generate_diff(file1, file2) ==  new_result