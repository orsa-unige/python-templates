#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess,json

cmd = ['Rscript', './2.R']

args = {'a':999.99,
        'b': [1,2,3],
        2: ['a','b'],
        'altro oggèèètto': {
            1:None,
            True:'ciccio',
            'vettore':[1,2,'stringa']
        },
        None:[1,"2",False]
}

args_in_json = json.dumps(args, indent=2, ensure_ascii=False)

#print(args_in_json)

subprocess.check_call(cmd + [args_in_json], shell=False)
