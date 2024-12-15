import threading
from concurrent.futures import ThreadPoolExecutor
from utils.colors import print_error

#Generic Threaded Cracker

def generic_threaded_cracker(task_function, task_args, tasks, num_threads):
    """
    Generic threading fn to divide tasks and run worker fn parallel.
    
    Args:
        task_function: fn to execute each task chunk
        task_args: tuple of extra arg passed to task fn
        tasks : list of task to be divided among threads
        num_threads : num of threads
    """
    
    chunk_size = len(tasks) // num_threads
    remainder = len(tasks) % num_threads
    task_chunks = []
    
    si = 0
    for i in range(num_threads):
        ei = si + chunk_size + (1 if i < remainder else 0)
        task_chunks.append(tasks[si:ei])
        si = ei
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for chunk in task_chunks:
            futures.append(executor.submit(task_function, chunk, *task_args))
            
            
            for future in futures:
                result = future.result()
                if result:
                    return result
    print_error("Password not found")
    return None