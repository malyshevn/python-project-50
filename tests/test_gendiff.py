from gendiff.generate_diff import generate_difference
import os


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    fixtures_dir = os.path.join(current_dir, 'fixtures')
    return os.path.join(fixtures_dir, file_name)


def test_nested_stylish():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    result = get_fixture_path('result.json')

    generated_diff = generate_difference(file1, file2, format_name="stylish")
    with open(result, 'r') as new_result_file:
        expected_result = new_result_file.read()

    assert generated_diff == expected_result


def test_nested_plain():
    file1 = get_fixture_path('tree1.json')
    file2 = get_fixture_path('tree2.json')
    result = get_fixture_path('flat_result')

    generated_diff = generate_difference(file1, file2, format_name="plain")
    with open(result, 'r') as new_result_file:
        expected_result = new_result_file.read()

    assert generated_diff == expected_result


def test_nested_json():
    file1 = get_fixture_path('tree1.json')
    file2 = get_fixture_path('tree2.json')
    result = get_fixture_path('json_result.json')

    generated_diff = generate_difference(file1, file2, format_name="json")
    with open(result, 'r') as new_result_file:
        expected_result = new_result_file.read()

    assert generated_diff == expected_result
