from zipfile import ZipFile
from optparse import OptionParser
from threading import Thread

def extract_file(z_file, pwd):
    try: 
        z_file.extractall(pwd=pwd)
        print(f'[+] Found Password {pwd}')
        return pwd
    except Exception as _:
        pass

def main():
    parser = OptionParser("usage%prog -f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest="zname", type="string", help="Specify Zip File")
    parser.add_option('-d', dest="dname", type="string", help="Specify dictionary file")

    (options, _) = parser.parse_args()

    if options.zname is None or options.dname is None:
        print(parser.usage)

    else:
        zname = options.zname
        dname = options.dname


        z_file = ZipFile(zname)
        p_file = open(dname)

        for line in p_file.readlines():
            pwd = line.strip('\n').encode('cp850','replace')
            t = Thread(target=extract_file, args=(z_file, pwd))
            t.start()

if __name__ == '__main__':
    main()
