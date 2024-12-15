import os

def check_file_and_wordlist(file_path, wordlist_path):
     
    if os.path.isfile(wordlist_path):
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
            passwords = wordlist.readlines()
    else:
        passwords = [wordlist.strip()]
    
    if not os.path.exists(file_path):
        print(f"[-] {file_path} does not exist")
        return None, None

    return file_path, wordlist_path
