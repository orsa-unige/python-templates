#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import template as t
import calculate_area as calc # importing my module!!! 
import numpy as np

'''Calculates the sqrt of an area given an object containing {area:number} or a list of
objects [{area:number},...,{area:number}]'''
def sqrt(args) :
    
    inp=calc.area(args)

    if isinstance(inp,dict) :
        try:
            out={'sqrt of area' : np.sqrt(inp['area']) }
        except:
            out={'error' : 'missing x,y values'}

    elif isinstance(inp,list) :
        out=[]
        for i in inp :
            out.append({'sqrt of area' : np.sqrt(i['area']) })
    else :
        out={
            'error' : 'Need either {area:...} or [{area},...,{area}]',
            'data:' : inp
        }

    return out

def main():
    args=t.parser()
    o=sqrt(args)        
    t.output(args,o)
    
if __name__ == "__main__": # i.e. run directly
    main()
