# python-templates
Python templates to manage json input output with exception handling and script arguments

# Tests:

"ok" tests should output the same input

```bash
    echo '{"éèèèééèè":"°"}' | ./template.1.py                             # {"éèèèééèè":"°"}
    echo '{"éèèèééèè":"°"}' | ./template.1.py '{"aa":"bb"}'               # {"error": "please provide only one input"}
    echo '{"éèèèééèè":"°"}' | ./template.1.py -i input.json               # {"error": "please provide only one input"}
    echo '{"éèèèééèè":"°"}' | ./template.1.py '{"aa":"bb"}' -i input.json # {"error": "please provide only one input"}
    echo '{"éèèèééèè":"°"}' | ./template.1.py -o output.json              # In output.json: {"éèèèééèè":"°"}
    
    echo '{"éèèèééèè":"°"}' | ./template.1.py | ./template.1.py           # {"éèèèééèè":"°"}
    
    ./template.1.py '{"éèèèééèè":"°"}'                # {"éèèèééèè":"°"}
    ./template.1.py -i input.json                     # Content of input.json
    ./template.1.py '{"éèèèééèè":"°"}' -i input.json  # {"error": "please provide only one input"}
    ./template.1.py -i input.json -o output.json      # In output.json: Content of input.json
    
    ./template.1.py '{"éèèèééèè":"°"}' -o output.json # In output.json: {"éèèèééèè":"°"}
    ./template.1.py                                   # null
    ./template.1.py -o output.json                    # In output.json: null
   
    echo '{a:b}' | ./template.1.py                    # {"error": "not a valid json"}
   
```

