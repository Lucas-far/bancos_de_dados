

"""
Módulo: aula_16.py

Curso || Bancos de Dados SQL e NoSQL do básico ao avançado
Local || Seção 3:Modelagem de Dados
Aula  || 16. Outras Formas Normais
"""

#####################
"Quarta forma normal"
#####################

"OBS"           # conhecida como 4FN e 5FN
"Condição 4FN"  # estar na 3FN e não conter campos com valores repetidos vindos de um mesmo CAMPO CHAVE
"Condição 4FN"  # apenas o CAMPO CHAVE pode repetir-se, nesse contexto

"Problema"  # o campo [ plano ] e [ exame ] estão com valores reincidentes de um mesmo CAMPO CHAVE
"Solução"   # duplicar o número de tabelas, usando o CAMPO CHAVE como intermediador, e eliminar a repetição
def exemplo1():
    """
    EXEMPLO ERRADO:

        paciente / plano      / exame
        Murilo   / São Camilo / endoscopia
        Murilo   / Unimed     / endoscopia
        Murilo   / São Camilo / hemograma
        Murilo   / Unimed     / hemograma

    EXEMPLO CORRETO:

        paciente / plano
        Murilo   / São Camilo
        Murilo   / Unimed

    EXEMPLO CORRETO:

        paciente / exame
        Murilo   / endoscopia
        Murilo   / hemograma
    """

"Problema"  # o campo [ titulação ] contêm valores reincidentes
"Solução"   # duplicar o número de tabelas, usando o CAMPO CHAVE como intermediador, e eliminar a repetição
def exemplo2():
    """
    EXEMPLO ERRADO:

        professor / disciplina                   / titulação
        Murilo    / Arq. e Org. de computadores  / Especialista
        Murilo    / Inteligência artificial      / Especialista
        João      / Lógica de programação        / Doutor
        João      / Sistemas Microcontrolados    / Doutor

    EXEMPLO CERTO:

    professor / disciplina
    Murilo    / Arq. e Org. de computadores
    Murilo    / Inteligência artificial
    João      / Lógica de programação
    João      / Sistemas Microcontrolados

    EXEMPLO CERTO:

    professor / titulação
    Murilo    / Especialista
    João      / Doutor
    """

#####################
"Quinta forma normal"
#####################

"OBS"           # conhecida como 5FN
"Condição 5FN"  # estar na 4FN, e que nenhum CAMPO NORMAL esteja repetido desnecessariamente, a não ser o CAMPO CHAVE
"Condição 5FN"  # portanto, se há 2 CAMPOS repetindo em mais de uma tabela, um deles é desnecessário

"Problema"  # o campo [ idproduto ] é reincidente, e não é o CAMPO CHAVE
"Solução"   # retirar o campo [ idproduto ] da última tabela
def exemplo3():
    """
    TABELA PRODUTOS     -> id_fornecedor / id_produto / descrição / qtd
    TABELA FORNECEDORES -> id_fornecedor / nome
    TABELA NOTA_FISCAL  -> id_fornecedor / id_nota / id_vendedor / id_produto
    """
