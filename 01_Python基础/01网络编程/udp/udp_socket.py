import socket

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定端口信息，需要绑定一个元祖
    udp_socket.bind(("",8989))
    while True :
        send_data = input("请输入要发送的数据...")
        if send_data=='exit':
            break
        udp_socket.sendto(send_data.encode('GBK'),("10.48.84.231",8080))

    udp_socket.close()

if __name__ == '__main__':
    main()