#import necessary files
from cracker.zip_cracker import crack_zip
from utils.command_line_args import parse_arg
from utils.user_input_handler import parse_user_input
from utils.output_handler import write_output


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
    
    #Wordlist
    custom_wordlists = {
        'custom_wordlist' : args.custom_wordlist,
        'charset' : args.charset,
        'min_length' : args.min_length,
        'max_length' : args.max_length,
        'first_char_rule' : args.first_char_rule,
        'no_repeat' : args.no_repeat,
        'exclude_chars' : args.exclude_chars,
    }

    wordlist_input =  parse_user_input(file, word, wordlist, custom_wordlists)
    
    pwd = crack_zip(file, wordlist_input, verbose, threads)
    
    write_output(file, pwd, output, verbose)
    
if __name__ == "__main__":
    main()