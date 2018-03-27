#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import template as t

def main():

    inp=t.input() # {"x":8, "y":2}

    out={'area' : inp['x'] * inp['y'] }

    return(t.output(out))
    
if __name__ == "__main__":
    main()
