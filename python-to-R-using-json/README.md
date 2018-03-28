# Passing an object from python to R

Sometimes we need to pass from python to R a long series of objects such as several arrays, or variable values. 
We can use `json` to do it.

```bash
sudo apt-get install r-base
```

## script-receiving-json.R

The R code needs a package to be able to receive json:

```bash
sudo R
> install.packages("jsonlite", repos="http://cran.r-project.org")
> quit()
```

Then the script **receiving** the `json` can be called like that:

```R
#!/usr/bin/Rscript

library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)

#nums = as.numeric(args)
nums = fromJSON(args)

b=nums['b']

print(b)
```

## script-sending-json.py

The python code **sending** the `json` is something like that, where the `utf-8` line helps to treat special characters:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess,json

cmd = ['Rscript', './script-receiving-json.R']

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
```

## Calling the script


```bash
 ./script-sending-json.py
 Loading required package: methods
 $b
 [1] 1 2 3
 ```
 
 
