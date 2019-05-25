import socket
import time
import threading


address = ('127.0.0.1', 10086)

def handle_request(request):
    num = 0
    while num <= 5:
        data = request.recv(1024)
        print(data.decode('utf-8'))
        request.send(b'hello')
        time.sleep(1)
        num += 1
        if num == 5:
            request.send(b'keep-alive')


def run_server(address):
    with socket.socket() as s:
        s.bind(address)
        s.listen()
        while True:
            conn, address = s.accept()
            if conn:
                t = threading.Thread(target=handle_request, args=(conn,), name='connct{0}'.format(conn))
                t.start()
            time.sleep(.5)
            

if __name__ == '__main__':
    run_server(address)