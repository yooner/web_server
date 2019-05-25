import socket
import time
import threading


thread_num = 5
address = ('127.0.0.1', 10086)

def run_client(address):
    data = ''
    with socket.socket() as s:
        s.connect(address)
        while data != 'keep-alive':
            s.send(b'hello')
            data = s.recv(1024)
            data = data.decode('utf-8')
            print(data)
            time.sleep(2)            
        
if __name__ == '__main__':
    thread_list = []
    for num in range(thread_num):
        t = threading.Thread(target=run_client, args=(address,), name ='thread:{0}'.format(num))
        thread_list.append(t)
    
    for thread in thread_list:
        thread.start()
    
    for thread_end in thread_list:
        thread_end.join()
    