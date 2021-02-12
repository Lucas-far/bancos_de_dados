

"""
Módulo: aula_28.py

Curso || Bancos de Dados SQL e NoSQL do básico ao avançado
Local || Seção 4: Linguagem SQL - Parte 1
Aula  || 28. DML - Data Manipulation Language
"""

"------------------------------------------------------- INSERT -------------------------------------------------------"
"Grupo sintático"  # INSERT INTO VALUES
"INSERT"           # tabela
"INTO"             # tabela
"VALUES"           # valor
"OBS"              # Não há uma sintaxe reservada para [ campos ], ao invés, ele ficam entre ()


def exemplo():
    """
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    TABELA = tipos_produto
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    codigo || descricao
    --------------------------------------------------------------------------------------------------------------------
    1      || computador
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    2      || impressora
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

    EXEMPLO
    INSERT INTO tabela        (campo)     VALUES ('valor');
    INSERT INTO tipos_produto (descricao) VALUES ('Notebook');
    """


def exemplo2():
    """
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    TABELA = produtos
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    codigo || descricao || preco || tipo_codigo
    --------------------------------------------------------------------------------------------------------------------
    1      || arroz     || 12,40 || a1
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    2      || feijão    || 9,90  || b1
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    3      || batata    || 6,20  || c1
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

    EXEMPLO
    INSERT INTO tabela   (campo, campo2)    VALUES (valor, valor2)       ;
    INSERT INTO produtos (descricao, preco) VALUES ('Cadeira gamer', 970);
    """


"------------------------------------------------------- UPDATE -------------------------------------------------------"
"Grupo sintático"  # UPDATE WHERE
"UPDATE"           # tabela
"WHERE"            # campo pk do campo
"set"              # campo
"OBS"              # O comando UPDATE sempre deve vir acompanhado de WHERE, que sempre vêm ao final da sintaxe


def exemplo3():
    """
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    TABELA = tipos_produto
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    codigo || descricao
    --------------------------------------------------------------------------------------------------------------------
    1      || computador
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    2      || impressora
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

    EXEMPLO
    UPDATE tabela        set campo     = 'valor'   WHERE campo  = 3;
    UPDATE tipos_produto set descricao = 'Nobreak' WHERE codigo = 3;
    """


def exemplo4():
    """
    ------------------- UPDATE produtos set descricao = 'Notebook', preco = 2.800 WHERE codigo = 20; -------------------

    TABELA = produtos
    #############################################
    codigo || descricao   || preco || codigo_tipo
    1      ||  computador || 1.200 ||  1
    2      ||  impressora ||  700  ||  2
    #############################################

    --------------------------------------- SINTAXE SIMPLIFICADA (MINHA OPINIÃO) ---------------------------------------
    parte 1 -> WHERE pk = INT;
    parte 2 -> set campo = valor, campo2 = valor2
    parte 3 -> UPDATE tabela
    """


# Pela ausência do WHERE, todos os objetos referentes aos campos [ descricao ] & [ preco ] receberiam o mesmo valor
def exemplo_errado_update():
    """ UPDATE produtos set descricao = 'Notebook', preco = 2.800; """


"------------------------------------------------------- DELETE -------------------------------------------------------"
"Grupo sintático"  # DELETE FROM WHERE
"DELETE"           # tabela
"FROM"             # tabela
"WHERE"            # campo pk do campo
"OBS"              # O comando DELETE deve vir acompanhado por outros comando: FROM & WHERE


def exemplo5():
    """
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    TABELA = tipos_produto
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    codigo || descricao
    --------------------------------------------------------------------------------------------------------------------
    1      || computador
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    2      || impressora
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

    EXEMPLO
    DELETE FROM tabela        WHERE campo  = 3;
    DELETE FROM tipos_produto WHERE codigo = 3;
    """


# Pela ausência do WHERE, é deletado globalmente todos os valores da tabela especificada, pois o campo pk está ausente
def exemplo_errado_delete():
    """ DELETE FROM tipos_produto; """
