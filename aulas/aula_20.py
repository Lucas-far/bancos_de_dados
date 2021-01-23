

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
    - Selecionar os tipos de dados para os atributos;
    - Definir chave primária (primary key, pk)
    - Definir chave estrangeira (foreign ket, fk, relacionamentos)
    - Exportar o diagrama (imagem ou pdf)
    """

# Criar um modelo e renomear
def parte2():
    """
    1 - Abrir o MySQL Workbench
    2 - No menu lateral, escolher a opção [ models ] (imagem de tabelas conectadas)
    3 - Por padrão, o MySQL Workbench já vêm com um exemplo de tabela
    4 - Clicar no botão de +
    5 - Na tela, há um texto [ mydb ], clicar 2x nele
    6 - Schema name: [ teste ]
    7 - Clicar no disquete (canto superior esquerdo) (menu visual abaixo do menu textual)
    8 - Será requisitado um nome, então coloque o mesmo da etapa 6
    9 - Fechar a janela que abriu, e agora o novo nome estará disponível, ao invés de [ mydb ]
    10 - O arquivo salvo, está em formato [ .mwb ]
    """

"OBS"  # É recomendável que, a partir do momento que cria-se um diagrama, você deve salvar alterações ao fazê-las
"OBS"  # O botão visual de salvar, foi mencionado na etapa 7 da função [ parte2 ]

# Criar um diagrama
def parte3():
    """
    1 - Acima do texto do modelo, há a opção [ + add diagram ]. Clicar neste.
    2 - No canto superior direito do diagrama, há dois retângulos
    3 - O da esquerda, fecha os menus laterais à esquerda
    4 - O da direita, fecha os menus laterais à direita
    """

# Criar uma tabela
def parte4():
    """
    1 - na tela do diagrama, escolher a opção [ place a new table ] [ ícone 7 ] [ atalho = T ]
    2 - ao clicar na área de trabalho do editor (tela branca), a tabela é criada
    3 - a tabela também passa para o menu esquerdo, aninhada ao diretório [ tables ]
    4 - para renomear a tabela: clique duplo botão esquerdo [ Name=funcionarios ] e [ SALVAR ]

    4 - SOBRE NOMES DE TABELAS:
        - sempre minúsculas, separador _
    """

# Criação de campos
def parte5():
    """
    1 - No clique duplo na tabela da área de trabalho, além de renomear, há várias outras opções disponíveis

        OPÇÕES: table, columns, indexes, foreign keys, triggers, partitioning, options, inserts, privileges

    2 - clicar em [ columns ]
    3 - column_name=id / datatype=int / PK
    4 - quando a caixa [ PK ] é selecionada, uma chave surge antes do campo [ column_name ]
    5 - Opções na criação de campos, que devem ser sempre marcadas:

        PARA CAMPO QUE SERÁ CHAVE PRIMÁRIA
            - PK
            - AI (auto incrementação)

        PARA CAMPO NORMAL
            - NN (para qualquer campo, pois isso significa que ele não pode ser nulo)
    """

#todo -> 19:00
