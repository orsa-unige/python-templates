#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from template import wrap
import calculate_area as calc # importing my module!!!

'''Calculates the square of an area given an object containing {x:number,y:number}
or a list of objects [{x,y},...,{x,y}].
'''
def sqrt(inp):

    inp=calc.area(inp) # it executes x*y and stores the result in "area"

    if isinstance(inp,dict) : # is it a python dict (~json object) type?
        try:
            out={'sqrt of area' : inp['area']**0.5 }
        except:
            out={'error' : 'missing x,y values'}

    elif isinstance(inp,list) : # is it a python list (~json array) type?
        out=[]
        for i in inp :
            if (i['area']) is not None :
                out.append({'sqrt of area' : i['area']**0.5 })
    else :
        out={
            'error' : 'Need either {area:...} or [{area},...,{area}]',
            'data:' : inp
        }

    return out

def main():

    o = wrap()

    args=o.input()
    s=sqrt(args)
    o.output(s)

if __name__ == "__main__": #i.e. run directly
    main()
