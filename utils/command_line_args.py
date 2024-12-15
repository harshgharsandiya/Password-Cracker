import argparse

def parse_arg():
    
    parser = argparse.ArgumentParser(description="Crack a password-protected ZIP file using a wordlist.")
    
    #Add arguments
    parser.add_argument("-f", "--file", type=str, required=True, help="Path to the Zip File")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-w", "--word", type=str, help="Single password", default=None)
    group.add_argument("-W", "--wordlist", type=str, help="Path to the Wordlist File", default=None)
    
    #Optional Arguments
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose Outpue")
    parser.add_argument("-o", "--output", type=str, help="Path to save cracked password")
    parser.add_argument("-t", "--threads", type=int, help="Number of Threads", default=4)
    
    return parser.parse_args()