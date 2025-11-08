import socket
import json
from translator import translate
HOST = ''              # Endereco IP do Servidor
PORT = 5300            # Porta que o Servidor ouvirá
orig = (HOST, PORT)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    print("Conectado com %s" % str(cliente))

    while True:
        msg = con.recv(1024)
        if not msg:
            break
        print(msg)
        request = json.loads(msg)
        resposta = "SERVER SIDE: " + str.upper(translate(str(request['msg']), request['language']))
        con.send(resposta.encode('utf-8'))

    print(str.format("Finalizando conexao do cliente {}", cliente))

    con.close()