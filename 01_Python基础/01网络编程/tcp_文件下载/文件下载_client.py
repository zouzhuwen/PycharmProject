import socket


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = input("请输入需求连接的ip:")
    port = int(input("请输入如需要连接的port:"))
    # 连接服务器
    client_socket.connect((ip, port))

    #发送数据
    filename = input("你要下载的文件:")
    client_socket.send(filename.encode("utf-8"))
    data = client_socket.recv(1024)
    if data:
        with open("[新]"+filename,'wb') as f:
            f.write(data)
            f.close()
    else:
        print("服务器不存在{}文件".format(filename))
    # 关闭客户端套接字
    client_socket.close()


if __name__ == '__main__':
    main()
    # f = open("2.txt",'rb')
    # print(f.read().encode("utf-8"))