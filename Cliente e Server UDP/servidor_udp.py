import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Conexão

print("Socket criado com sucesso!")

host = "localhost" # Definindo o servidor interno como host
port = 5432

s.bind((host, port)) # Ligação entre cliente e servidor
mensagem = "Servidor: Olá, cliente"

while 1: # Enquanto for verdadeiro
    dados, end = s.recvfrom(4096) # Recebe a mensagem para duas variáveis, dados e endereco

    if dados:
        print("Servidor enviando mensagem...")
        s.sendto(dados + (mensagem.encode()), end)