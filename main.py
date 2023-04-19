from watchfiles import watch

for changes in watch('/watch-this', debug=True):
    print(changes)
