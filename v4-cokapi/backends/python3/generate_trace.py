# Generates a JSON trace that is compatible with the js/pytutor.js frontend
# With customization to support extra modules. Runs within the container

import os, os.path
import sys, pg_logger, json
from optparse import OptionParser

# To make regression tests work consistently across platforms,
# standardize display of floats to 3 significant figures
#
# Trick from:
# http://stackoverflow.com/questions/1447287/format-floats-with-standard-json-module
json.encoder.FLOAT_REPR = lambda f: ('%.3f' % f)

def json_finalizer(input_code, output_trace):
    ret = dict(code=input_code, trace=output_trace)
    # sort_keys=True leads to printing in DETERMINISTIC order, but might
    # screw up some old tests ... however, there is STILL non-determinism
    # in Python 3.3 tests, ugh!
    json_output = json.dumps(ret, indent=INDENT_LEVEL)
    return json_output

parser = OptionParser(usage="Generate JSON trace for pytutor")
parser.add_option('--json', default='{}', action='store',
        help='JSON string with user script and modules.', dest='user_code')
parser.add_option('-c', '--cumulative', default=False, action='store_true',
        help='output cumulative trace.')
parser.add_option('-p', '--heapPrimitives', default=False, action='store_true',
        help='render primitives as heap objects.')
parser.add_option('-o', '--compact', default=False, action='store_true',
        help='output compact trace.')
parser.add_option('-i', '--input', default=False, action='store',
        help='JSON list of strings for simulated raw_input.', dest='raw_input_lst_json')

(options, args) = parser.parse_args()
INDENT_LEVEL = None if options.compact else 2

def run_logger(source, setup, modules=None):
    modules = modules or {}
    # Add current directory to path to make sure that imports work consistently
    sys.path.append(os.getcwd() + '/')
    return pg_logger.exec_script_str_local(source,
                                           options.raw_input_lst_json,
                                           options.cumulative,
                                           options.heapPrimitives,
                                           json_finalizer,
                                           separate_stdout_by_module=True,
                                           disable_security_checks=True,
                                           custom_modules={'pg_setup': setup},
                                           extra_modules=modules)

def trace_json(json_str):
    forbidden_files = ('pg_logger.py', 'pg_encoder.py', 'generate_trace.py')
    data = json.loads(json_str)
    if 'user-script' not in data:
        raise ValueError("user-script not in data")
    source, setup = data['user-script'], data.get('setup', '')
    extra_files = data.get('extra-files', {})
    modules = {}

    for filename, contents in data['extra-files'].items():
        if filename not in forbidden_files:
            directory = os.path.dirname(filename)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
            with open(filename, 'w') as f:
                f.write(contents)
                f.flush()

            module_name = filename.rstrip(".py").replace('/', '.')
            modules[module_name] = contents

    return run_logger(source, setup, modules)

if __name__ == "__main__":
    print(trace_json(options.user_code))
