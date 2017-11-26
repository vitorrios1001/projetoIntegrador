import socket


def cliente(host,port,msg):
    
    HOST = host     # Endereco IP do Servidor
    PORT = port            # Porta que o Servidor esta
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)
    print 'Para sair use CTRL+X\n'
    msg = msg

    ativo = True    
    while ativo:
        tcp.send (msg)
        ativo = False
    tcp.close()