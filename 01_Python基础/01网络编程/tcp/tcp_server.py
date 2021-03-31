import socket


def main():
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 绑定信息
    tcp_server_socket.bind(("",7890))
    # 默认套接字设置为监听状态
    tcp_server_socket.listen(128)
    while True:
        print("等待一个客户端的到来：")
        new_client_socket,client_addr = tcp_server_socket.accept()
        print("一个新的客户端已经到来%s"%str(client_addr))

        # 接收客户端的请求
        recv_data = new_client_socket.recv(1024)
        print("客户端发送的数据是%s:" %recv_data.decode("gbk"))
        # 回送数据到客户端
        new_client_socket.send("收到你的请求了！".encode("gbk"))
        # 关闭套接字，不在为当前客户端服务
        new_client_socket.close()
        print("服务器已关闭...")

    # 如果将监听套接字关闭了，会导致不能再次等待新客户端的到来 即xxx.accept
    tcp_server_socket.close()



if __name__ == '__main__':
    main()