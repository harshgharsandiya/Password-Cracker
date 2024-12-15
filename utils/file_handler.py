from utils.colors import print_error
import os

#File handling
def validate_file(target_file, wordlist_input, is_wordlist=True):
    if not os.path.isfile(target_file):
        print_error(f"[-] Target file '{target_file} not exist")
        return None
    
    if is_wordlist:
        if not os.path.isfile(wordlist_input):
            print_error(f"[-] Wordlist file '{wordlist_input}' not exist")
            return None
        try:
            with open(wordlist_input, 'r', encoding='utf-8', errors='ignore') as wordlist:
                passwords = wordlist.readlines()
        except Exception as e:
            print_error(f"[-] Error reading wordlist file: {e}")
            return None
    else:
        passwords = [wordlist_input.strip()]
    return passwords
