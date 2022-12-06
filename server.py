import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = input("Enter IP: ")
port = int(input("Enter Port Number: "))

server.bind((ip, port))
#server.bind(("localhost", 9999))
server.listen()

client, addr = server.accept()

done = False

f = open('chat.txt', 'w')

while not done:
        received = client.recv(1024).decode('utf-8')
        f.write(received + "\n")
        if received == 'quit':
                done = True
        else:
                print(received)
                sent = input("Message: ")
                f.write("Server: " + sent + "\n")
                client.send(sent.encode('utf-8'))
