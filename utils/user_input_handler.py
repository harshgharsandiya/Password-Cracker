from utils.colors import print_error
import os

def parse_user_input(target_file, word, wordlist):
    
    if not os.path.isfile(target_file):
        print_error(f"[-] Target file '{target_file} not exist")
        return None
    
    if wordlist:
        if not os.path.isfile(wordlist):
            print_error(f"[-] Wordlist file '{wordlist}' not exist")
            return None
        try:
            with open(wordlist, 'r', encoding='utf-8', errors='ignore') as wordlist:
                passwords = wordlist.readlines()
        except Exception as e:
            print_error(f"[-] Error reading wordlist file: {e}")
            return None
    else:
        passwords = [word.strip()]
    return passwords
    