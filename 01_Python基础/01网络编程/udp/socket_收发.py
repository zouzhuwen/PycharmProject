import socket

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #绑定端口
    #udp_socket.bind(("",7788))
    #获取目标ip /port
    dest_ip = input("请输入对方的ip")
    try:
        dest_port = int(input("请输入对方的port"))
    except :
        pass

    #获取发送的内容
    masg = input("请输入要发送的内容")
    udp_socket.sendto(masg.encode("GBK"),(dest_ip,dest_port))

    #接收回送的消息
    data=udp_socket.recvfrom(1024)
    rec_ip = data[1]
    rec_data = data[0]
    print("%s %s" %(rec_ip,rec_data.decode("GBK")))




if __name__ == '__main__':
    main()