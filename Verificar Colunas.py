import pandas as pd

# Ler o arquivo Excel do gabarito
gabarito_df = pd.read_excel("Dia 1.xlsx")

# Exibir as colunas presentes no DataFrame do gabarito
print(gabarito_df.columns)

# Ler o arquivo Excel do gabarito
gabarito_ff = pd.read_excel("Gabarito - Dia 1.xlsx")

# Exibir as colunas presentes no DataFrame do gabarito
print(gabarito_ff.columns)

print(gabarito_df.info())
print(gabarito_ff.info())