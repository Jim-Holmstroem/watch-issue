import sys

from watchfiles import run_process

run_process(sys.argv[1], target=print, args=("changed",), debug=True)
