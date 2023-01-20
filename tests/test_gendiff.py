from gendiff.gendiff import generate_diff
from fixtures.fixture_gendiff import file1_json_flat, file2_json_flat, file1_yaml_flat, file2_yaml_flat, FLAT_RESULT


def test_generate_diff_flat():
    f = open('tests/fixtures/tester.txt', 'r')

    assert generate_diff(file1_json_flat, file2_json_flat) == f.read()
    assert generate_diff(file1_yaml_flat, file2_yaml_flat) == f.read()

