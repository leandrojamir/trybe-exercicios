# Exercício 1
#  Sua liderança gostaria de ter uma visão geral sobre as informações contidas
# na base de dados fifa_audience.

import pandas as pd


df = pd.read_csv("fifa_audience.csv")

print(df.info())
