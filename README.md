# Tiddlywiki Launcher

A small Python wrapper script for installing [TiddlyWiki](https://tiddlywiki.com/) in a system-wide way so that each user on the system can launch their own TiddlyWiki.

## Features and limitations

* Respects the `$BROWSER` environment variable.
* Uses `/usr/bin/xdg-open` for opening TiddlyWiki in a browser, if `$BROWSER` is not set.
* Requires [`empty.html`](http://www.tiddlywiki.com/empty.html) to be present in `/usr/share/tiddlywiki/empty.html`.
* Copies `empty.html` into `$HOME/.tiddlywiki` upon launch, if Tiddlywiki does not already exist there.

## General information

* MIT licensed
