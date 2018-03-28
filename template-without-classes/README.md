# Template without classes

This example contains three files: 
  - a template, 
  - a first  script importing the template,
  - a second script importing the template and the first script.

Thanks to the template, all have the same capabilities: they can manage input and output in different ways and they can used both as a module and as a command line script.

## template.py


The first one is `template.py`.
When imported by other files, can manage input, output and help so that all scripts behave the same way:

```bash  
usage: template.py [-h] [-i INPUT_FILE | -j [JSON]] [-o OUTPUT_FILE] [-p]

Template for python script managing JSON as input/output format. A JSON file
can be [], {}, "string", 123, true, false, null.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input-file INPUT_FILE
                        Input file name containing a valid JSON. Default and
                        priority: standard input.
  -j [JSON], --json [JSON]
                        Input file name containing a valid JSON. Default and
                        priority: standard input.
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        Output file name. Default: standard output.
  -p, --pretty          If set, JSON output will be formatted in pretty print.
```

## calculate_area.py

Template is imported by the second file. `calculate_area.py` takes an object (or a list of objects) containing x and y values, and it outputs an object containing the area. This occours calling the input from template in a function to receive the input from one of the template methods:

```python

import template as t

def area() :
    inp=t.input()
    ...
    return out
```

The output is called in the main function:


```python
def main() :
    o=area()
    t.output(o)
```

Here come test examples from command line and as a module:


```bash
./calculate_area.py
{"error": "Need either {x,y} or [{x,y},...,{x,y}]", "data:": null}


echo '{"x":2, "y":3}' | ./calculate_area.py
{"area": 6}

./calculate_area.py -j '{"x":2, "y":3}'
{"area": 6}

echo '[{"x":4, "y":1},{"x":4, "y":9},{"x":4, "y":25} ]' | ./calculate_area.py
[{"area": 4}, {"area": 36}, {"area": 100}]

echo '[{"x":4, "y":1},{"x":4, "y":9},{"x":4, "y":25} ]' | ./calculate_area.py -p
[
  {
    "area": 4
  },
  {
    "area": 36
  },
  {
    "area": 100
  }
]

echo '[{"x":1, "y":4},{"x":4, "y":9},{"x":4, "y":25} ]' | python3 -m calculate_area
[{"area": 4}, {"area": 36}, {"area": 100}]
```


## calculate_sqrt.py


The third script, `calculate_sqrt`, imports both `template` and `calculate_area`. It takes an object (or a list of objects) containing x and y values. Inside the script the area is calculated by `calculate area`, then  it calculates the square root and outputs it:

```python

import template as t 
import calculate_area as calc 

def sqrt() : 
   inp=calc.area()
   ...
   return out

```

The same way as above, the output is called in the main function:


```python
def main() :
    o=sqrt()
    t.output(o)
```

Here come test examples from command line and as a module:


```bash  
./calculate_sqrt.py
{"error": "missing x,y values"}

echo '{"x":2, "y":3}' | ./calculate_sqrt.py
{"sqrt of area": 2.449489742783178}

./calculate_sqrt.py -j '{"x":2, "y":3}'
{"sqrt of area": 2.449489742783178}

echo '[{"x":4, "y":1},{"x":4, "y":9},{"x":4, "y":25} ]' | ./calculate_sqrt.py
[{"sqrt of area": 2.0}, {"sqrt of area": 6.0}, {"sqrt of area": 10.0}]

echo '[{"x":4, "y":1},{"x":4, "y":9},{"x":4, "y":25} ]' | ./calculate_sqrt.py -p
[
  {
    "sqrt of area": 2.0
  },
  {
    "sqrt of area": 6.0
  },
  {
    "sqrt of area": 10.0
  }
]

echo '[{"x":1, "y":4},{"x":4, "y":9},{"x":4, "y":25} ]' | python3 -m calculate_sqrt
[{"sqrt of area": 2.0}, {"sqrt of area": 6.0}, {"sqrt of area": 10.0}]

```
 
