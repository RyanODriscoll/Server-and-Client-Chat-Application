import socket
import threading

HOST = socket.gethostname()
print("server will start on host : ", HOST)
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []
usernames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"{usernames[clients.index(client)]} says {message}")
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            usernames.remove(username)
            break
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}!")

        client.send("USER".encode('utf-8'))
        username = client.recv(1024)

        usernames.append(username)
        clients.append(client)

        print(f"Username of the  client is {username}")
        broadcast(f"{username} connected to the server!\n".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is running...")
receive()