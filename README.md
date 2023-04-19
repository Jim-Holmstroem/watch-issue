# watch-issue

# NOTE _not_ an issue
The culprit was a missing flush for prints.

## run in docker
### forced polling
```bash
WATCH_THIS=watch-this-folder WATCHFILES_FORCE_POLLING=1 docker-compose up --build
```
### inotify
```bash
WATCH_THIS=watch-this-folder docker-compose up --build
```

## run outside of docker
```bash
pip install -r requirements.txt

python -m main.py watch-this

python -m async-main.py watch-this
```
