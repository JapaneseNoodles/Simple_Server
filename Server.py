import socket
import threading
import time
import math

HEADER = 64   # length of received data
PORT = 5051   # port that is being used
SERVER = socket.gethostbyname(socket.gethostname())   # getting the computers IP address
ADDR = (SERVER, PORT)   # variables represented in a tuple
FORMAT = "utf-8"   # format that info will be in
DISCONNECT_MESSGAGE = "!Disconnected"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # states that we're using ipv4 / TCP and streaming info
server.bind(ADDR)   # binding the socket to the address. Any connections to this address will hit the socket


def decrypt(d_msg):
    word = d_msg
    m = 0
    d_word = ['']

    for x in word:
        n = ord(x)
        n = math.sqrt(n+8)
        i = chr(int(n))
        d_word.append(i)
        m = m + 1

    global b
    b = ''.join(d_word)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected \n")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)   # checking the length of the message
        if msg_length:
            msg_length = int(msg_length)   # converting info to int
            msg = conn.recv(msg_length).decode(FORMAT)   # receiving the message
            decrypt(msg)

            if msg == DISCONNECT_MESSGAGE:
              connected = False

            print(f"[{addr}] {msg} ")
            print("DECRYPTING...")
            time.sleep(5)
            print(f"[{addr}] {b}")   # printing the message
            conn.send("Message received".encode(FORMAT))

    conn.close()


def start():
    server.listen()   # watches for new connections
    print(f"[LISTENING] Server is listening to {SERVER}")
    while True:
        conn, addr = server.accept()   # accepts that connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))   # creates a thread for the class
        thread.start()   # starts the thread
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")   # shows active threads


print("[STARTING] server is starting......")
start()
