#importation de la bibliotheque socket
import socket
#adresses et port
host,port = ('',5566)
#création d'un objet socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#lier le socket avec le serveur
socket.bind((host,port))
print("le serveur est démarré")

#boucle de traitement de requetes
while True:
    socket.listen(66)
    conn, address = socket.accept()
    print("un client viens de ce connecter.")
    client_id=generate_id()
    client_ids[conn]=client_id
    bienvenue= f"{client_id} est votre identifiant .\n"
    conn.sendall(bienvenue).encode("utf-8")
    data = conn.recv(1024)
    data = data.decode("utf-8")
    print( data )

