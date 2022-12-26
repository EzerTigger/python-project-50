#!/usr/bin/env python3

import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first file', type=str)
    parser.add_argument('second file', type=str)
    parser.parse_args()


if __name__ == '__main__':
    main()