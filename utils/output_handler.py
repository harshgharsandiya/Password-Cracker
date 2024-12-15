import json

def write_output(file, password, output, verbose):
    if output:
        try: 
            #Handle default extension (.txt)
            if '.' not in output:
                output += '.txt'
            
            if output.endswith('json'):
                result = {
                    "File": file,
                    "Password ": password if password else "Not Found"
                }
                with open(output, 'a', encoding='utf-8') as out:
                    json.dump(result, out, ensure_ascii=False)
                    out.write("\n")
            else:
                with open(output, 'a', encoding='utf-8') as out:
                    if password:
                        out.write(f"File: {file} | Password Found: {password}\n")
                    else:
                        out.write(f"File: {file} | Password Not Found")
    
            if verbose:
                print(f"[+] Results saved to {output}")
        except Exception as e:
            if verbose:
                print(f"[-] Failed to write output: {e}")
                