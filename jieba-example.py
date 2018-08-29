#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import jieba

def main(args):
    with open(args[0]) as f:
        full_text = f.read()
        words = jieba.cut(full_text, cut_all=True)

        count = {}
        for word in words:
            if word not in count:
                count[word] = 0
            count[word] += 1

        for key, value in sorted(count.iteritems(), key=lambda (k,v): (v,k)):
            print "%s: %s" % (key, value)

if __name__ == '__main__':
    main(sys.argv[1:])
