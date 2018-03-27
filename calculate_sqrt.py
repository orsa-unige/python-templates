#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import template as t
import calculate_area as i
import numpy as np
import json

def main():
    
    inp=json.loads(i.main())

    out={'sqrt of area' : np.sqrt(inp['area']) }

    return(t.output(out))
    
if __name__ == "__main__":
    main()
