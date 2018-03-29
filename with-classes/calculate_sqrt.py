#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from template import orsa
import calculate_area as calc # importing my module!!! 

o = orsa()

'''Calculates the sqrt of an area given an object containing
{area:number} or a list of objects [{area:number},...,{area:number}]
'''
def sqrt():
    
    inp=calc.area()

    if isinstance(inp,dict) :
        try:
            out={'sqrt of area' : inp['area']**0.5 }
        except:
            out={'error' : 'missing x,y values'}

    elif isinstance(inp,list) :
        out=[]
        for i in inp :
            out.append({'sqrt of area' : i['area']**0.5 })
    else :
        out={
            'error' : 'Need either {area:...} or [{area},...,{area}]',
            'data:' : inp
        }

    return out

    
def main():
    s=sqrt()
    o.output(s)
    
if __name__ == "__main__":
    main()
