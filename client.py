import socket

host, port =('localhost',5566)
socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)



try:
    socket.connect((host, port))
    print("client connecté ! ")
    while True:
        bienvenue = socket.recv(1024)
        bienvenue = bienvenue.decode("utf-8")
        print(bienvenue)
        data = input( "entrez votre nom : ")
        data = data.encode("utf-8")
        socket.sendall(data)
except ConnectionRefusedError:
    print("Connexion au serveur échouée !")


