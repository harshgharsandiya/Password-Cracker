#import necessary files
from cracker.zip_cracker import crack_zip
from utils.command_line_args import parse_arg

#import necessary library
import sys
import argparse
import os

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
    output = args.output
    
    if wordlist:
        is_wordlist = True
        wordlist_input = wordlist
    else:
        is_wordlist = False
        wordlist_input = word
        
    pwd = crack_zip(file, wordlist_input, verbose, is_wordlist, threads)

    

if __name__ == "__main__":
    main()