#!/usr/bin/env python
#
# rare.py
# A script to read in a text file, enumerate characters,
# and output character statistics starting with least-used

import sys,argparse,collections

# Function Defs
def rare():
    wordlist = args.file.read()        #read in file as list
    res = collections.Counter(wordlist).most_common()[::-1]
    print("Count of characters, starting with those of least occurrence \n")
    print(str(res))

# CLI arguments & arg parser
ex = '''example:
python rare.py file.txt'''
parser = argparse.ArgumentParser(prog='rare',
                                description='Outputs character statistics of a text file.',
                                epilog=ex,
                                formatter_class=argparse.RawDescriptionHelpFormatter,
                                )
parser.add_argument('file', type=argparse.FileType('r'))
parser.set_defaults(func=rare)
args = parser.parse_args()

def main():
    args.func()

if __name__ == "__main__":
    sys.exit( main() )
