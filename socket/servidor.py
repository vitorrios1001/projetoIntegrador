import socket
import os
import sys


def servidor(host,port):
    HOST = host     # Endereco IP do Servidor
    PORT = port     # Porta que o Servidor esta
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT)
    tcp.bind(orig)
    tcp.listen(1)

    ativo = True
    while ativo:
        con, cliente = tcp.accept()
        pid = os.fork()
        if pid == 0:
            tcp.close()
            print 'Conectado por', cliente
            while ativo:
                msg = con.recv(1024)
                if not msg: break
                print cliente, msg
                ativo = False
            print 'Finalizando conexao do cliente', cliente
            con.close()
            sys.exit(0)
        else:
            con.close()

    return msg        