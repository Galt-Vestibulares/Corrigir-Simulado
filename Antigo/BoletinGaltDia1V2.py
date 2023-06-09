import pandas as pd

# Função para verificar se uma resposta está correta


def verificar_resposta(resposta_aluno, gabarito):
    if resposta_aluno == gabarito:
        return 1
    else:
        return 0


# Ler os arquivos Excel (Dia 1 e Gabarito)
dia1_df = pd.read_excel("Dia 1.xlsx")
gabarito_df = pd.read_excel("Gabarito.xlsx")

# Definir colunas do resultado final
colunas_resultado = ["Matrícula", "Resposta", "Questão",
                     "Gabarito", "Tema", "Subtema", "Prova", "vl_certo", "vl_errado"]
resultado_df = pd.DataFrame(columns=colunas_resultado)

# Questões de língua estrangeira (1 a 5)
questoes_lingua_estrangeira = [f"{i}I" for i in range(1, 6)]

# Questões do Dia 1 (6 a 90)
questoes_dia1 = [f"Item {i}" for i in range(6, 91)]

# Iterar sobre cada linha do DataFrame do Dia 1
for index, row in dia1_df.iterrows():
    matricula = row["Qual seu número de matrícula?"]
    # Todas as respostas do aluno
    resposta_aluno = row["Item 6":"Item 90"].values.tolist()
    tema = "Definir o tema do Dia 1"  # Substituir pelo tema correto
    subtema = "Definir o subtema do Dia 1"  # Substituir pelo subtema correto
    prova = "Definir a prova do Dia 1"  # Substituir pela prova correto

    # Iterar sobre as questões e comparar com o gabarito
    for i, gabarito_questao in enumerate(questoes_dia1):
        resposta = resposta_aluno[i]
        gabarito = gabarito_df.loc[gabarito_df["Questão"]
                                   == gabarito_questao]["Gabarito"].values
        if len(gabarito) > 0:
            resultado = verificar_resposta(resposta, gabarito[0])
            resultado_df.loc[len(resultado_df)] = [matricula, resposta, gabarito_questao,
                                                   gabarito[0], tema, subtema, prova, resultado, 1 - resultado]

# Salvar o resultado em um novo arquivo Excel
resultado_df.to_excel("Resultado_Dia1.xlsx", index=False)
