from zipfile import ZipFile
from threading import Thread

def extract_file(z_file, pwd):
    try: 
        z_file.extractall(pwd=pwd)
        print(f'[+] Found Password {pwd}')
        return pwd
    except Exception as _:
        pass

def main():
    z_file = ZipFile('evil.zip')
    p_file = open('dictionary.txt')
    for line in p_file.readlines():
        pwd = line.strip('\n').encode('cp850','replace')
        t = Thread(target=extract_file, args=(z_file, pwd))
        t.start()

if __name__ == '__main__':
    main()
