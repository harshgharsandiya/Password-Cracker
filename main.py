#import necessary files
from cracker.zip_cracker import crack_zip
from utils.command_line_args import parse_arg

#import necessary library
import sys
import argparse

def main():
    """Run Password Cracker here"""
    args = parse_arg()
    
    #Required
    file = args.file
    word = args.word
    wordlist = args.wordlist

    #Optional
    verbose = args.verbose
    threads = args.threads
    
    if file and word:
        pwd = crack_zip(file, word, verbose, 0, threads)
    elif file and wordlist:
        pwd = crack_zip(file, wordlist, verbose, 1, threads)
    else:
        sys.exit(0)
    

if __name__ == "__main__":
    main()