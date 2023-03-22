from gendiff.gendiff import generate_diff
from fixtures.fixture_gendiff import file1_json_flat, file2_json_flat, file1_yaml_flat, file2_yaml_flat
from fixtures.fixture_gendiff import file1_json_nested, file2_json_nested, file1_yaml_nested, file2_yaml_nested


def test_generate_diff_flat():
    with open('tests/fixtures/tester_flat.txt', 'r') as f:
        expected = f.read()

    assert generate_diff(file1_json_flat, file2_json_flat) == expected
    assert generate_diff(file1_yaml_flat, file2_yaml_flat) == expected


def test_generate_diff_nested():
    with open('tests/fixtures/tester_nested.txt', 'r') as f:
        expected = f.read()

    assert generate_diff(file1_json_nested, file2_json_nested) == expected
    assert generate_diff(file1_yaml_nested, file2_yaml_nested) == expected


def test_format_plain():
    with open('tests/fixtures/tester_plain.txt', 'r') as f:
        expected = f.read()

    assert generate_diff(file1_json_nested, file2_json_nested,
                         'plain') == expected
    assert generate_diff(file1_yaml_nested, file2_yaml_nested,
                         'plain') == expected


def test_format_json():
    with open('tests/fixtures/tester_json.json', 'r') as f:
        expected = f.read()
    assert generate_diff(file1_json_nested, file2_json_nested, 'json') == expected
    assert generate_diff(file1_yaml_nested, file2_yaml_nested, 'json') == expected
