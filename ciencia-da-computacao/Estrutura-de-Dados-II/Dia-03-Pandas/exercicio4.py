# Exercício 4
#  O departamento comercial de sua empresa quer fazer um trabalho especial nos
# países que fazem parte da confederação CONMEBOL, portanto mostre na tela
# quais são eles.

import pandas as pd


df = pd.read_csv("fifa_audience.csv")

conmebol_countries = df.loc[df["confederation"] == "CONMEBOL"]

print(conmebol_countries)
