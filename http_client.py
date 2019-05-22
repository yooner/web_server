import socket
import sys


address = ('127.0.0.1', 80)
def client(*argv):
    '''
    GET / HTTP/1.1\r\n
    Host: baidu.com\r\n
    Connection: keep-alive\r\n
    Upgrade-Insecure-Request: 1\r\n
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;v=b3\r\n
    Accept-Encoding:gzip, deflate\r\n
    Accept-Language:zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7\r\n
    Cookie:xx=xx;yy=yy\r\n
    ----
    useage: http_client.py ip:port/path
    '''
    
    if len(argv):
        pass
    with socket.socket(family=AF_INET, type=SOCKET_STEAM, proto=0, fileno=None) as s:
        s.connect(address)
        s.sendall(b'hello')
        data = s.recv(1024)
    print(data)
    
def useage(print_str=None):
    if print_str:
        print(print_str)
    print("useage: http_client.py ip:port/path get/post [postting]")
    
def check_ip(ip):
    split_ip_list = ip.split('.')
    if len(split_ip_list) != 4:
        useage('ip format error')
    try:
        split_ip_list = [0<= int(num) <=255 for num in split_ip_list]
    except ValueError as e:
        useage('ip format error')
        return False
    
    if set(split_ip_list) != {True}:
        useage('ip format error')
        return False
    return True        

def check_port(port):
    if not port:
        useage('port format error')
        return False
    try:
        port = int(port)
    except ValueError as e:
        useage('port format error')
        return False
    return True

def check_method(method):
    method_list = ['GET', 'POST']
    if method.upper() not in method_list:
        usegae('method format error')


if __name__ == '__main__':
    if len(sys.argv) < 5:
        useage()
    
    # parse ip and url
    ip_and_url = argv[1]

    ip = argv[1].partition(':')[0]
    if !check_ip(ip):
        return 
    port = argv[1].partition('/')[0].partition(':')[2]
    if !check_port(port):
        return
    url = '/' + argv[1].partition('/')[2]

    # parse method
    method = argv[2]



