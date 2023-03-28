import pytest

from gendiff.gendiff import generate_diff
from fixtures.fixture_gendiff import file1_json_flat, file2_json_flat, file1_yaml_flat, file2_yaml_flat
from fixtures.fixture_gendiff import file1_json_nested, file2_json_nested, file1_yaml_nested, file2_yaml_nested
from gendiff.argparse import parse

@pytest.mark.parametrize(
    ('file_1', 'file_2'),
    (
        (file1_json_flat, file2_json_flat),
        (file1_yaml_flat, file2_yaml_flat)
    )
)
def test_generate_diff_flat(file_1, file_2):
    with open('tests/fixtures/tester_flat.txt', 'r') as f:
        expected = f.read()

    assert generate_diff(file_1, file_2) == expected


@pytest.mark.parametrize(
    ('file_1', 'file_2'),
    (
        (file1_json_nested, file2_json_nested),
        (file1_yaml_nested, file2_yaml_nested)
    )
)
def test_generate_diff_nested(file_1, file_2):
    with open('tests/fixtures/tester_nested.txt', 'r') as f:
        expected = f.read()

    assert generate_diff(file_1, file_2) == expected


@pytest.mark.parametrize(
    ('file_1', 'file_2', 'formatter'),
    (
        (file1_json_nested, file2_json_nested, 'plain'),
        (file1_yaml_nested, file2_yaml_nested, 'plain')
    )
)
def test_format_plain(file_1, file_2, formatter):
    with open('tests/fixtures/tester_plain.txt', 'r') as f:
        expected = f.read()

    assert generate_diff(file_1, file_2, formatter) == expected


@pytest.mark.parametrize(
    ('file_1', 'file_2', 'formatter'),
    (
        (file1_json_nested, file2_json_nested, 'json'),
        (file1_yaml_nested, file2_yaml_nested, 'json'),
    )
)
def test_format_json(file_1, file_2, formatter):
    with open('tests/fixtures/tester_json.json', 'r') as f:
        expected = f.read()

    assert generate_diff(file_1, file_2, formatter) == expected


def test_argparse():
    args = parse(['file1', 'file2', '--format', 'plain'])
    assert args.first_file == 'file1'
    assert args.second_file == 'file2'
    assert args.format == 'plain'
