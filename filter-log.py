#!/usr/bin/python3

import json
import sys

def get_json(line):
    i = line.index('{')
    return line[i:]

def get_ns_name(doc):
    log_json = json.loads(doc)
    return log_json['kubernetes']['namespace_name']


def main(log_fname):
    with open(log_fname, 'r') as reader:
        log_content = reader.readlines()

    log_lines = map(lambda x: get_json(x), log_content)
    log_ns_names = list(map(lambda x: get_ns_name(x), log_lines))

    for ns_name in log_ns_names:
        print(ns_name)


if __name__ == '__main__':
    print('running ... ', sys.argv[1])
    main(sys.argv[1])
