import socket


server_address = ('127.0.0.1', 80)

def make_server():
    '''
    HTTP/1.1 302 Moved Temporarily\r\n
    Server: bfe/1.0.8.18/r/n
    Date: Tue, 21 May 2019 06:49:36 GMT\r\n
    Content-Type: text/html\r\n
    Content-Length: 161\r\n
    Connection: Keep-Alive\r\n
    Location: https://www.baidu.com\r\n
    Expires: web, 22 May 2019 06:49:36 GMT\r\n
    Cache-Control: max-age=86400\r\n
    Cache-Control: privae\r\n
    File Date: 161 bytes\r\n
    \r\n
    body
    '''
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None) as s:
        s.bind(server_address)
        s.listen()
        while True:
            conn, address = s.accept()
            if conn:
                data = conn.recv(1024)
                if not data:break
                conn.sendall(data)
                
    
    