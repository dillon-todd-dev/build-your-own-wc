import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--count', action='store_true', help='count the number of bytes in the file')
parser.add_argument('file_path')
args = parser.parse_args()

if args.count:
    file_size = os.stat(args.file_path)
    print(file_size.st_size, args.file_path)
