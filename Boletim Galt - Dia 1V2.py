import pandas as pd

# Função para verificar se uma resposta está correta
def verificar_resposta(resposta_aluno, gabarito):
    """
    Verifica se a resposta do aluno está correta, comparando com o gabarito.
    :param resposta_aluno: Resposta fornecida pelo aluno
    :param gabarito: Gabarito da questão
    :return: 1 se a resposta estiver correta, 0 caso contrário
    """
    if resposta_aluno == gabarito:
        return 1
    else:
        return 0

# Corrigir questões de língua estrangeira (Dia 1)
def corrigir_lingua_estrangeira(dia1_df, gabarito_df):
    resultado_df = pd.DataFrame(columns=colunas_resultado)
    questoes_lingua_estrangeira = [f"Item {i}I" for i in range(1, 6)]

    for index, row in dia1_df.iterrows():
        matricula = row["Qual seu número de matrícula?"]
        turma = row["Qual sua turma?"]
        resposta_aluno = row["Item 1I":"Item 90"].values.tolist()
        opcao = row["Qual sua opção de língua estrangeira?"]

        prova = ""
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
                # Obtém o gabarito da questão de língua estrangeira
                gabarito_row = gabarito_df.loc[gabarito_df["Questão"] == gabarito_questao]
                gabarito = gabarito_row["Gabarito"].values[0] if not gabarito_row.empty else ""
            else:
                # Obtém o gabarito das outras questões
                col_index = gabarito_questoes.index(gabarito_questao) + 1
                gabarito = gabarito_df.iloc[:, col_index].values[0] if col_index < len(gabarito_df.columns) else ""

            resultado = verificar_resposta(resposta, gabarito)
            resultado_df.loc[len(resultado_df)] = [matricula, resposta, gabarito_questao,
                                        gabarito, turma, prova, '', resultado, 1 - resultado]
    
    return resultado_df


# Corrigir questões de 6 a 90 (Dia 1)
def corrigir_questoes_6_a_90(dia1_df, gabarito_df):
    """
    Corrige as questões de 6 a 90 do Dia 1.
    :param dia1_df: DataFrame com as respostas dos alunos
    :param gabarito_df: DataFrame com o gabarito das questões
    :return: DataFrame com os resultados da correção
    """
    resultado_df = pd.DataFrame(columns=colunas_resultado)

    # Percorre cada linha do DataFrame "dia1_df"
    for index, row in dia1_df.iterrows():
        # Extrai a matrícula do aluno da coluna "Qual seu número de matrícula?"
        matricula = row["Qual seu número de matrícula?"]

        # Cria uma lista com as respostas do aluno para as questões de 6 a 90 (Item 6 a Item 90)
        resposta_aluno = row["Item 6":"Item 90"].values.tolist()

        # Percorre as questões do aluno de 6 a 90
        for i in range(6, 91):
            resposta = resposta_aluno[i - 6]
        
            # Obtém a linha correspondente ao gabarito da questão
            gabarito_row = gabarito_df.loc[gabarito_df["Questão"] == i]

            if not gabarito_row.empty:
                # Extrai as informações do gabarito
                gabarito = gabarito_row["Gabarito"].values[0]
                tema = gabarito_row["Tema"].values[0]

                # Verifica se a resposta está correta comparando com o gabarito
                resultado = verificar_resposta(resposta, gabarito)
                
                # Adiciona os resultados ao DataFrame final
                resultado_df.loc[len(resultado_df)] = [matricula, resposta, i, gabarito, tema, '', '', resultado, 1 - resultado]

    return resultado_df


# Ler os arquivos Excel (Dia 1 e Gabarito)
dia1_df = pd.read_excel("Dia 1.xlsx")
gabarito_df = pd.read_excel("Gabarito - Dia 1.xlsx")

# Definir colunas do resultado final
colunas_resultado = ["Matrícula", "Resposta", "Questão",
                     "Gabarito", "Tema", "Turma", "Prova", "vl_certo", "vl_errado"]

# Corrigir questões de língua estrangeira (Dia 1)
resultado_lingua_estrangeira = corrigir_lingua_estrangeira(dia1_df, gabarito_df)

# Corrigir questões de 6 a 90 (Dia 1)
resultado_questoes_6_a_90 = corrigir_questoes_6_a_90(dia1_df, gabarito_df)

# Concatenar os resultados
resultado_final = pd.concat([resultado_lingua_estrangeira, resultado_questoes_6_a_90], ignore_index=True)

# Salvar o resultado final em um único arquivo Excel
resultado_final.to_excel("Resultado Dia 1.xlsx", index=False)
