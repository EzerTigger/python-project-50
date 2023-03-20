#!/usr/bin/env python3

from gendiff.gendiff import generate_diff
from gendiff.argparse import parse
from gendiff.formatters.plain import plain


args = parse()


def main():
    if args.format == 'plain':
        print(generate_diff(args.first_file, args.second_file, plain))
    else:
        print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
