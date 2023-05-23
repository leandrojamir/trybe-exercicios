# Exercício 5
#  A gerência do seu setor quer fazer um trabalho para aumentar a média de
# audiência nos países da confederação UEFA, porém ainda não se sabe qual a
# média atual. Mostre a média de audiência dos países que fazem parte da
# confederação UEFA e limite em duas casas decimais.

import pandas as pd


df = pd.read_csv("fifa_audience.csv")

uefa_countries = df[df["confederation"] == "UEFA"]

audience_average = uefa_countries["tv_audience_share"].mean()

print(audience_average)
