# Exercício 2
#  Com a finalidade de ter a visibilidade dos países com maior participação no
# compartilhamento global de transmissões, mostre na tela apenas os países com
# porcentagem de compartilhamento global (population_share) maior que 2.

import pandas as pd


df = pd.read_csv("fifa_audience.csv")

#  Aqui armazenamos a condicional com os países que possuem uma porcentagem de
# compartilhamento global maior que 2
global_share_greater_2 = df["population_share"] > 2
#  Se você fizer um print aqui, verá que as linhas na coluna
# "population_share" estarão marcadas como True ou False, que são referentes à
# comparação entre a porcentagem do país e o valor "> 2"

#  Se aplicarmos essa série de Booleanos como índice do DataFrame, apenas as
# linhas marcadas como True serão selecionadas e mostradas.
result = df[global_share_greater_2]

print(result)
