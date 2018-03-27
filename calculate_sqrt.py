#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import template as t
import calculate_area as i
import numpy as np
import json

def main(*args):

    inp=json.loads(i.main())

    if isinstance(inp,dict) :
        try:
            out={'sqrt of area' : np.sqrt(inp['area']) }
        except:
            out={'error' : "missing area value"}

    elif isinstance(inp,list) :
        out=[]
        for o in inp :
            out.append({'sqrt of area' : np.sqrt(o['area']) })
    else :
        out={
            'error' : "Need either {area:...} or [{area},...,{area}]",
            'data:' : inp}

        
    return(t.output(out))

if __name__ == "__main__": # i.e. run directly
    import sys
    try:
        main(sys.argv[1:])
    except IOError:
        handle_error()
