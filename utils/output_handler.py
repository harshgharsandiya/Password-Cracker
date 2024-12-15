def write_output(password, output, verbose):
    try: 
        if output:
            with open(output, 'w', encoding='utf-8') as out:
                if password:
                    out.write(f"Password Found: {password}\n")
                else:
                    out.write(f"Password Not Found")

            if verbose:
                print(f"[+] Results saved to {output}")
    except Exception as e:
        if verbose:
            print(f"[-] Failed to write output: {e}")
            