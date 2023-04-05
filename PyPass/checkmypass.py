import requests
import hashlib
import sys


def req_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'error fetching: {res.status_code}')
    return res

def get_pass_count(hashes, checkhash):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == checkhash:
            return count
    return 0

def check_api(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    firstfive, tail = sha1password[:5], sha1password[5:]
    response = req_api_data(firstfive)
    return get_pass_count(response, tail)

def main(args):
    for password in args:
        count = check_api(password)
        if count:
            print(f'{password} was found {count}. You should change this! \n')
        else:
            print(f'{password} is all good!')

main(sys.argv[1:])
