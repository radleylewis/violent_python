from crypt import crypt

def test_password(crypt_password):
    salt = crypt_password[0:2]
    dict_file = open('dictionary.txt', 'r')
    for word in dict_file.readlines():
        word = word.strip('\n')
        crypt_word = crypt(word, salt)
        if crypt_word == crypt_password.strip('\n'):
            print(f'[+] Found Password: {word}\n')
            return
    print(f'[-] Password Not Found.\n')

def main():
    passfile = open('passwords.txt')
    for line in passfile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            crypt_password = line.split(':')[1].strip(' ')
            print(f'[*] Cracking Password for User: {user}')
            test_password(crypt_password)

if __name__ == "__main__":
    main()


