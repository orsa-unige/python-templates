#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from template import orsa
import calculate_area as calc

o = orsa()

def run():

    c = calc.run()
    c['square'] = c['sum']**2
    return c

    
def main():
    r=run()
    o.output(r)
    
if __name__ == "__main__":
    main()
