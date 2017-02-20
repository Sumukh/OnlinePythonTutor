#!/bin/sh

## Execute tests (see gen_test.py for how to generate this argument)
python generate_trace.py --json '{"extra-files": {"helper.py": "from collections import defaultdict\nimport os # Test the ability to import all libraries\n\nvalues = [1, 2, 3]", "foo.py": "from helper import values\ndef bar(x):\n    if x == 0:\n        print(values)\n        return values\n    return bar(x-1)"}, "setup": "from foo import *", "user-script": "x = 1\nprint(\"ok\")\nprint(bar(x) == None)\n"}'

