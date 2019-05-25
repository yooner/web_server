import socket
import time
import threading
import queue


address = ('127.0.0.1', 10086)
q = queue.Queue()
thread_q = queue.Queue()
temp_use_list = []

def handle_request():
    try:
        request = q.get(timeout=2)
    except queue.Empty:
        print('empty')
        return False
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
                q.put(conn)
                t = thread_q.get(timeout=5)
                t.start()
                temp_use_list.append(t)
            time.sleep(.5)
        
for num in range(3):
    t = threading.Thread(target=handle_request, args=(), name='')
    thread_q.put(t)

def monitor_thread_use():
    while True:
        if len(temp_use_list):



if __name__ == '__main__':
    run_server(address)