#import necessary files
from cracker.zip_cracker import crack_zip
from utils.command_line_args import parse_arg
from utils.user_input_handler import parse_user_input
from utils.output_handler import write_output

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

    is_wordlist, wordlist_input =  parse_user_input(file, word, wordlist)
        
    pwd = crack_zip(file, wordlist_input, verbose, is_wordlist, threads)
    write_output(pwd, output, verbose)
    
if __name__ == "__main__":
    main()