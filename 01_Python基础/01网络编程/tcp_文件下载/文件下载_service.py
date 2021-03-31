import socket


def send_to_file(client_socket,client_addr):
    print("连接的客户端:{}".format(str(client_addr)))
    # 接收客户端数据
    file_name = client_socket.recv(1024).decode("utf-8")
    print("客户端发送的数据：{}".format(file_name))
    file_content = None
    try :
        f = open(file_name,'rb')
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有找到名为{}的文件".format(file_name))
        print(ret)
    if file_content:
        client_socket.send(file_content)



def main():
    service_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 绑定端口号
    service_socket.bind(("",7890))
    # 监听
    service_socket.listen(128)
    #分配连接客户端的socket 获取客户端地址
    client_socket,client_addr = service_socket.accept()
    # 调用send_to_file()方法
    send_to_file(client_socket, client_addr)

    client_socket.close()
    service_socket.close()




if __name__ == '__main__':
    main()