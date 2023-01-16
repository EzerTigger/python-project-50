from gendiff.gendiff import generate_diff
from fixtures.fixture_gendiff import RESULT


file1 = 'gendiff/files/file1.json'
file2 = 'gendiff/files/file2.json'


def test_generate_diff():
    assert generate_diff(file1, file2) == RESULT

