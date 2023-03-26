import socket,time
 
udp_socket = socket.socket(type=socket.SOCK_DGRAM)
udp_socket.connect(('192.168.232.130',2425))

package = time.time()
content = "hello feiq"
send_data = ('1.0:' + str(package) + ':_hang:' + "hostname" + ':32:' + content)
for i in range(1000):
    udp_socket.send(send_data.encode())

udp_socket.close()