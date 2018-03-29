#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from template import orsa

class show_script_name(orsa):

    def __init__(self):
        self.title = 'ciccio. '
        self.descr = 'pippo. '
        self.data = 'null'
        self.parse()
        

''' test if running as script '''
def main():
     s = show_script_name()
     i = s.input()
     s.output(i)

    
if __name__ == "__main__":

    import sys
    main()
