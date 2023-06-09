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

    for i in range(91, 181):
        resposta = resposta_aluno[i - 91]
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
            resultado_df.loc[len(resultado_df)] = [
                matricula, resposta, i, gabarito, tema, subtema, prova, resultado, 1 - resultado]
        else:
            print(f"Gabarito para a questão {i} não encontrado.")

resultado_df.to_excel("Resultado Dia 2.xlsx", index=False)
