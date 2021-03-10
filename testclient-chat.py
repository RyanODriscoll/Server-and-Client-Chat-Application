import socket

class ClientChat():
    client = socket.socket()
    host = input(str("Please enter the hostname of the server : "))
    port = 8080
    client.connect((host,port))
    
    name = input(str("Please enter your username : \n"))
    print("Connected to chat server\n")
    client.send(name.encode())
    client_name = client.recv(1024)
    client_name = client_name.decode()
    print(client_name, "has joined the chat room\n")

    #When someone sends a message from the client it will be encoded and 
    #sent to the server-side
    while True:
        message = client.recv(1024)
        message = message.decode()
    
        print(client_name, ":" ,message)
    
        message = input(str("Please enter your message: "))
        message = message.encode()
        client.send(message)
    
        print("Sent\n") 