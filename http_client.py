import socket
import sys


MAX_LENGTH = 65536
address_default = ('127.0.0.1', 80)


def clientrequest(request, address=address_default):
    '''
    GET / HTTP/1.1\r\n
    Host: baidu.com\r\n
    Connection: keep-alive\r\n
    Upgrade-Insecure-Request: 1\r\n
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;v=b3\r\n
    Accept-Encoding:gzip, deflate\r\n
    Accept-Language:zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7\r\n
    Cookie:xx=xx;yy=yy\r\n
    \r\n
    ----
    useage: http_client.py ip:port/path get/post [postting]
    '''
    
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None) as s:
        s.connect(address)
        s.sendall(request)
        data = s.recv(MAX_LENGTH)
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
        useage('method format error')
        return False
    return True

def assemble_headers(**kwargs):
    '''
    1.generally header
    2.request   header
    3.post      header
    4.body      header
    5.extend    header
    '''
    header_str = ''
    for k, v in dict(kwargs).items():
        header_str = header_str + '{0}: {1}\r\n'.format(k, v)
    return header_str

def assemble_http_packet(header_str, method='GET', url='/', 
            http_verion='1.1', **kwargs):
    start_line = '{0} {1} HTTP/{2}\r\n'.format(method, url, http_verion)
    return start_line + header_str

'''
######################recive###########################
'''

def parse_response(response_data):
    response_line = response_data[0]
    if isinstance(response_line, str):
        http_version, _, status_str = response_line.deocde('utf-8').partition(' ')
        stats_code, _, desc_str = status_str.partition(' ')
    
    headers = dict()
    header_end_postion = response_data.index('\r\n')
    header_str_list = [header_ele.decode('utf-8') for header_ele in  
                response_data[1:header_end_postion]]
    for header_str in header_str_list:
        key, _, value = header_str.partition(':')
        headers[key] = value.strip()
    
    body = response_data[header_end_postion+1:]
    return http_version, stats_code, desc_str, headers, body
        


if __name__ == '__main__':
    if len(sys.argv) < 5:
        useage()
    
    # parse ip and url
    ip_and_url = sys.argv[1]

    ip = sys.argv[1].partition(':')[0]
    if check_ip(ip) != True:
        exit -1
    port = sys.argv[1].partition('/')[0].partition(':')[2]
    if check_port(port) != True:
        exit -1
    url = '/' + sys.argv[1].partition('/')[2]
    address_default = (ip, port)

    # parse method
    method = sys.argv[2]
    if check_method != True:
        exit -1

    # assemble headers
    header_str = assemble_headers(host=ip)

    # assemble http packet
    request = assemble_http_packet(header_str=header_str, method=method,
                                        url=url)

    # send request and recv response
    clientrequest(request)
