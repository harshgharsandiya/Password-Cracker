import argparse

def parse_arg():
    
    parser = argparse.ArgumentParser(description="Crack a password-protected ZIP file using a wordlist.")
    
    #Add arguments
    parser.add_argument("-f", "--file", type=str, required=True, help="Path to the Zip File")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-w", "--word", type=str, help="Single password", default=None)
    group.add_argument("-W", "--wordlist", type=str, help="Path to the Wordlist File", default=None)
    group.add_argument("-cw", "--custom-wordlist", action="store_true", help="Generate custom wordlist")
    
    parser.add_argument("--charset", type=str, default="a-z,0-9",
        help="Character set for custom wordlist (e.g., a-z, A-Z, 0-9, all, or custor char like abc123)")
    parser.add_argument("--min-length", type=int, default=1, help="Minimum password lenght")
    parser.add_argument("--max-length", type=int, default=3, help="Maximum password lenght")
    parser.add_argument("--first-char-rule", type=str, default=None, help="First character rule (e.g., A-Z)")
    parser.add_argument("--no-repeat", action="store_true", help="Password with no repeat character")
    parser.add_argument("--exclude-chars", type=str, default=None, help="Comma-seperated list of char to exclude (e.g., !,@,#)")
    
    #Optional Arguments
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose Outpue")
    parser.add_argument("-o", "--output", type=str, help="Path to save cracked password")
    parser.add_argument("-t", "--threads", type=int, help="Number of Threads", default=4)
    
    return parser.parse_args()