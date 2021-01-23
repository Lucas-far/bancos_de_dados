

"""
Módulo: aula_20.py
Palavra chave:

Curso || Bancos de Dados SQL e NoSQL do básico ao avançado
Local || Seção 3:Modelagem de Dados
Aula  || 20. MER - Modelo Entidade Relacionamento
"""

# Mapa desta aula
def parte1():
    """
    - Criar um modelo
    - Dar nome ao modelo (== nome do bdd)
    - Salvar o modelo
    - Criar tabelas (entidades)
    - Criar campos nas tabelas (atributos)
    - Selecionar os tipos de dados para os atributos
    - Definir chave primária (primary key, pk)
    - Definir chave estrangeira (foreign ket, fk, relacionamentos)
    - Exportar o diagrama (imagem ou pdf)
    """

# Criar um modelo
def parte2():
    """
    1 - Abrir o MySQL Workbench
    2 - Menu lateral esquerdo [ models ] (ícone = imagem de tabelas conectadas) CLICAR 1X
    3 - Botão [ + ] CLICAR 1X
    4 - Procurar [ Physical Schemas ] [ mydb ] CLICAR 2X
    5 - Modificar input [ schema name ] para [ teste ]
    6 - Salvar (ícone = disquete) (local = canto superior esquerdo, abaixo do menu textual)

    OBS: Como o modelo está sendo criado, o salvar apenas salva o arquivo, não salva modificações
    OBS: Nome do arquivo == item 5
    OBS: Formato == nome_dado.mwb
    """

# Criar um diagrama (a partir desse momento, salvar todas as alterações feitas)
"OBS"  # Como salvar? método [ parte2 ] item 6
def parte3():
    """
    1 - Depois de salvar o modelo, deve-se criar um diagrama dele
    2 - Procurar por [ + add diagram ] no topo da tela CLICAR 2X

    OBS: Há dois retângulos no canto superior direito do diagrama
    OBS: O da esquerda, fecha os menus laterais à esquerda
    OBS: O da direita, fecha os menus laterais à direita
    """

# Criar uma tabela = [ funcionarios ] (regras de nome == vars em python)
def parte4():
    """
    1 - Na tela do diagrama, escolher a opção [ place a new table ] [ ícone 7 ] [ atalho = T ]
    2 - Clicar no DESKTOP (tela branca), e a tabela surge

    OBS: A tabela também torna-se disponível no canto esquerdo, na área [ navigator ]

    3 - Selecionar a tabela no DESKTOP (CLICAR 2X) e na opção [ Name = funcionarios ] (SALVAR)
    """

# Criação de campos da tabela = [ funcionarios ]
"OBS"  # Traços significam o momento específico da criação dos campos
def parte5():
    """
    1 - Qualquer tabela selecionada no DESKTOP, têm opções acessíveis por (DUPLO CLIQUE)

    OPÇÕES: table, columns, indexes, foreign keys, triggers, partitioning, options, inserts, privileges

    OBS: No OS Linux, as opções ficam logo abaixo da tela DESKTOP
    OBS: No OS Windows, as opções ficam na parte mais inferior da tela do software

    2 - Clicar em [ columns ]
    3 - column_name = id / datatype = int / PK / NN / AI ---------------------------------------------------------------

    CAIXAS MARCADAS CHAVE PRIMÁRIA:
        - PK
        - AI (auto incrementação)

    CAIXA MARCADA PARA TODOS OS CAMPOS:
        - NN (nenhum campo pode ser nulo)

    OBS: Ao criar o primeiro campo, este aparece no DESKTOP, dentro da tabela
    OBS: Ao criar o primeiro campo, seu nome aparece abaixo das opções mencionadas no item 1
    OBS: Outros campos criados vêm abaixo do primeiro, funcionando como itens de lista

    6 - column_name = nome / datatype = varchar(50) / NN ---------------------------------------------------------------

    OBS: varchar = str / 50 = max_length

    7 - column_name = telefone / datatype = varchar(11) / NN -----------------------------------------------------------
    """

# Criação de uma segunda tabela = [ cargos ] + edição da primeira (adição de uma chave estrangeira)
def parte6():
    """
    1 - A segunda tabela [ cargos ] irá conectar-se com [ funcionarios ] através da chave estrangeira (FK)

    CAMPOS DA SEGUNDA TABELA [ cargos ]
    2 - column_name = id / datatype = INT / PK / NN / AI ---------------------------------------------------------------
    3 - column_name = nome / datatype = varchar(70) / NN ---------------------------------------------------------------

    NOVO CAMPO NA PRIMEIRA TABELA [ funcionarios ]
    4 - column_name = id_cargo / datatype = INT / NN -------------------------------------------------------------------

    OBS: o campo do item 4 não recebe (1) PK ou (2) AI
    OBS: (1) não pode ser chave primária e estrangeira ao mesmo tempo
    OBS: (2) os valores são criados manualmente, portanto não é preciso auto incremento
    OBS: a opção [ columns ] não possui a opção de marcar [ FK ], pois esta está na opção [ foreign keys ]
    OBS: consequentemente, o campo criado no item 4 será classificado como [ FK ] na opção [ foreign keys ]

    5 - Ir ao menu [ foreign keys ], que possui 3 opções:

        - foreign key name (á esquerda)
        - referenced table (ao meio)
        - foreign keys columns (á direita)

    OBS: Apenas no (Linux), a chave estrangeira pode ser gerada automaticamente
    OBS: No contexto atual, onde há duas tabelas [ funcionarios ] [ cargos ], quem está selecionado é [ funcionarios ]

    6 - Clicar em [ foreign key name ], um nome novo de chave estrangeira é gerado
    7 - Na opção [ referenced table ], duplo clique para informar a relação entre [ funcionarios ] <---> [ cargos ]
    8 - Na opção [ foreign keys columns ], marcar o campo que servirá como chave estrangeira, [ id_cargo ]

    9 - Ao fazer a ação do item 8, no DESKTOP, a conexão muda: [ traço ] para [ traço pontilhado ]
    9 - Isso significa relacionamento fraco entre as tabelas [ funcionarios ] & [ cargos ]
    9 - A tabela [ funcionarios ] oferece a chave estrangeira para a tabela [ cargos ], mas a 1 é quem depende da 2
    9 - Você não adiciona um id para um cargo, se ele não tiver sido criado, em primeiro lugar
    """

# Exportação do modele
def parte7():
    """
    1 - No menu principal, no canto superior esquerdo da tela, fazer: [ File / export / escolher a opção desejada... ]
    """
