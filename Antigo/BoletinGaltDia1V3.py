import pandas as pd

# Carregar os DataFrames das respostas e do gabarito
respostas_df = pd.read_excel("Dia 1.xlsx")
gabarito_df = pd.read_excel("Gabarito - Dia 1.xlsx")

# Selecionar as colunas correspondentes às respostas e ao gabarito
respostas_colunas = ["Item 1I", "Item 2I", "Item 3I", "Item 4I",
                     "Item 5I", "Item 1E", "Item 2E", "Item 3E", "Item 4E", "Item 5E"]
gabarito_colunas = ["1I", "2I", "3I", "4I", "5I", "1E", "2E", "3E", "4E", "5E"]

# Criar um DataFrame para armazenar as respostas corrigidas
respostas_corrigidas = pd.DataFrame()

# Percorrer as colunas das respostas e do gabarito
for respostas_col, gabarito_col in zip(respostas_colunas, gabarito_colunas):
    # Obter o gabarito da questão atual
    gabarito = gabarito_df.loc[gabarito_df["Questão"]
                               == gabarito_col, "Gabarito"].values[0]

    # Verificar se a resposta está correta
    respostas_corrigidas[respostas_col] = respostas_df[respostas_col] == gabarito

# Salvar as respostas corrigidas em um novo arquivo
respostas_corrigidas.to_excel("Respostas_Corrigidas.xlsx", index=False)
