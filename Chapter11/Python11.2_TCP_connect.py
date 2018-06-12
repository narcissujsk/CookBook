from socket import socket,AF_INET,SOCK_STREAM
import  time
import datetime
s=socket(AF_INET,SOCK_STREAM)
s.connect(('localhost',20000))
s.send(b'Hello')
re=s.recv(8192)
print(re)
if __name__ == "__main__":
    while True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        s.send(b'hi')
        time.sleep(1)
        re=s.recv(8192)
        print(re)

