import socket
import json
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5300            # Porta que o Servidor esta
dest = (HOST, PORT)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(dest)

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

    if msg == '':
        break

    if msg.lower() == 'ch lng':
        language = input('''
----------------------
en -> inglês
es -> espanhol
Selecione um novo idioma: ''')
        continue

    request = {'msg': (str('') if msg is None else msg), 'language': (str('') if language is None else language)}
    tcp.send(str(json.dumps(request)).encode('utf-8'))

    ret = tcp.recv(1024)
    print(str(ret, encoding='utf-8'))


tcp.close()