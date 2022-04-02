from optparse import OptionParser
from socket import AF_INET, SOCK_STREAM, socket, gethostbyname, gethostbyaddr, setdefaulttimeout


def connection_scanner(tgt_host, tgt_port):
    try:
        connection_socket = socket(AF_INET, SOCK_STREAM)
        connection_socket.connect((tgt_host, tgt_port))
        connection_socket.send('ViolentPython\r\n')
        results = connection_socket.recv(100)
        print(f'[+] {tgt_port} / tcp open')
        print(f'[+] {results}')
        connection_socket.close()
    except:
        print(f'[-] {tgt_port} / tcp closed')

def port_scanner(tgt_host, tgt_ports):
    try:
        tgt_ip = gethostbyname(tgt_host)
    except:
        print(f'[-] Cannot Resolve {tgt_host}: unknown host')
        return
    try:
        tgt_name = gethostbyaddr(tgt_ip)
        print(f'[+] Scan Results for: {tgt_name[0]}')
    except:
        print(f'[+] Scan Results for: {tgt_ip}')
    setdefaulttimeout(1)
    for tgt_port in tgt_ports:
        print(f'Scanning Port: {tgt_port}')
        connection_scanner(tgt_host, tgt_port)

def main():
    parser = OptionParser('usage %prog -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgt_host', type='string', help='Specify target host')
    parser.add_option('-p', dest='tgt_ports', type='string', help='Specify target port')
    (options, _args) = parser.parse_args()
    tgt_host = options.tgt_host
    tgt_ports = str(options.tgt_ports).split(',')
    print(tgt_ports)
    if tgt_host is None or tgt_ports is None:
        print(parser.usage)
        exit(0)

    port_scanner(tgt_host, tgt_ports)

if __name__ == '__main__':
    main()

