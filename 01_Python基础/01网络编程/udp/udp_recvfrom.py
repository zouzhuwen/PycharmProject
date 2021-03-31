import socket

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    localaddr = ('',7878)
    #绑定端口信息
    udp_socket.bind(localaddr)
    while True:
        recv_data = udp_socket.recvfrom(1024)
        recv_msg = recv_data[0]  #存储接收到的数据
        send_addr = recv_data[1]  #存储发送的地址

        print("%s %s"%(str(send_addr),recv_msg.decode("GBK")))

    udp_socket.close()

if __name__ == '__main__':
    main()