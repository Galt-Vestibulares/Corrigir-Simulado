#Feito por Lucas Heler(Akaeboshi), em algum dia de junho de 2023
#Qualquer duvidas só mandar mensagem, mesmo se eu tiver saido do Galt - 61 991152252

import pandas as pd

# Função para verificar se uma resposta está correta
def verificar_resposta(resposta_aluno, gabarito):
    """
    Verifica se a resposta do aluno está correta.
    :param resposta_aluno: Resposta do aluno
    :param gabarito: Gabarito da questão
    :return: 1 se a resposta está correta, 0 caso contrário
    """
    if resposta_aluno == gabarito:
        return 1
    else:
        return 0


# Ler os arquivos Excel (Dia 2 e Gabarito)
dia2_df = pd.read_excel("Dia 2.xlsx")
gabarito_df = pd.read_excel("Gabarito - Dia 2.xlsx")

# Definir colunas do resultado final
colunas_resultado = ["Matrícula", "Resposta", "Questão",
                     "Gabarito", "Tema", "Subtema", "Prova", "vl_certo", "vl_errado"]
resultado_df = pd.DataFrame(columns=colunas_resultado)

# Percorre cada linha do DataFrame "dia2_df"
for index, row in dia2_df.iterrows():
    # Extrai a matrícula do aluno da coluna "Qual seu número de matrícula?"
    matricula = row["Qual seu número de matrícula?"]
    
    # Cria uma lista com as respostas do aluno para as questões de 91 a 180 (Item 91 a Item 180)
    resposta_aluno = row["Item 91":"Item 180"].values.tolist()

    # Percorre as questões do aluno de 91 a 180
    for i in range(91, 181):
        resposta = resposta_aluno[i - 91]
        
        # Obtém a linha correspondente ao gabarito da questão
        gabarito_row = gabarito_df.loc[gabarito_df["Questão"] == i]

        if not gabarito_row.empty:
            # Extrai as informações do gabarito
            gabarito = gabarito_row["Gabarito"].values[0]
            tema = gabarito_row["Tema"].values[0]
            subtema = gabarito_row["Subtema"].values[0]

            if "Prova" in gabarito_df.columns:
                prova = gabarito_row["Prova"].values[0]
            else:
                prova = ""

            # Verifica se a resposta está correta comparando com o gabarito
            resultado = verificar_resposta(resposta, gabarito)
            
            # Adiciona os resultados ao DataFrame final
            resultado_df.loc[len(resultado_df)] = [matricula, resposta, i, gabarito, tema, subtema, prova, resultado, 1 - resultado]
        else:
            print(f"Gabarito para a questão {i} não encontrado.")

# Salvar o resultado final em um único arquivo Excel
resultado_df.to_excel("Resultado Dia 2.xlsx", index=False)
