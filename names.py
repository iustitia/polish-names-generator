#!/usr/bin/env python

import random
import re
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('n', metavar='N', type=int, nargs='?', default=350)
args = parser.parse_args()

n = args.n

# based on:
# https://gist.github.com/jdudek/732279/e0d85c10acd8df3421e314699609ca283f4d8ac6

names = []
for i, name in enumerate(["last.txt", "first-f.txt", "first-m.txt"]):
    with open(name, "r") as f:
        names.append(f.readlines())

for i in range(n):
    g = random.randint(0, 1) + 1
    last_name = names[0][random.randint(0, 93)]

    first_name = names[g][random.randint(0, 49)]
    if g == 1:
        last_name = re.sub('ski$', 'ska', last_name)
        last_name = re.sub('cki$', "cka", last_name)
        last_name = re.sub('dzki$', "dzka", last_name)
    print(first_name, last_name)
