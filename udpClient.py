import socket
import json
HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5300            # Porta que o Servidor esta

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

destination = (HOST, PORT)

print('Para sair use CTRL+X\n')

language = input('''
----------------------
en -> ingles
es -> espanhol
Selecione um idioma: ''')



while True:

    msg = input(f'''
    ----------------------
    ('ch lng' para trocar idioma, ENTER para sair)
    ({language.upper()}) Digite uma mensagem para traduzir: ''')


    if msg.lower() == 'ch lng':
        language = input('''
    ----------------------
    en -> inglês
    es -> espanhol
    Selecione um novo idioma: ''')
        continue

    if msg == '\x18':
        break

    request = {'msg': (str('') if msg is None else msg), 'language': (str('') if language is None else language)}
    request = str(json.dumps(request)).encode('utf-8')
    udp.sendto(request, destination)

    message, serverAddress = udp.recvfrom(2048)
    print(message, serverAddress)

udp.close()