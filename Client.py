import socket
import math
p = ''

HEADER = 64   # length of received data
PORT = 5051   # port that is being used
FORMAT = "utf-8"   # format that info will be in
#  DISCONNECT_MESSGAGE = "!Disconnected"
SERVER = socket.gethostbyname(socket.gethostname())   # getting the computers IP address
ADDR = (SERVER, PORT)   # variables represented in a tuple


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


def encrypt(msg):
    word = msg
    m = 0
    e_word = ['']

    for x in word:
        n = ord(x)
        n = (n**2) - 8
        i = chr(n)
        e_word.append(i)
        m = m + 1

    global p
    p = ''.join(e_word)


mssgg = input("Enter your message here:")
encrypt(mssgg)
send(p)
#  send(DISCONNECT_MESSGAGE)
