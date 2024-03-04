import hashlib
import itertools
import string
import keyboard
import time
import re

#current_dir = os.path.dirname(os.path.abspath(__file__))
# current_dir = r"C:\Users\brugarrido\OneDrive - Deloitte (O365D)\Python Scripts\a_Hash_Finder"
# wordlist_path = current_dir + r"\\a_Hash_Finder\\rockyou.txt"
wordlist_path = r"..\a_Hash_Finder\rockyou.txt"
with open(wordlist_path, encoding='latin-1') as wordlist_open:
    wordlist = wordlist_open.read().splitlines()


def menu():
    print('''
    +---------------------------------+
    |         Sha256 Hashcrack        |
    +---------------------------------+
    | Select an option:               |
    +---------------------------------+
    | 1 - Hash a String               |
    | 2 - BruteForce hash into string |
    | 3 - Wordlist hash check         |      
    | 4 - Exit                        |
    +---------------------------------+''')


def find_hash(data):
    if isinstance(data, str):
        data = data.encode()

    sha256_hash = hashlib.sha256(data).hexdigest()

    return sha256_hash

def brute_force(hash_to_find, length):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + string.whitespace

    for guess in itertools.product(characters, repeat=length):
        guess = ''.join(guess)
        if find_hash(guess) == hash_to_find:
            return guess

    return None

def try_wordlist(hash_to_find, wordlist):
    for word in wordlist:
        wl = find_hash(word)
        if wl == hash_to_find:
            return word
        
    return f'String not found for {hash_to_find}.'


def is_sha256(string):
    if re.fullmatch(r'[A-Fa-f0-9]{64}', string) is not None:
        return True
    return False


def welcome_screen():
    print('''
        .-')    ('-. .-.   ('-.                                                                  
    ( OO ). ( OO )  /  ( OO ).-.                                                              
    (_)---\_),--. ,--.  / . --. / .-----. .------.   ,--.                                      
    /    _ | |  | |  |  | \-.  \ / ,-.   \|   ___|  /  .'                                      
    \  :` `. |   .|  |.-'-'  |  |'-'  |  ||  '--.  .  / -.                                     
     '..`''.)|       | \| |_.'  |   .'  / `---.  '.| .-.  '                                    
    .-._)   \|  .-.  |  |  .-.  | .'  /__ .-   |  |' \  |  |                                   
    \       /|  | |  |  |  | |  ||       || `-'   /\  `'  /                                    
     `-----' `--' `--'  `--' `--'`-------' `----''  `----'                                     
    ('-. .-.   ('-.      .-')    ('-. .-.           _  .-')     ('-.               .-. .-')   
    ( OO )  /  ( OO ).-. ( OO ). ( OO )  /          ( \( -O )   ( OO ).-.           \  ( OO )  
    ,--. ,--.  / . --. /(_)---\_),--. ,--.   .-----. ,------.   / . --. /   .-----. ,--. ,--.  
    |  | |  |  | \-.  \ /    _ | |  | |  |  '  .--./ |   /`. '  | \-.  \   '  .--./ |  .'   /  
    |   .|  |.-'-'  |  |\  :` `. |   .|  |  |  |('-. |  /  | |.-'-'  |  |  |  |('-. |      /,  
    |       | \| |_.'  | '..`''.)|       | /_) |OO  )|  |_.' | \| |_.'  | /_) |OO  )|     ' _) 
    |  .-.  |  |  .-.  |.-._)   \|  .-.  | ||  |`-'| |  .  '.'  |  .-.  | ||  |`-'| |  .   \   
    |  | |  |  |  | |  |\       /|  | |  |(_'  '--'\ |  |\  \   |  | |  |(_'  '--'\ |  |\   \  
    `--' `--'  `--' `--' `-----' `--' `--'   `-----' `--' '--'  `--' `--'   `-----' `--' '--' 
        ''')


def main():
    menu()
    sel = input('')
    while sel !='4':
        if sel == '1':
            data = input('Type a string to find its hash: ')
            start = time.time()
            hash_to_find = find_hash(data)
            end = time.time()
            print(f'Sha256 hash for {data}: {hash_to_find}.\nTime taken: {end-start} seconds.')

        elif sel == '2':
            hash_to_find = input('Type an hash to BruteForce it\'s string: ')
            sha = is_sha256(hash_to_find)
            length = 1
            result = None

            if sha == True:
                while result is None:
                    print(f"Trying strings of length {length}...")
                    start = time.time()
                    result = brute_force(hash_to_find, length)
                    length += 1

                    if result is not None:
                        end = time.time()
                        print(f'Found string for {hash_to_find}: {result}.\nTime taken: {end-start} seconds.')
                        break
            else:
                print(f'{hash_to_find} is not a suitable sha256 hash.')
        

        elif sel == '3':
            wl_data = input(f'Type an hash to check against the wordlist: ')
            sha = is_sha256(wl_data)
            if sha == True: 
                start = time.time()       
                result = try_wordlist(wl_data, wordlist)

                if result is not None:
                    end = time.time()
                    print(f'Found string for {wl_data}: {result}.\nTime taken: {end - start} seconds.')
                else:
                    print(f'String not found for  {wl_data}.')
            else:
                print(f'{wl_data} is not a suitable sha256 hash.')

        else: print('Sorry, no option found.')
        menu()
        sel = input('')
    print('A Encerrar!')

welcome_screen()
print('Press "ENTER" to start!')
keyboard.wait("enter")
n = input("")
main()