#! /Users/trezendes/.pyenv/versions/3.13.0/envs/FormFiller/bin/python

import argparse

if __name__ == '__main__':

    msg = 'This is the help message for %(prog)s'
    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument('-f', '--foo')
    parser.add_argument('-b', '--baz')
    parser.add_argument('bar')
    parser.parse_args()
    args = parser.parse_args()
    print(f'foo: {args.foo}\nbar: {args.bar}\nbaz: {args.baz}')
