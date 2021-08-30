#!/usr/bin/env python3
import os
import sys

def message(content):
    for tty in os.popen("ps ua | grep -P '^'\"$USER\"'.*?((sh)|(zsh)|(bash))$' |  awk '{ print $7 }'").readlines():
        os.system("echo '{}' > /dev/{}".format(content, tty))

if __name__ == '__main__':
    message(" ".join(sys.argv[1:]))
