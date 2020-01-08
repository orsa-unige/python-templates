#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json,sys,argparse,os


class wrap():
    
    def __init__(self):
        self.title = 'Template for python script managing JSON as input/output format. '
        self.descr = 'A JSON file can be [], {}, "string", 123, true, false, null. '
        self.data = 'null'
        self.parse()

        
    def parse(self):
        parser = argparse.ArgumentParser(description=self.title+self.descr)

        infile = ['-i','--input-file']
        kwinfile = {'type': argparse.FileType('r'),
                    'help': '''Input file name containing a valid JSON. 
                               Default and priority: standard input.'''}

        jstring = ['-j','--json']
        kwjstring = {'type': str,
                     'nargs': '?',
                     'help': '''Input file name containing a valid JSON. 
                                Default and priority: standard input.'''}

        outfile = ['-o','--output-file']
        kwoutfile = {'type': argparse.FileType('w'),
                     'default': sys.stdout,
                     'help': '''Output file name. It will contain valid JSON. 
                                Default: standard output.'''}

        pretty = ['-p','--pretty']
        kwpretty = {'action': 'store_true',
                    'help': 'If set, JSON output will be formatted in pretty print.'}
    
        group = parser.add_mutually_exclusive_group()
        
        group.add_argument(*infile, **kwinfile)
        group.add_argument(*jstring, **kwjstring)
        
        parser.add_argument(*outfile, **kwoutfile)
        parser.add_argument(*pretty, **kwpretty)
        
        self.args = parser.parse_args()    

        
    def input(self,*inp):
        if inp: self.data=inp[0] 

        if not sys.stdin.isatty(): # pipe
            self.data=sys.stdin.read()
        else:  # no pipe
            if len(sys.argv) < 1 or (self.args.input_file or self.args.json) != None :
                self.data = self.args.json or self.args.input_file.read()

        try:
            self.data = json.loads(self.data)
        except:
            self.data = {'script_name': (sys.argv[0]),
                         'error': 'Input is not a valid JSON.',
                         'data': self.data}
            self.output()
            sys.exit(0)

        return self.data

    
    def output(self,*inp):
        if inp: self.data=inp[0] 
        
        indent = 2 if self.args.pretty else None    
        out = json.dumps(self.data, indent=indent, ensure_ascii=False)
        self.args.output_file.write(out+os.linesep)

        return out

    
''' test if running as script '''
def main():
    ors = wrap()
    i = ors.input()
    ors.output(i)

    
if __name__ == "__main__":

    import sys
    main()
