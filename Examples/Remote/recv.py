import socket
import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(12), 8)

UDP_IP = "IP_FROM_THIS_ESP"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    print ("received message:", int(data))
    for i in range(0, 8):
        np[i] = (int(data), int(data), int(data))
        np.write()
