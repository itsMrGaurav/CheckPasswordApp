import requests
import hashlib
import sys

def get_responses(hash_value):
    url='https://api.pwnedpasswords.com/range/'+hash_value
    try:
        res=requests.get(url)
    except:
        return -1
    if res.status_code==200:
        return res.text
    else:
        return -2


def get_count(hashes,hash_to_check):
    hashes=(line.split(':') for line in hashes.splitlines())
    for h,count in hashes:
        if h == hash_to_check:
            return count
    return 0

    
def check_password(passwd):
    password=hashlib.sha1(passwd.encode('utf-8')).hexdigest().upper()
    first5_chr,tail=password[:5],password[5:]
    res=get_responses(first5_chr)
    if res not in [-1,-2]:return get_count(res,tail)
    else: return res

def main(passwords):
    for password in passwords:
        count=check_password(password)
        if count>=0:
            if count:
                print(f'{password} is pawned {count} times...time to change your password.')
            else:
                print(f'{password} is clear.')

if __name__=='__main__':
    main(sys.argv[1:])