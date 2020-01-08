#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from template import wrap

'''Calculates an area given an object containing {x:number,y:number}
or a list of objects [{x,y},...,{x,y}]
'''
def area(inp):

    if isinstance(inp,dict) : # is it a python dict (~json object) type?
        try:
            out={'area' : inp['x'] * inp['y'] }
        except:
            out={'error' : 'missing x,y values'}

    elif isinstance(inp,list) : # is it a python list (~json array) type?
        out=[]
        for i in inp :
            if (i['x'] and i['y']) is not None :
                out.append({'area' : i['x'] * i['y'] })
    else :
        out={
            'error' : "Need either {x,y} or [{x,y},...,{x,y}]",
            'data:' : inp
        }

    return out

def main(): 

    o = wrap()

    args=o.input()    
    a=area(args)
    o.output(a)
    
if __name__ == "__main__": #i.e. run directly
    main()
