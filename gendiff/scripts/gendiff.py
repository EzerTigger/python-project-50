#!/usr/bin/env python3


from gendiff.gendiff import parse, generate_diff

args = parse()


def main():
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
