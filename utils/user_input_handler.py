from utils.colors import print_error
from wordlist_generator.wordlist_generator import generate_custom_wordlist, parse_charset

import os

def parse_user_input(target_file, word, wordlist, custom_wordlists):
    
    if not os.path.isfile(target_file):
        print_error(f"[-] Target file '{target_file}' not exist")
        return None
    
    if wordlist:
        if not os.path.isfile(wordlist):
            print_error(f"[-] Wordlist file '{wordlist}' not exist")
            return None
        try:
            with open(wordlist, 'r', encoding='utf-8', errors='ignore') as file:
                passwords = file.readlines()
        except Exception as e:
            print_error(f"[-] Error reading wordlist file: {e}")
            return None
        
    elif custom_wordlists['custom_wordlist']:
        
        charset = parse_charset(custom_wordlists['charset'])
        min_length = custom_wordlists['min_length']
        max_length = custom_wordlists['max_length']
        first_char_rule = custom_wordlists['first_char_rule']
        no_repeat = custom_wordlists['no_repeat']
        exclude_chars = custom_wordlists['exclude_chars']
        
        passwords = generate_custom_wordlist(charset, min_length, max_length, first_char_rule, no_repeat, exclude_chars)
        
    
    else:
        passwords = [word.strip()]
    return passwords
    