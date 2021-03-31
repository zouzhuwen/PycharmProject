import  socket
from re import match
from urllib import parse
from gevent import  monkey
import select

monkey.patch_all()

def server_client(new_socket,request):
    # 1.接收浏览器发送过来的请求，即http请求
    # GET /HTTP/1.1
    # ...
    #request = new_socket.recv(1024).decode("utf-8") #将请求的字节转成字符串
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
        f = open(r"..\http协议\智慧房产html版0902"+encode_url,"rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "---file not found---"
        new_socket.send(response.encode("utf-8"))
    else:
        html_conten = f.read()
        f.close()
        response_body = html_conten
        # 给浏览器返回数据
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"

        response = response_header.encode("utf-8")+response_body
        new_socket.send(response)

    # 关闭套接字
    # new_socket.close()



def main():
    """用来完成整体控制"""
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # IP地址和端口绑定到某个套接口上时，还允许此IP地址和端口捆绑到另一个套接口上。
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    # 绑定
    tcp_server_socket.bind(("",7890))
    # 变为监听套接字
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)  # 将套接字变成非堵塞

    # 创建一个epoll对象
    epl = select.epoll()

    # 将监听套接字对应的fd注册到epoll中
    epl.register(tcp_server_socket.fileno(),select.EPOLLIN)

    fd_event_dict = dict()

    while True:
        fd_event_list = epl.poll()  # 默认会堵塞，直到 os监测到数据到来 通过事件通知方式 告知这个程序 此时才会解堵塞

        # [(fd,event)] ,(套接字对应的文件描述符，这个文件描述符到底是什么事件 如：可以调用recv接收等)
        for fd,event in fd_event_list:
            # 等待客户端的链接
            if fd == tcp_server_socket.fileno():
                new_socket,client_add = tcp_server_socket.accept()
                epl.register(new_socket.fileno(),select.EPOLLIN)  # 将新的客户端注册到epoll
                fd_event_dict[new_socket.fileno()] = new_socket  # 将fd 和 new_scoket 放到字典中
            elif event == select.EPOLLIN:
                # 判断已经链接的客户端是否有发数据过来
                recv_date = fd_event_dict[fd].recv(1024).decode("utf-8")
                if recv_date:
                    server_client(fd_event_dict[fd],recv_date)
                else:
                    fd_event_dict[fd].close
                    epl.unregister(fd)
                    del fd_event_dict[fd]

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()