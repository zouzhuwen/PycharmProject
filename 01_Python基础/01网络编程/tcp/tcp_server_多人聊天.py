import  socket

def main():
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 绑定客户端
    tcp_socket.bind(("",7890))
    # 默认套接字监听状态
    tcp_socket.listen(128) #  服务器能够接收的链接
    while True:
        print("等待客户端的连接：")
        client_socket,client_addr = tcp_socket.accept()#  服务器分配的scoket
        print("连接的客户端是：{}".format(client_addr))
        while True:
            # 接收客户端请求
            data = client_socket.recv(1024)
            if data:
                print("客户端发送的数据：{}".format(data.decode("gbk")))
                # 发送数据到客户端
                client_socket.send("我是服务器".encode("gbk"))
            else:
                break

        #关闭分配的套接字
        client_socket.close()

    # 关闭服务器套接字
    tcp_socket.close()




if __name__ == '__main__':
    main()