import threading
from concurrent.futures import ThreadPoolExecutor

def crack_zip_thread(zip_file, passwords, verbose, num_threads=4):
    
    #Divide pwd for each thread
    chunk_size = len(passwords) // num_threads
    passwords_chunk = [passwords[i:i + chunk_size] for i in range(0, len(passwords), chunk_size)]
    
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
    
    with zip_file.ZipFile(zip_file, 'r') as zf:
        for pwd in tqdm(passwords_chunk, desc="Cracking ZIP"):
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