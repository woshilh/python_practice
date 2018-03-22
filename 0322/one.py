#coding:utf-8
import socket
"""
from math import *

socket = 

sockfd = socket()
sockfd.bind()
sockfd.listen()
"""

from multiprocessing import Process

HTML_ROOT_DIR = ""

def handle_client(client_socket):
    request_data = client_socket.recv(1023)
    print("request data:",request_data)

    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    response_body = "hello itcast"
    response = response_start_line + response_headers + "\r\n" + response_body
    print("response data:", response)

    client_socket.send(bytes(response,"utf-8"))
    client_socket.close()

if __name__ == "__main__":
    sersockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    seraddr = ("",8000)
    sersockfd.bind(seraddr)
    sersockfd.listen(10)

    while True:
        clifd,cliaddr = sersockfd.accept()
        print("[%s,%s]用戶连接上" %(cliaddr[0],cliaddr[1]))
        handle_client_process = Process(target=handle_client,args=(clifd,))
        handle_client_process.start()
        clifd.close()

