from socket import *
import os

os.system('clear')
os.system('clear')

def get_ip(x, y):
    x = gethostbyname(y)
    print("\033[32mEndereço IP ====> \033[m", x)
    print (' ')
    print ('\033[32m=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~\033[m')

def menu():
    print ('''
\033[36m~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~\033[m
      \033[32m<<<------------------------------------>>>\033[m\033[33m                  <•••••> By: Ryan Garccia <•••••>\033[m
     \033[32m <<<------------------------------------>>>\033[m
\033[36m~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~\033[m
    ''')
    print (' ')
    print ('\033[32m             •••••••••••••••••••••••••••\033[m')
    print ('\033[32m            |\033[m\033[32m •••••••••••••••••••••••••\033[m \033[32m|\033[m')
    print ('\033[32m            | [ 1 ] Sair do Script \033[m \033[32m    |\033[m')
    print ('\033[32m            |\033[m\033[32m •••••••••••••••••••••••••\033[32m |\033[m')
    print ('\033[32m            | [ 2 ] Descobrir o IP    \033[32m  |\033[m')
    print ('\033[32m            |\033[m\033[32m •••••••••••••••••••••••••\033[m \033[32m|\033[m')
    print ('\033[32m             •••••••••••••••••••••••••••\033[m')
    print (' ')
    return int(input('\033[33m[AndressIP]~> \033[m'))

while True:

      opção = menu()

      if opção == 1:
         os.system('clear')
         os.system('clear')
         print ('\033[32mAté Logo, volte sempre...\033[m')
         break;

      elif opção == 2:
           print (' ')
           print ('\033[32m=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~\033[m')
           print (' ')
           print ('\033[36m-------> Não use HTTP nem WWW <-------\033[m')
           print (' ')
           dominio = str(input('\033[33mDigite o Site | Domínio > \033[m'))
           print (' ')
           print ('\033[36m-------> Não use HTTP nem WWW <-------\033[m')
           print (' ')
           print ('\033[32m=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~\033[m')
           print (' ')
           get_ip(dominio, dominio)

      elif opção == 3:
           print (' ')
           print ('\033[32m=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\033[m')
           print (' ')
           print ('\033[32mPor favor, não deixe o seu teclado aberto, para o uso correto do Script\033[m')
           print (' ')
           print ('\033[32m=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\033[m')
           os.system('sleep 3')
      else:
           print (' ')
           print ('\033[32m=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~\033[m')
           print (' ')
           print ('\033[32mOpção inválida! Escolha entre 1 - 2 - 3. :(')
           os.system('sleep 3')
           os.system('clear')
