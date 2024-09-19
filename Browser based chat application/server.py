import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind(('localhost', 9999)) 


server.listen()
print("Server is listening for connections...")


client, addr = server.accept()
print(f"Got a connection from {addr}")

done = False

while not done:
    
    msg = client.recv(1024).decode('utf-8')
    if msg == 'exit':  
        done = True
        print("Client disconnected.")
    else:
        print(f"Client: {msg}")

    message = input("Server: ")
    client.send(message.encode('utf-8'))

client.close()
server.close()
