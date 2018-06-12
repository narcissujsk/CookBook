from socketserver import BaseRequestHandler,ThreadingTCPServer,TCPServer
import datetime
class EchoHander(BaseRequestHandler):
    def handle(self):
        print('get connection from ',self.client_address)
        while True:
            msg=self.request.recv(8192)
            #print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            #print(msg)
            if not msg:
                break
            self.request.send(msg)


if __name__ == "__main__":
    from  threading import Thread
    num=3
    TCPServer.allow_reuse_address=True
    serv=TCPServer(('',20000),EchoHander)
    for n in range(num):
        t=Thread(target=serv.serve_forever)
        t.daemon=True
        t.start()
    serv.serve_forever()