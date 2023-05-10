# Exercício 5:
#  Faça um script que exibe o seu respectivo process id utilizando o módulo os
# do Python e então fique em execução por um determinado tempo. Agora
# utilizando os comandos de monitoramento visto no conteúdo, exiba os
# processos em execução e então identifique o seu processo.

from time import sleep
from os import getpid


print(getpid())
sleep(20)

# jamir@jamir-X550CA:~/trybe-exercicios/ciencia-da-computacao/
# Estrutura-de-Dados/Dia-01-Arquitetura-de-Computadores$ python3 exercicio5.py
# 11087

# jamir@jamir-X550CA:~$ ps aux | grep 11087
# jamir      11087  0.1  0.0  18784  7652 pts/0
# S+   19:15   0:00 python3 exercicio5.py
# jamir      11092  0.0  0.0   9104  2356 pts/1
# S+   19:15   0:00 grep --color=auto 11087
# jamir@jamir-X550CA:~$ 
