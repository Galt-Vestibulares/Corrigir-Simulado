import pandas as pd

# Função para verificar se uma resposta está correta
def verificar_resposta(resposta_aluno, gabarito):
    if resposta_aluno == gabarito:
        return 1
    else:
        return 0

# Corrigir questões de língua estrangeira (Dia 1)
def corrigir_lingua_estrangeira(dia1_df, gabarito_df):
    resultado_df = pd.DataFrame(columns=colunas_resultado)
    questoes_lingua_estrangeira = [f"{i}I" for i in range(1, 6)]

    for index, row in dia1_df.iterrows():
        matricula = row["Qual seu número de matrícula?"]
        resposta_aluno = row["Item 1I":"Item 90"].values.tolist()
        tema = "Linguagens Códigos e suas Tecnologias"
        subtema = "Interpretação de texto"

        opcao = row["Qual sua opção de língua estrangeira?"]
        if opcao.lower() == "inglês":
            prova = "Inglês"
            gabarito_questoes = questoes_lingua_estrangeira
        elif opcao.lower() == "espanhol":
            prova = "Espanhol"
            gabarito_questoes = questoes_lingua_estrangeira
        else:
            gabarito_questoes = [f"Item {i}" for i in range(6, 91)]

        for i, gabarito_questao in enumerate(gabarito_questoes):
            resposta = resposta_aluno[i]
            if gabarito_questao in questoes_lingua_estrangeira:
                gabarito = gabarito_df.loc[gabarito_df["Questão"] == gabarito_questao]["Gabarito"].values
            else:
                col_index = gabarito_questoes.index(gabarito_questao) + 1
                gabarito = gabarito_df.iloc[:, col_index].values
            if len(gabarito) > 0:
                resultado = verificar_resposta(resposta, gabarito[0])
                resultado_df.loc[len(resultado_df)] = [matricula, resposta, gabarito_questao,
                                                       gabarito[0], tema, subtema, prova, resultado, 1 - resultado]
    
    return resultado_df


# Corrigir questões de 6 a 90 (Dia 1)
def corrigir_questoes_6_a_90(dia1_df, gabarito_df):
    resultado_df = pd.DataFrame(columns=colunas_resultado)

    for index, row in dia1_df.iterrows():
        matricula = row["Qual seu número de matrícula?"]
        resposta_aluno = row["Item 6":"Item 90"].values.tolist()

        for i in range(6, 91):
            resposta = resposta_aluno[i - 6]
            gabarito_row = gabarito_df.loc[gabarito_df["Questão"] == i]

            if not gabarito_row.empty:
                gabarito = gabarito_row["Gabarito"].values[0]
                tema = gabarito_row["Tema"].values[0]
                subtema = gabarito_row["Subtema"].values[0]

                if "Prova" in gabarito_df.columns:
                    prova = gabarito_row["Prova"].values[0]
                else:
                    prova = ""

                resultado = verificar_resposta(resposta, gabarito)
                resultado_df.loc[len(resultado_df)] = [matricula, resposta, i, gabarito, tema, subtema, prova, resultado, 1 - resultado]
            else:
                print(f"Gabarito para a questão {i} não encontrado.")

    return resultado_df


# Ler os arquivos Excel (Dia 1 e Gabarito)
dia1_df = pd.read_excel("Dia 1.xlsx")
gabarito_df = pd.read_excel("Gabarito - Dia 1.xlsx")

# Definir colunas do resultado final
colunas_resultado = ["Matrícula", "Resposta", "Questão",
                     "Gabarito", "Tema", "Subtema", "Prova", "vl_certo", "vl_errado"]

# Corrigir questões de língua estrangeira (Dia 1)
resultado_lingua_estrangeira = corrigir_lingua_estrangeira(dia1_df, gabarito_df)

# Corrigir questões de 6 a 90 (Dia 1)
resultado_questoes_6_a_90 = corrigir_questoes_6_a_90(dia1_df, gabarito_df)

# Concatenar os resultados
resultado_final = pd.concat([resultado_lingua_estrangeira, resultado_questoes_6_a_90])

# Salvar o resultado final em um único arquivo Excel
resultado_final.to_excel("Resultado Dia 1.xlsx", index=False)
