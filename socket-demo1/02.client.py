import socket

s = socket.socket()
s.connect(('127.0.0.1',6666))

while True:
    msg = input("要发送的内容")
    s.send(msg.encode())
    receive = s.recv(10240)
    print(f"服务器返回:{receive.decode()}")