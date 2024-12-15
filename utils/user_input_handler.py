def parse_user_input(target_file, word, wordlist):
    
    if wordlist:
        is_wordlist = True
        wordlist_input = wordlist
    else:
        is_wordlist = False
        wordlist_input = word
        
    return is_wordlist, wordlist_input
    