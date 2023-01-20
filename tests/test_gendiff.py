from gendiff.gendiff import generate_diff
from fixtures.fixture_gendiff import file1_json_flat, file2_json_flat, file1_yaml_flat, file2_yaml_flat


def test_generate_diff_flat():
    with open('tests/fixtures/tester.txt', 'r') as f:
        expected = f.read()

    assert generate_diff(file1_json_flat, file2_json_flat) == expected
    assert generate_diff(file1_yaml_flat, file2_yaml_flat) == expected

