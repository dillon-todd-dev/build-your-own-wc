import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--count', action='store_true', help='count the number of bytes in the file')
parser.add_argument('-l', '--length', action='store_true', help='count the number of lines in the file')
parser.add_argument('-w', '--words', action='store_true', help='count the number of words in the file')
parser.add_argument('file_path')
args = parser.parse_args()

if args.count:
    file_size = os.stat(args.file_path)
    print(file_size.st_size, args.file_path)

if args.length:
    with open(args.file_path) as fp:
        num_lines = len(fp.readlines())
        print(num_lines, args.file_path)

if args.words:
    with open(args.file_path) as fp:
        data = fp.read()
        lines = data.split()
        num_words = len(lines)
        print(num_words, args.file_path)
