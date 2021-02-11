

"""
Módulo: aula_27.py

Curso || Bancos de Dados SQL e NoSQL do básico ao avançado
Local || Seção 4: Linguagem SQL - Parte 1
Aula  || 27. DQL - Data Query Language
"""

"Comando"   # SELECT
"Objetivo"  # Consultar dados

def exemplo_1():
    """
    TABELA = tipos_produto
    --------------------
    codigo || descricao
    1      /  computador
    2      /  impressora
    --------------------

    SELECT * FROM tipos_produto;
    SELECT código FROM tipos_produto;
    SELECT codigo, descricao FROM tipos_produto;
    """

# Exemplo (alias = apelido)
"OBS"  # não foi explicado se apelidos podem ser passado aos campos independente da tabela ter sido apelidade ou não
def exemplo_2():
    """
    TABELA = tipos_produto
    --------------------
    codigo || descricao
    1      /  computador
    2      /  impressora
    --------------------

    SELECT tp.codigo AS cd, descricao AS dsc FROM tipos_produto AS tp;
    """