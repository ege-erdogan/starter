from argparse import ArgumentParser
import sys


def parse_args(args=sys.argv[1:]):
    parser = ArgumentParser()

    args = parser.parse_args(args)
    return args
