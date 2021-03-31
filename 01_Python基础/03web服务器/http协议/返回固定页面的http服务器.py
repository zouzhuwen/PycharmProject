import  socket
from re import match
from urllib import parse
from urllib import request
import multiprocessing
import threading
import gevent
from gevent import  monkey

monkey.patch_all()


def server_client(new_socket):
    # 1.接收浏览器发送过来的请求，即http请求
    # GET /HTTP/1.1
    # ...
    request = new_socket.recv(1024).decode("utf-8") #将请求的字节转成字符串
    # 字符串切割
    request_lines = request.splitlines()
    print(">"*20)
    print(request_lines)

    # GET / HTTP/1.1
    ret = match(r"[^/]+(/[^ ]*)",request_lines[0])

    if ret:
        file_name = ret.group(1)
        # url解码
        encode_url = parse.unquote(file_name)
        print("*"*50,encode_url)
        if file_name == "/":
            encode_url = "/index.html"

    try:
        f = open(r"./智慧房产html版0902"+encode_url,"rb")
    except Exception as ret:
        print(ret)
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "---file not found---"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        # 给浏览器返回数据
        respose = "HTTP/1.1 200 OK\r\n"
        respose += "\r\n"
        new_socket.send(respose.encode("utf-8"))
        new_socket.send(html_content)

    # 关闭套接字
    new_socket.close()



def main():
    """用来完成整体控制"""
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    # 绑定
    tcp_server_socket.bind(("",7890))

    # 变为监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 等待客户端的链接
        new_socket,client_addr = tcp_server_socket.accept()

        # 为这个客户端服务
        # 协程实现
        g = gevent.spawn(server_client,new_socket)
        g.join()

        # 线程实现
        # t = threading.Thread(target=server_client,args=(new_socket,))
        # t.start()

        # 进程实现
        # p = multiprocessing.Process(target=server_client,args=(new_socket,))
        # p.start()
        #
        # new_socket.close()

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()