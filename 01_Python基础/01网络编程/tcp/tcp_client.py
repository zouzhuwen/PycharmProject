import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip = input("请输入要发送的ip:")
    port = int(input("请输入要发送的port:"))
    # 链接服务器
    tcp_socket.connect((ip,port))

    send_data = input("请输入要发送的数据:")
    tcp_socket.send(send_data.encode("GBK"))

    # 关闭套接字
    tcp_socket.close()

if __name__ == '__main__':
    main()