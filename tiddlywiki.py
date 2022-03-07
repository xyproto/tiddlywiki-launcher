#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# tiddlywiki launcher
#
# Version:  0.3.0
# Author:   Alexander F. Rødseth <xyproto@archlinux.org>
# Modified: 2021-03-07
# License:  BSD-3
#

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
