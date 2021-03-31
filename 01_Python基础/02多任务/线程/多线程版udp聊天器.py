import threading
import socket

def recv_msg(udp_socket):
    while True:
        data = udp_socket.recvfrom(1024)
        print("来自{}：{}".format(data[1],data[0].decode('gbk')))


def send_msg(udp_socket,dest_ip,dest_port):
    while True:
        data = input("请输入要发送的数据：")
        udp_socket.sendto(data.encode("gbk"),(dest_ip,dest_port))

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("",7890))
    dest_ip = input("请输入对方的ip:")
    dest_port = int(input("请输入对方的port："))

    t_recv = threading.Thread(target=recv_msg,args=(udp_socket,))
    t_send = threading.Thread(target=send_msg,args=(udp_socket,dest_ip,dest_port))

    t_recv.start()
    t_send.start()



if __name__ == '__main__':
    main()