"""Dump all strings from a given input file which match the encoding of the given tbl file."""

import sys

# tbl is a file format for mapping variable-length codes to stuff.
# It is used for romhacking and hex editing

class Tbl:
    def __init__(self, tbl_path):
        self.tbl_path = tbl_path
        self.mappings = {}
        with open(tbl_path) as f:
            for line in f.readlines():
                # whoops, kept trying to "lsplit"
                code, meaning = line.split('=', 1)    # gotta watch out for "3E=="
                print code, meaning
                print repr(meaning)
                print repr(bytearray.fromhex(code))
                self.mappings[code] = meaning


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Usage: python tabledump.py input.tbl")
    tblpath = sys.argv[1]
    table = Tbl(tblpath)
