#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import template as t


'''Calculates an area given an object containing {x:number,y:number} or a list of
objects [{x,y},...,{x,y}]'''
def area(args) :
    inp=t.input(args)

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
    args=t.parser()
    o=area(args)    
    t.output(args,o)


    
if __name__ == "__main__": #i.e. run directly
    main()
