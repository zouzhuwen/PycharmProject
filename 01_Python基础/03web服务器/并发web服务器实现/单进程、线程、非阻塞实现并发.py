import socket
import time

tcp_server_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_server_tcp.bind(("",7890))
tcp_server_tcp.listen(128)
tcp_server_tcp.setblocking(False) #  设置套接字为非阻塞状态

client_socket_list = list()

while True:
    time.sleep(0.8)
    try:
        new_socke,new_addr = tcp_server_tcp.accept()

    except  Exception as ret:
        print(ret)
        print("---客户端没有到来---")
    else:
        print("---只要没产生异常，那就意味着 来了一个新的客户端---")
        new_socke.setblocking(False) #  设置套接字为非阻塞状态
        client_socket_list.append(new_socke)

    for client_socket in client_socket_list:

        if client_socket:
            try:
                recv_date = client_socket.recv(1024)
            except Exception as ret:
                print(ret)
                print("---这客户端没有发送数据----")
            else:
                if client_socket:
                    # 对方发来数据
                    print("---对方发来数据---")
                else:
                    # 对方调用了close 导致recv返回
                    client_socket.close
                    client_socket_list.remove(client_socket)