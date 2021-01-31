

"""
Módulo: aula_21.py
Palavra chave:

Curso || Bancos de Dados SQL e NoSQL do básico ao avançado
Local || Seção 3:Modelagem de Dados
Aula  || 21. Exemplo passo a passo Modelagem de Dados
"""

"modelo"  # clientes
"OBS"     # eu acho que os campos de cidade para baixo, quebram a 2FN
def parte_1():
    """
    id          INT PK AI
    nome        VARCHAR(150) NN
    cpf         VARCHAR(14) NN
    telefone    VARCHAR(15) NN
    estado      VARCHAR(2) NN
    cidade      VARCHAR(150) NN
    rua         VARCHAR(150) NN
    bairro      VARCHAR(150) NN
    numero_casa INT NN

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ver arquivo [ @detalhes.py ], em [ def aula_21 ] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

"modelo"  # produtos
def parte_2():
    """
    id            INT PK AI
    descriminacao VARCHAR(200)
    valor_unidade DECIMAL(7,2)

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ANÁLISE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    um produto precisa de um [ id ], numérico, não repetível e incrementável, para representá-lo
    um produto precisa de uma [ descriminacao ], pois tudo que existe, ou não, fisicamente, deve ter um nome
    um produto precisa de um [ valor_unidade ], pois tudo pode ser vendido ou trocado
    """

"modelo"  # notas_fiscais
"OBS"     # id_cliente -> FK -> clientes/id
def parte_3():
    """
    id            INT PK AI
    id_cliente    INT NN
    data_envio    DATE NN
    valor         DECIMAL(7,2)

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ANÁLISE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    uma nota fiscal precisa de um [ id ], numérico, não repetível e incrementável, para representá-la
    uma nota fiscal precisa de um [ id_cliente ], pois pessoas compram, e geram uma nota fiscal
    uma nota fiscal precisa de uma [ data_envio ], para organizar quando está foi gerada
    uma nota fiscal precisa de um [ valor ], pois precisa-se saber quanto custou o total de uma compra

    OBS: [ id_cliente ] já existe no modelo [ clientes ], portanto, [ id_cliente ] aqui, herda do modelo mencionado
    """

"modelo"  # produtos_nota_fiscal
"OBS"     # id_nota_fiscal -> FK -> notas_fiscais/id
"OBS"     # id_produto -> FK -> produtos/id
def parte_4():
    """
    id             INT PK AI (representa cada resultado de contagem de produtos da cada nota fiscal diferente)
    id_nota_fiscal INT NN
    id_produto     INT NN
    quantidade     INT NN

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ANÁLISE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    para contar produtos numa nota fiscal, é preciso um [ id ] para separar cada nota fiscal contada, de forma separada
    para contar produtos numa nota fiscal, é preciso um [ id_nota_fiscal ], para dar um identificador à nota fiscal
    para contar produtos numa nota fiscal, é preciso um [ id_produto ], pois os produtos são os validadores
    para contar produtos numa nota fiscal, é preciso uma [ quantidade ], pois este é o contador
    """
