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

data = []
for i, name in enumerate(["last.txt", "first-f.txt", "first-m.txt"]):
    with open(name, "r") as f:
        data.append(f.readlines())


def gen_names(x, formatted=True):
    names = []
    for i in range(x):
        g = random.randint(0, 1) + 1
        last_name = data[0][random.randint(0, 93)].replace('\n', '')

        first_name = data[g][random.randint(0, 49)].replace('\n', '')
        if g == 1:
            last_name = re.sub('ski$', 'ska', last_name)
            last_name = re.sub('cki$', "cka", last_name)
            last_name = re.sub('dzki$', "dzka", last_name)
        if formatted:
            name = '{} {}'.format(first_name, last_name)
        else:
            name = [first_name, last_name]
        names.append(name)
    return names


if __name__ == "__main__":
    print(gen_names(n))
