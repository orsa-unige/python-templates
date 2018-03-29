#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from template import orsa

o = orsa()

def run():
    i = o.input()
    i['z'] = 3
    
    s = i['x'] + i['y']

    somma={'sum': s}
    
    return somma
    
def main(): 
    r=run()
    o.output(r)

if __name__ == "__main__":
    main()
