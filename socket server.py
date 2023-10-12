import socketserver

class MyTCPhandler(socketserver.BaseRequestHandler):

    def handle(self) :
        self.data = self.request.recv(1024).strip()
        print("{} worte: ".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())

if __name__=="__main__":

    HOST, PORT = "localhost", 9999

    with socketserver.TCPServer((HOST,PORT),MyTCPhandler) as server:

        server.serve_forever()