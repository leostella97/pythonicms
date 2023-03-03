import socket # Biblioteca que faz o relacionamento d placa de rede com o sistema operacional
import sys # Biblioteca fornece acesso a algumas variáveis e funções que tem interação com o Python

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) # Objeto de conexão, 0 é o protocolo TCP
    except socket.error as e: # Caso der erro
        print("A conexão falhou")
        print("Erro: {}".format(e))
        sys.exit() # Caso der erro, sai do programa

    print("Socket criado com sucesso") # Caso passe pelo try

    host_alvo = input("Digite o IP/HOST a ser conectado: ") # Host a ser conectado
    porta_alvo = input("Digite a porta a ser conectada: ") # Porta a ser conectada

    try: # Tenta a conexão
        s.connect((host_alvo, int(porta_alvo))) # IP/HOST e porta alvo
        print("Cliente TCP conectado com sucesso!\nConectado em: " + host_alvo + " " + porta_alvo)
        s.shutdown(2) # Espera 2 segundos para finalizar a conexão para não ficar em looping
    except socket.error as e:
        print("Não foi possível conectar em: " + host_alvo + " " + porta_alvo)
        print("Erro {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()