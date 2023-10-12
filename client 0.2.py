
import socket

# creation de client socket
client_socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = "127.0.0.1", 9721

# connection au serveur
client_socket.connect((host,port))

# entrer le nom de l'utilisateur
nom = input("quel est votre nom ?")

if __name__ == "__main__":
    #
    running = True

    while running:
        #prendre message de l'utilisateur
        message = input(f"{nom}>")
        # envoi au server
        client_socket.send(f"{nom}> {message}".encode("utf_8"))
        # recoit la reponse du serveur
        data = client_socket.recv(1024)
        # affiche la reponse
        print(data.decode())
