from gendiff.gendiff import generate_diff
from fixtures.fixture_gendiff import RESULT, file1_json, file2_json, file1_yaml, file2_yaml


def test_generate_diff_json():
    assert generate_diff(file1_json, file2_json) == RESULT


def test_generate_diff_yaml():
    assert generate_diff(file1_yaml, file2_yaml) == RESULT

