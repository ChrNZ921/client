# server.py
import socket
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = "127.0.0.1", 9721

server.bind((host , port))
server.listen(999)

socket_objets = [server]
print("le serveur est e attente de connexions...")
print("serveur connecté !")

client_connect = True

# un dictionnaire pour stocker les identifiants des clients
client_ids = {}

while client_connect:
    print("client connecté")
    #print(f"{len(socket_objets) } clients connectés")
    liste_lu, liste_acce_Ecrit , exception = select.select(socket_objets,[],socket_objets)

    for socket_objet in liste_lu:
        if socket_objet is server:
            client , adresse = server.accept()
            socket_objets.append(client)
            # générer un identifiant aléatoire pour le client
            client_id = str(len(socket_objets) - 1)
            # associer l'identifiant au socket du client
            client_ids[client] = client_id
            # envoyer l'identifiant au client
            client.send(f"Votre identifiant est {client_id}".encode("utf_8"))



        else:
            donnees_recues = socket_objet.recv(200).decode("utf_8")

            if donnees_recues:
                # récupérer l'identifiant du client
                client_id = client_ids[socket_objet]
                # ajouter le préfixe à la réponse
                reponse = f"{client_id}. {donnees_recues}"
                # envoyer la réponse au client
                socket_objet.send(reponse.encode("utf_8"))
                print(reponse)

            else:
                socket_objets.remove(socket_objet)
                print("Client déconnecté...")
                print(f"{len(socket_objets)-1} clients connectés")