import pandas as pd

Dia1 = pd.read_excel("Dia 1.xlsx")
# Dia2=pd.read_excel("Dia 2.xlsx")
Gabarito = pd.read_excel("Gabarito.xlsx")


def FUNCAO1(Dia1):
    if (Dia1["Qual sua opção de língua estrangeira?"] == 'Espanhol'):
        return 'E'
    elif (Dia1["Qual sua opção de língua estrangeira?"] == 'Inglês'):
        return 'I'


Dia1['Sigla'] = Dia1.apply(FUNCAO1, axis=1)

Evento = "1° Simulado Vest - 2/2020"

x = 1
a = 1

while x < 31:
    df = Dia1.loc[Dia1['Qual sua opção de língua estrangeira?'] == 'Inglês']

    Planilha = pd.read_excel("Dia 1_Compilado.xlsx")

    y = str(x)

    y = y + 'I'

    z = 'Item ' + y

    z = str(z)

    df = df.loc[:, ['Qual seu número de matrícula?', z]]

    df['Questão'] = y

    Gab = Gabarito.loc[Gabarito['Questão'] == y]

    Gab = Gab.reset_index()

    b = Gab['Gabarito'].iloc[0]

    b = str(b)

    c = Gab['Tema'].iloc[0]

    c = str(c)

    d = Gab['Subtema'].iloc[0]

    d = str(d)

    df['Gabarito'] = b

    df['Tema'] = c

    df['Subtema'] = d

    df['Prova'] = 'Linguagens Códigos e suas Tecnologias - Língua Inglesa'

    df.columns = ['Matrícula', 'Resposta', 'Questão',
                  'Gabarito', 'Tema', 'Subtema', 'Prova']

    def FUNCAO3(df):
        if (df["Resposta"] == df['Gabarito']):
            return 1
        else:
            return 0

    df['vl_certo'] = df.apply(FUNCAO3, axis=1)

    def FUNCAO4(df):
        if (df["Resposta"] == df['Gabarito']):
            return 0
        else:
            return -1

    df['vl_errado'] = df.apply(FUNCAO4, axis=1)

    df['Evento'] = Evento

    df.columns = ['Matrícula', 'Resposta', 'Questão', 'Gabarito',
                  'Tema', 'Subtema', 'Prova', 'vl_certo', 'vl_errado', 'Evento']

    Final = pd.concat([Planilha, df])

    Final = Final.loc[:, ['Matrícula', 'Resposta', 'Questão', 'Gabarito',
                          'Tema', 'Subtema', 'Prova', 'vl_certo', 'vl_errado', 'Evento']]

    Final.to_excel("Dia 1_Compilado.xlsx")

    x = x+1

while a < 31:
    df2 = Dia1.loc[Dia1['Qual sua opção de língua estrangeira?'] == 'Espanhol']

    Planilha = pd.read_excel("Dia 1_Compilado.xlsx")

    y = str(a)

    y = y + 'E'

    z = 'Item ' + y

    z = str(z)

    df2 = df2.loc[:, ['Qual seu número de matrícula?', z]]

    df2['Questão'] = y

    Gab = Gabarito.loc[Gabarito['Questão'] == y]

    Gab = Gab.reset_index()

    b = Gab['Gabarito'].iloc[0]

    b = str(b)

    c = Gab['Tema'].iloc[0]

    c = str(c)

    d = Gab['Subtema'].iloc[0]

    d = str(d)

    df2['Gabarito'] = b

    df2['Tema'] = c

    df2['Subtema'] = d

    df2['Prova'] = 'Linguagens Códigos e suas Tecnologias - Língua Espanhola'

    df2.columns = ['Matrícula', 'Resposta', 'Questão',
                   'Gabarito', 'Tema', 'Subtema', 'Prova']

    def FUNCAO3(df2):
        if (df2["Resposta"] == df2['Gabarito']):
            return 1
        else:
            return 0

    df2['vl_certo'] = df2.apply(FUNCAO3, axis=1)

    def FUNCAO4(df2):
        if (df2["Resposta"] == df2['Gabarito']):
            return 0
        else:
            return -1

    df2['vl_errado'] = df2.apply(FUNCAO4, axis=1)

    df2['Evento'] = Evento

    df2.columns = ['Matrícula', 'Resposta', 'Questão', 'Gabarito',
                   'Tema', 'Subtema', 'Prova', 'vl_certo', 'vl_errado', 'Evento']

    Final = pd.concat([Planilha, df2])

    Final = Final.loc[:, ['Matrícula', 'Resposta', 'Questão', 'Gabarito',
                          'Tema', 'Subtema', 'Prova', 'vl_certo', 'vl_errado', 'Evento']]

    Final.to_excel("Dia 1_Compilado.xlsx")

    a = a+1

while x > 30 and x < 151:

    Planilha = pd.read_excel("Dia 1_Compilado.xlsx")

    print(x)

    y = str(x)

    z = 'Item ' + y

    df = Dia1.loc[:, ['Qual seu número de matrícula?', z]]

    df['Questão'] = y

    Gabarito['Questão'] = Gabarito['Questão'].astype(str)

    Gab = Gabarito.loc[Gabarito['Questão'] == y]

    Gab = Gab.reset_index()

    b = Gab['Gabarito'].iloc[0]

    b = str(b)

    c = Gab['Tema'].iloc[0]

    c = str(c)

    d = Gab['Subtema'].iloc[0]

    d = str(d)

    df['Gabarito'] = b

    df['Tema'] = c

    df['Subtema'] = d

    df['Prova'] = ''

    df.columns = ['Matrícula', 'Resposta', 'Questão',
                  'Gabarito', 'Tema', 'Subtema', 'Prova']

    def FUNCAO3(df):
        if (df["Resposta"] == df['Gabarito']):
            return 1
        else:
            return 0

    df['vl_certo'] = df.apply(FUNCAO3, axis=1)

    def FUNCAO4(df):
        if (df["Resposta"] == df['Gabarito']):
            return 0
        else:
            return -1

    df['vl_errado'] = df.apply(FUNCAO4, axis=1)

    df['Evento'] = Evento

    df.columns = ['Matrícula', 'Resposta', 'Questão', 'Gabarito',
                  'Tema', 'Subtema', 'Prova', 'vl_certo', 'vl_errado', 'Evento']

    Final = pd.concat([Planilha, df])

    Final = Final.loc[:, ['Matrícula', 'Resposta', 'Questão', 'Gabarito',
                          'Tema', 'Subtema', 'Prova', 'vl_certo', 'vl_errado', 'Evento']]

    Final.to_excel("Dia 1_Compilado.xlsx")

    x = x+1
