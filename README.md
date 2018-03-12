# python-templates
Python templates to manage json input output with exception handling and script arguments

# Tests:

"ok" tests should output the same input

```bash
    echo '{"éèèèééèè":"°"}' | ./template.1.py                                  # ok
    echo '{"éèèèééèè":"°"}' | ./template.1.py '{"éèèèééèè":"°"}'               # not ok or decide priority and ignore others
    echo '{"éèèèééèè":"°"}' | ./template.1.py -i input.json                    # not ok or decide priority and ignore others
    echo '{"éèèèééèè":"°"}' | ./template.1.py '{"éèèèééèè":"°"}' -i input.json # not ok or decide priority and ignore others
    echo '{"éèèèééèè":"°"}' | ./template.1.py -o output.json                   # ok
    
    echo '{"éèèèééèè":"°"}' | ./template.1.py | ./template.1.py                # ok
    
    ./template.1.py '{"éèèèééèè":"°"}'                # ok
    ./template.1.py -i input.json                     # ok
    ./template.1.py '{"éèèèééèè":"°"}' -i input.json  # not ok or decide priority and ignore others
    
    ./template.1.py '{"éèèèééèè":"°"}' -o output.json # ok
    ./template.1.py -o output.json                    # not ok or decide if empty json (array? object? null? error json?)
    
    ./template.1.py                                   # not ok or decide if empty json (array? object? null? error json?)
```

