# Exercício 3:
#  Agora vamos tanto explorar o hardware que estamos utilizando quanto aprender
# algo interessante: enviar programaticamente comandos para o shell. Crie um
# script chamado resources.py e utilize-o para exibir no console as
# informações solicitadas abaixo. Para isso, utilize o método check_output do
# módulo subprocess do Python 😎.

#  Informações sobre a sua CPU (no Linux você pode usar comando lscpu, e no OSX
#  você pode usar o comando sysctl -n machdep.cpu.brand_string):

# O modelo;
# A quantidade de cores;
# A velocidade em Megahertz - MHz;
# A quantidade de cache (L1, L2, L3).
#  Informações sobre a memória RAM (no Linux você pode usar comando free, e no
# OSX você pode usar o comando top -l 1 | head -n 10 | grep PhysMem):
#  A quantidade total de memória RAM disponível em sua máquina em
# megabytes - MB (faça a conversão também 😉).
# A quantidade total de memória RAM que está sendo utilizada em megabytes - MB.

# dica:
#  O método decode("UTF-8") vai ser útil para ler os dados oriundos da
# check_output;
#  Os métodos split e strip vão ser úteis para limpar e separar as informações
# obtidas com os comandos;
# O método startswith vai ser útil para selecionar informações específicas.
#  Se estiver muito difícil fazer a filtragem e limpeza dos dados, se contente
# com a exibição de informações a mais 😉

from subprocess import check_output

# Processador
cpu_information = check_output("lscpu").decode("UTF-8").split("\n")
desired_cpu_information = {
    "model name": "Modelo",
    "cpu(s)": "Cores",
    "cpu mhz": "Velocidade (MHz)",
    "l1d": "Cache L1d",
    "l1i": "Cache L1i",
    "l2": "Cache L2",
    "l3": "Cache L3",
}
for desired_name, desired_description in desired_cpu_information.items():
    for information in cpu_information:
        if information.lower().startswith(desired_name):
            information = information.split("  ")  # 2 blank spaces
            information = information[-1].strip()
            print(f"{desired_description}: {information}")

# Memória
memory_information = [
    information
    for information in check_output("free")
    .decode("UTF-8")
    .split("\n")[1]
    .split(" ")
    if information != ""
]
total_memory = int(memory_information[1]) / 1000
used_memory = int(memory_information[2]) / 1000
print(
    f"Memória total: {total_memory:.0f}MB\n"
    f"Memória utilizada: {used_memory:.0f}MB"
)
