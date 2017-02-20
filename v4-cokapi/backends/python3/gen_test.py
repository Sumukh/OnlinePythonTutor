import json
import shlex

data = {
    'user-script': """x = 1
print("ok")
print(bar(x) == None)
""",
    'extra-files': {
        'helper.py': """from collections import defaultdict
import os # Test the ability to import all libraries

values = [1, 2, 3]""",
        'foo.py': """from helper import values
def bar(x):
    if x == 0:
        print(values)
        return values
    return bar(x-1)"""

    },
    'setup': 'from foo import bar'
}

if __name__ == "__main__":
    print(shlex.quote(json.dumps(data)))