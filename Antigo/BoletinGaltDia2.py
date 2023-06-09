import pandas as pd


def verificar_resposta(resposta_aluno, gabarito):
    if resposta_aluno == gabarito:
        return 1
    else:
        return 0


dia2_df = pd.read_excel("Dia 2.xlsx")
gabarito_df = pd.read_excel("Gabarito.xlsx")

colunas_resultado = ["Matrícula", "Resposta", "Questão",
                     "Gabarito", "Tema", "Subtema", "Prova", "vl_certo", "vl_errado"]
resultado_df = pd.DataFrame(columns=colunas_resultado)

for index, row in dia2_df.iterrows():
    matricula = row["Qual seu número de matrícula?"]
    resposta_aluno = row["Item 91":"Item 180"].values.tolist()
    tema = ""
    subtema = ""
    prova = ""

    for i in range(91, 181):
        resposta = resposta_aluno[i - 91]
        gabarito = gabarito_df.loc[gabarito_df["Questão"]
                                   == i]["Gabarito"].values
        if len(gabarito) > 0:
            resultado = verificar_resposta(resposta, gabarito[0])
            resultado_df.loc[len(resultado_df)] = [
                matricula, resposta, i, gabarito[0], tema, subtema, prova, resultado, 1 - resultado]
        else:
            print(f"Gabarito para a questão {i} não encontrado.")

resultado_df.to_excel("Resultado_Dia2.xlsx", index=False)
