# Tiddlywiki Launcher

A small Python wrapper script for installing [TiddlyWiki](https://tiddlywiki.com/) in a system-wide way so that each user on the system can launch their own TiddlyWiki.

## Features and limitations

* Respects the `$BROWSER` environment variable.
* Uses `/usr/bin/xdg-open` for opening TiddlyWiki in a browser, if `$BROWSER` is not set.
* Requires [`empty.html`](http://www.tiddlywiki.com/empty.html) to be present in `/usr/share/tiddlywiki/empty.html`.
* Copies `empty.html` into `$HOME/.tiddlywiki` upon launch, if Tiddlywiki does not already exist there.

## tiddlywiki.py

This is the entire script, without comments:

```python
from sys import argv
from os.path import join, exists
from os import mkdir, system, environ


def main():
    arguments = argv[1:]
    if arguments:
        where = arguments[0]
    else:
        where = join(environ['HOME'], '.tiddlywiki')
    goal = join(where, 'index.html')
    if not exists(where):
        mkdir(where)
        system('cp /usr/share/tiddlywiki/empty.html %s' % (goal))
    if ('BROWSER' in environ) and environ['BROWSER']:
        system(environ['BROWSER'] + " " + goal)
    else:
        system("/usr/bin/xdg-open " + goal)


if __name__ == "__main__":
    main()
```

## General information

* License: BSD-3
