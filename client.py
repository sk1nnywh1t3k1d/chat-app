import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


ip = input("Enter IP Address: ")
port = int(input("Enter Port Number: "))

client.connect((ip, port))

#client.connect(("localhost", 9999))

done = False

f = open('log.txt', 'w')

while not done:
        sent = input("Message: ")
        f.write("Client: "+sent +"\n")
        client.send(sent.encode('utf-8'))
        received = client.recv(1024).decode('utf-8')
        f.write("Server: " + received+"\n")
        if received == 'quit':
                done = True
        else:
                print(received)
