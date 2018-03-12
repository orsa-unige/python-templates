#!/usr/bin/env python3

import json,sys,argparse

def main():
    
    parser = argparse.ArgumentParser(description='Template for python script managing JSON as input/output format. \
                                                  A JSON file can be [], {}, "string", 123, true, false, null.')

    infile=['-i','--input-file']
    kwinfile={'type':argparse.FileType('r'), 'help':'Input file name containing a valid JSON. Default and priority: standard input.'}

    jstring=['-j','--json']
    kwjstring={'type':str,  'nargs':'?', 'help':'Input file name containing a valid JSON. Default and priority: standard input.'}

    outfile=['-o','--output-file']
    kwoutfile={'type':argparse.FileType('w'), 'help':'Output file name. Default: standard output.', 'default':sys.stdout}

    pretty=['-p','--pretty']
    kwpretty={'action':'store_true', 'help':'If set, JSON output  will be formatted in pretty print.'}
    
    group = parser.add_mutually_exclusive_group()

    group.add_argument(*infile, **kwinfile)
    group.add_argument(*jstring, **kwjstring)
    parser.add_argument(*outfile, **kwoutfile)
    parser.add_argument(*pretty, **kwpretty)
    
    args = parser.parse_args()

    if not sys.stdin.isatty(): # pipe
        data=sys.stdin.read()
    else:  # no pipe
        if not len(sys.argv) > 1 or (args.input_file == None and args.json == None) : # no arguments or no input
            data='null'
        else :
            data = args.json or args.input_file.read()

    try:
        datain = json.loads(data)
    except:
        datain = {'script_name':(sys.argv[0]), 'error': 'Input is not a valid JSON.'}
        
    is_pretty = 2 if args.pretty else None
    
    dataout = json.dumps(datain, indent=is_pretty, ensure_ascii=False)
    args.output_file.write(dataout+'\n')
    
if __name__ == "__main__":
    main()