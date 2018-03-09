#!/usr/bin/env python3

import json,sys,argparse

parser = argparse.ArgumentParser(description='Template for python script managing JSON as input/output format')

group = parser.add_mutually_exclusive_group()
group.add_argument('--input-file', '-i',  type=str, help='Input file name containing a valid JSON.', default=sys.stdin)
group.add_argument('json',    nargs='?',  type=str, help='Input string containing a valid JSON.' , default=sys.stdin)
parser.add_argument('--output-file', '-o',type=str, help='Output file name.')

args = parser.parse_args()

if not sys.stdin.isatty():
    data = sys.stdin.read()
else:
#    args = parser.parse_args()
    if args.input_file :
        data=open(args.input_file).read()
    elif args.json :
        data=args.json


datain=json.loads(data)
        
dataout=json.dumps(datain, indent=2)

if args.output_file :
        output_file=open(args.output_file, 'w')
        output_file.write(dataout+'\n')
        output_file.close()
else:
    print (dataout)
