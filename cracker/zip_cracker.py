import zipfile
from tqdm import tqdm

from utils.colors import ColorConfig
from utils.thread_handler import generic_threaded_cracker

def crack_zip_worker(passwords_chunk, zip_file, verbose):
    
    with zipfile.ZipFile(zip_file, 'r') as zf:
        for pwd in tqdm(passwords_chunk, desc="Cracking ZIP", leave=False):
            if verbose:
                tqdm.write(f"{ColorConfig.INFO}Trying password: {pwd.strip()}{ColorConfig.RESET}")
            try:
                zf.setpassword(bytes(pwd.strip(), 'utf-8'))
                #password found
                if zf.testzip() is None:
                    tqdm.write(f"{ColorConfig.SUCCESS}Password found: {pwd.strip()}{ColorConfig.RESET}")
                    return pwd.strip()
            except Exception as e:
                continue
            
    return None

def crack_zip(zip_file, wordlist_file, verbose, threads):
    
    passwords = wordlist_file
    
    if passwords is None:
        return None  
        
    cracked_password = generic_threaded_cracker(
        task_function=crack_zip_worker,
        task_args=(zip_file, verbose),
        tasks=passwords,
        num_threads=threads
        )   
    
    return cracked_password
