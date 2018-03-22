#coding:utf-8

import socket
import re

from multiprocessing import Process

HTML_ROOT_DIR = "./html"

def handle_client(clisock):
    request_data = clisock.recv(1023)
    print("request data:",request_data)

    request_lines = request_data.splitlines()
    for line in request_lines:
        print(line)

    request_start_line = request_line[0]
    print("*"*10)
    print(request_start_line.decode("utf-8"))
    file_name = re.match(r"\w+ +(/[^ ]*) ",request_start_line.decode("utf-8")).group(1)
    if "/" == file_name:
        file_name = "/index.html"
    try:
        file = open(HTML_ROOT_DIR + file_name,"rb")
    except IOError:
        response_start_line = "HTTP/1.1 404 Not Found\s\n"
        response_headers = "Server: My server\r\n"
        response_body = "The file is not found!"
    else:
        file_data = file.read()
        file.close()

        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server:My server\r\n"
        response_body = file_data.decode("utf-8")

    response = response_start_line + response_headers + "\r\n" + response_body
    print("response data:" ,response)

    clisock.send(bytes(response,"utf-8"))
    clisock.close()

if __name__ == "__main__":
    sersock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sersock.bind(("",8000))
    sersock.listen(10)

    while True:
        clisock,cliaddr = sersock.accept()
        print("[%s %s]用户连接上" %(cliaddr[0],cliaddr[1]))
        handlecli = Process(target=handle_client,args=(clisock,))
        handlecli.start()
        clisock.close()


