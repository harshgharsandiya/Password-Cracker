import itertools
import string

from utils.colors import print_error

def parse_charset(charset_string):
    """
    return appropriate character set
    """
    charsets = {
        "a-z": string.ascii_lowercase,
        "A-Z": string.ascii_uppercase,
        "0-9": string.digits,
        "all": string.ascii_letters + string.digits
    }
    
    charset = []
    for i in charset_string.split(','):
        if i in charsets:
            charset.append(charsets[i])
        else:
            #user custom sets (e.g., "abc123")
            charset.append(i)
            
    return ''.join(charset)

def generate_custom_wordlist(charset, min_length, max_length, first_char_rule=None, no_repeats=False, exclude_chars=None):
    """
    Based on specified rules generate wordlists
    """
    wordlist = []
    
    if not isinstance(min_length, int) or not isinstance(max_length, int) or min_length > max_length:
        print_error("[-] Invalid min_length or max_length for custom wordlist.")
        return None
    
    first_char_set = charset if first_char_rule is None else first_char_rule
    
    #Generate passwords
    for length in range(min_length, max_length+1):
        
        if length == 1:
            wordlist.extend([''.join(p) for p in itertools.product(charset, repeat=length)])
        else:
            for first_char in first_char_set:
                for rest in itertools.product(charset, repeat=length - 1):
                    password = first_char + ''.join(rest)
                    
                    #additional rule
                    if no_repeats and len(set(password)) != len(password):
                        continue
                    if exclude_chars:
                        if any(c in password for c in exclude_chars):
                            continue
                    
                    wordlist.append(password)
                    
        
    return wordlist

#Driver Code
if __name__ == "__main__":
    c = parse_charset("a-z,A-Z,34")
    w = generate_custom_wordlist(c, 1, 2, "az", True, ['1','z'])
    with open("wordlist.txt", "w") as file:
        for word in w:
            file.write(word + "\n")
    print(len(w))
            