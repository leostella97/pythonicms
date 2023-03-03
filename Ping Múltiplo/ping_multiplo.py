import os # Importa a biblioteca do sistema
import time #importa a biblioteca do tempo

with open('hosts.txt') as file: # Cria um alias para o arquivo
    dump = file.read() # coloca a leitura do arquivo na variável dump
    dump = dump.splitlines()  # Para não pular linha para caractere único
    
    for ip in dump:
        print("\n\nPingando o IP/HOST: ", ip) # Título antes do ping
        os.system('ping -n 2 {}' .format(ip)) # Envia ping para o ip/host no arquivo
        time.sleep(5) # Espera até pingar o próximo