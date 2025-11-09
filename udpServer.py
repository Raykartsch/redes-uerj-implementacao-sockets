import socket
from translator import translate
import json
HOST = ''              # Endereco IP do Servidor
PORT = 5300            # Porta que o Servidor esta

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

orig = (HOST, PORT)

udp.bind(orig)

print("Server ONLINE!")
while True:
    message, clientAddress = udp.recvfrom(2048)
    if not message: 
        break 
    print("Received from customer: ", message, clientAddress)
    message = json.loads(message)

    modifiedMessage = str.upper(translate(message['msg'], message['language'])).encode('utf-8')
    print("Returned:", modifiedMessage)
    udp.sendto(modifiedMessage, clientAddress)

udp.close()