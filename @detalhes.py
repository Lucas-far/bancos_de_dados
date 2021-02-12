

"""
Módulo: @detalhes.py
Palavra chave: detalhes
Objetivo: registrar em um arquivo separado, dados já mencionados em aula, que podem ser relevantes
"""

def aulas_13_para_16():
    """
    1 - Tabelas não devem possuir campos nulos, caso contrário, é uma tabela problemática
    2 - 1FN -> Em uma tabela, campos não devem conter valores múltiplos (multivalorados)
    3 - 2FN -> Em uma tabela, todos os CAMPOS NÃO CHAVE devem ser dependentes do CAMPO CHAVE
    4 - 3FN -> Em uma tabela, nenhum CAMPO NÃO CHAVE pode depender de outro(s) CAMPO NÃO CHAVE
    """


# 21. Exemplo passo a passo Modelagem de Dados
def aula_21():
    """
    - Algo importante para mim é mencionado em 29:20
    - Há uma comparação entre 4 entidades relacionadas, e ao explicar sobre 2FN, é mostrado uma abordagem prática
    - Qual foi a lógica entendiada por mim?

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ um modelo deve ter campos que precisa ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - EXEMPLO:
    - MODELO: [ clientes ]

            id          INT PK AI
            nome        VARCHAR(150) NN
            cpf         VARCHAR(14) NN
            telefone    VARCHAR(15) NN
            estado      VARCHAR(2) NN
            cidade      VARCHAR(150) NN
            bairro      VARCHAR(150) NN
            rua         VARCHAR(150) NN
            numero_casa INT NN

    - um cliente é uma pessoa
    - uma pessoa precisa de um (id, nome, cpf, telefone, estado, cidade, bairro, rua, numero_casa)?

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ANÁLISE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    - uma pessoa precisa de um [ id ], por serem infinitos e, em programação podem ser programados para não repetir
    - uma pessoa precisa de um [ nome ], pois qualquer ser precisa de uma nomemclatura no mundo
    - uma pessoa precisa de um [ cpf ], para pode ser um cidadão visto pelo governo
    - uma pessoa precisa de um [ telefone ], para poder falar com pessoas de forma remota
    - uma pessoa precisa de um [ estado ], para ter um identificador local do país onde esta localiza-se
    - uma pessoa precisa de uma [ cidade ], para ter um identificador local do estado onde esta localiza-se
    - uma pessoa precisa de uma [ bairro ], para ter um identificador local do cidade onde esta localiza-se
    - uma pessoa precisa de uma [ rua ], para ter um identificador local do bairro onde esta localiza-se
    - uma pessoa precisa de um [ numero_casa ], para ter um identificador local na rua onde esta localiza-se
    """


def aula_26():
    """
    SQL é dividido em subgrupos: DCL DDL DML DQL DTL

    - DCL = Control      (aula 30)
    - DDL = Definititon  (aula 29)
    - DML = Manipulation (aula 28) INSERT INTO VALUES / UPDATE WHERE / DELETE FROM
    - DQL = Query        (aula 27) SELECT FROM / SELECT FROM AS
    - DTL = Transaction  (aula 31)
    """
