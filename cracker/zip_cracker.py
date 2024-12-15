import zipfile
from tqdm import tqdm
from utils.colors import print_success, print_error, ColorConfig

#Thread
from concurrent.futures import ThreadPoolExecutor

import os

def crack_zip(zip_file, wordlist_file, verbose, isWordlist, threads):
    
    if not os.path.exists(zip_file):
            print(f"[-] {zip_file} does not exist")
            return None, None

    if isWordlist:

        if not os.path.exists(wordlist_file):
            print(f"[-] {wordlist_file} does not exist")
            return None, None
        
        if os.path.isfile(wordlist_file):
            with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as wordlist:
                passwords = wordlist.readlines()
    else:
        passwords = [wordlist_file.strip()]  
        
        
    cracked_password = crack_zip_thread(zip_file, passwords, verbose, threads)   


def crack_zip_thread(zip_file, passwords, verbose, num_threads):
    
    #Divide pwd for each thread
    chunk_size = len(passwords) // num_threads
    remainder = len(passwords) % num_threads
    passwords_chunk = []

    si=0
    for i in range(num_threads):
        ei = si + chunk_size + (1 if i < remainder else 0)
        passwords_chunk.append(passwords[si:ei])
        si = ei
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for chunk in passwords_chunk:
            futures.append(executor.submit(crack_zip_worker, zip_file, chunk, verbose))
            
        for future in futures:
            res = future.result()
            if res: return res
                        
    #No pass found        
    print_error("Password not Found")
    return None


def crack_zip_worker(zip_file, passwords_chunk, verbose):
    
    with zipfile.ZipFile(zip_file, 'r') as zf:
        for pwd in tqdm(passwords_chunk, desc="Cracking ZIP", leave=False):
            if verbose:
                tqdm.write(f"{ColorConfig.INFO}Trying password: {pwd.strip()}{ColorConfig.RESET}")
            try:
                zf.setpassword(bytes(pwd.strip(), 'utf-8'))
                #password found
                if zf.testzip() is None:
                    print_success(f"Password found: {pwd.strip()}")
                    return pwd.strip()
            except RuntimeError:
                continue
            
    return None