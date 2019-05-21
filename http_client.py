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
    

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        pass