#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import template as t

def main(*args):

    inp=t.input()

    if isinstance(inp,dict) :
        try:
            out={'area' : inp['x'] * inp['y'] }
        except:
            out={'error' : "missing x and/or y value"}

    elif isinstance(inp,list) :
        out=[]
        for o in inp :
            if (o['x']  and o['y']) is not None :
                out.append({'area' : o['x'] * o['y'] })
    else :
        out={
            'error' : "Need either {x,y} or [{x,y},...,{x,y}]",
            'data:' : inp}
        
    return(t.output(out))
    
if __name__ == "__main__": #i.e. run directly
    import sys
    try:
        main(sys.argv[1:])
    except IOError:
        handle_error()
