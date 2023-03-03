import os # Importa a biblioteca os (integra os programas e recursos do sistema)

print("#" * 60) # 60 hashtags no começo

ip_host = input("Digite o IP ou HOST a ser verificado: ") # Pede o ip/host e coloca na variável ip_host

print("-" * 60) # 60 traços no final

os.system('ping -n 6 {}'.format(ip_host)) # Manda 6x pings para o ip/host
