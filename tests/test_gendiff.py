from gendiff.gendiff import generate_diff
from fixtures.fixture_gendiff import file1_json_flat, file2_json_flat, file1_yaml_flat, file2_yaml_flat, FLAT_RESULT


def test_generate_diff_flat():
    assert generate_diff(file1_json_flat, file2_json_flat) == FLAT_RESULT
    assert generate_diff(file1_yaml_flat, file2_yaml_flat) == FLAT_RESULT

