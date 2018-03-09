#!/usr/bin/env python3

import json,sys,argparse

parser = argparse.ArgumentParser(description='Template for python script managing JSON as input/output format')

group = parser.add_mutually_exclusive_group()
group.add_argument('--input-file', '-i', type=argparse.FileType('r'), default=sys.stdin,
                   help='Input file name containing a valid JSON.')
group.add_argument('json', nargs='?', type=str,
                   help='Input string containing a valid JSON.')
parser.add_argument('--output-file', '-o', type=argparse.FileType('w'), default=sys.stdout,
                    help='Output file name.')

args = parser.parse_args()

# if not sys.stdin.isatty():
#     data = sys.stdin.read()

data = args.json or args.input_file.read()

datain = json.loads(data)

dataout = json.dumps(datain, indent=2)
args.output_file.write(dataout+'\n')
