import sys

from watchfiles import watch

for changes in watch(sys.argv[1], debug=True):
    print(changes)
