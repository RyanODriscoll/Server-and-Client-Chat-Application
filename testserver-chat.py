import socket

class ServerChat():
    server = socket.socket()
    host = socket.gethostname()
    print("server will start on host : ", host)
    port = 8080
    server.bind((host,port))

    name = input(str("Please enter your username: \n"))
    print("Server is waiting for incoming connections\n")

    server.listen(1)
    conn, addr = server.accept()

    print("Recieved connection\n")
    server_name = conn.recv(1024)
    server_name = server_name.decode()
    print(server_name, "has joined the chat room")
    conn.send(name.encode())

    #When someone sends a message from the server it will be encoded and 
    #sent to the client-side
    while True:
        message = input(str("Please enter your message: "))
        conn.send(message.encode())
    
        print("Sent\n")
    
        message = conn.recv(1024)
        message = message.decode()
    
        print(server_name, ":" ,message)