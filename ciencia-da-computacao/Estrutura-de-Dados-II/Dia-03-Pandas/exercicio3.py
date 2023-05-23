# Exercício 3
#  Uma pessoa da equipe ficou curiosa sobre a quantidade de países em cada
# confederação, portanto mostre a ela essa informação.

#  Dica: caso queira renomear o nome da coluna que conterá a contagem dos
# países, você utilizar o método reset_index().

import pandas as pd


df = pd.read_csv("fifa_audience.csv")

#  Para contar os países por confederação usamos o método
# count() e reset_index() para dar um nome à coluna que mostra a contagem.
count_countries_by_confederation = (
    df.groupby("confederation")["country"].count().reset_index(name="count")
)

print(count_countries_by_confederation)
