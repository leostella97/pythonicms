import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Objeto de conexão

print("Cliente socket criado com sucesso!") # Caso criado com sucesso

host = 'localhost' # Coloca a rede interna como o host
porta = 5433
mensagem = "Olá, servidor"

try:  # Tentativa de envio da mensagem
    print("Cliente: " + mensagem)
    s.sendto(mensagem.encode(), (host, 5432)) # Encapoca e envia a mensagem em UDP para o host

    dados, servidor = s.recvfrom(4096) # As duas variáveis recebem a resposta
    dados = dados.decode # Desempacota os dados recebidos
    print("Cliente: " + dados)

finally:
    print("Cliente: Fechando a conexão")
    s.close() # Fecha a conexão