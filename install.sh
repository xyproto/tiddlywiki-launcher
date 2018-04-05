#!/bin/sh
pkgdir="$1"
install -Dm755 "tiddlywiki.py" "$pkgdir/usr/bin/tiddlywiki"
