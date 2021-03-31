import socket

def send_msg(udp_socket):
    """发送数据"""
    dest_ip = input("请输入要发送的目标ip:")
    dest_port = int(input("请输入要发送的目标port:"))
    send_msg = input("请输入要发送的内容：")
    udp_socket.sendto(send_msg.encode("gbk"),(dest_ip,dest_port))

def recv_msg(udp_socket):
    """接收数据"""
    recv_data = udp_socket.recvfrom(1024)
    print("%s：%s" %(str(recv_data[1]),recv_data[0].decode("gbk")))

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("",7788))

    while True:
        print("=====xxx聊天器=====")
        print("1:发送消息 2:接收消息 3:退出应用 0:退出系统")
        op = input("请选择功能：")
        if op == "1":
            # 发送
            send_msg(udp_socket)
        elif op == "2":
            # 接收
            recv_msg(udp_socket)
        elif op == "0":
            break
        else :
            print("你输入有误请重新输入：")

if __name__ == '__main__':
    main()