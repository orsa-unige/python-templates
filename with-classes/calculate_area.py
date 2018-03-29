#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from template import orsa

o = orsa()

'''Calculates an area given an object containing {x:number,y:number}
or a list of objects [{x,y},...,{x,y}]

'''
def area():
    inp=o.input()

    if isinstance(inp,dict) :
        try:
            out={'area' : inp['x'] * inp['y'] }
        except:
            out={'error' : 'missing x,y values'}

    elif isinstance(inp,list) :
        out=[]
        for i in inp :
            if (i['x']  and i['y']) is not None :
                out.append({'area' : i['x'] * i['y'] })
    else :
        out={
            'error' : "Need either {x,y} or [{x,y},...,{x,y}]",
            'data:' : inp
        }

    return out


def main(): 

    a=area()
    o.output(a)

    
if __name__ == "__main__":
    main()
