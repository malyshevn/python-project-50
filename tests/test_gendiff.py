from gendiff import generate_diff


def test_generate_diff():
    file1 = './tests/fixtures/file1.json'
    file2 = './tests/fixtures/file2.json'
    result = './tests/fixtures/result.json'

    generated_diff = generate_diff(file1, file2, format_name="stylish")
    with open(result, 'r') as new_result_file:
        expected_result = new_result_file.read()

    assert generated_diff == expected_result


def test_generate_diff_yaml():
    file1 = './tests/fixtures/file1.yml'
    file2 = './tests/fixtures/file2.yml'
    result = './tests/fixtures/result'

    generated_diff = generate_diff(file1, file2, format_name="stylish")
    with open(result, 'r') as new_result_file:
        expected_result = new_result_file.read()

    assert generated_diff == expected_result


def test_nested_plain():
    file1 = './tests/fixtures/tree1.json'
    file2 = './tests/fixtures/tree2.json'
    result = './tests/fixtures/flat_result'

    generated_diff = generate_diff(file1, file2, format_name="plain")
    with open(result, 'r') as new_result_file:
        expected_result = new_result_file.read()

    assert generated_diff == expected_result


def test_nested_json():
    file1 = './tests/fixtures/tree1.json'
    file2 = './tests/fixtures/tree2.json'
    result = './tests/fixtures/json_result.json'

    generated_diff = generate_diff(file1, file2, format_name="json")
    with open(result, 'r') as new_result_file:
        expected_result = new_result_file.read()

    assert generated_diff == expected_result
