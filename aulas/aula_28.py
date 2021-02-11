

"""
Módulo: aula_28.py

Curso || Bancos de Dados SQL e NoSQL do básico ao avançado
Local || Seção 4: Linguagem SQL - Parte 1
Aula  || 28. DML - Data Manipulation Language
"""

"Comandos"   # INSERT UPDATE DELETE (crud)
"Objetivo"   # Manipular dados

"--------------------------------------------------- COMANDO INSERT ---------------------------------------------------"
"Grupo sintático"  # INSERT INTO VALUES
"Sintaxe"          # INSERT INTO table (field) VALUES (value);
"Sintaxe maior"    # INSERT INTO table (field, field2, ...) VALUES (value, value2);

def insert_parte_1():
    """
    TABELA = tipos_produto
    --------------------
    codigo || descricao
    1      /  computador
    2      /  impressora
    --------------------

    APLICAÇÃO:
        INSERT INTO tipos_produto (descricao) VALUES ('Notebook');
    """


"OBS"  # Inserir na tabela abaixo, ao campos (descricao) & (preco) um novo valor
"OBS"  # Os dados podem ser manipulados por múltipla atribuição
def insert_parte_2():
    """
    TABELA = produtos
    --------------------------------------------
    codigo || descricao  || preco || codigo_tipo
    1      /  computador /  1.200 /  1
    2      /  impressora /  700   /  2
    --------------------------------------------

    APLICAÇÃO:
        INSERT INTO produtos (descricao, preco) VALUES ('Cadeira gamer', 970);
    """


"--------------------------------------------------- COMANDO UPDATE ---------------------------------------------------"
"OBS"  # O comando UPDATE deve vir acompanhado com frequência, por outro comando: WHERE
"OBS"  # WHERE vêm ao final da sintaxe, e serve como filtro, para melhor identificação
"OBS"  # Sua interdependência é muito importante, e caso UPDATE não venha com WHERE, pode gerar erros graves
"OBS"  # Em minha opinião, a sintaxe pode ser quebrada, para melhor entendimento

"EXEMPLO ERRADO/PERIGOSO"  # UPDATE produtos set descricao = 'Notebook', preco = 2.800;
"PROBLEMA"                 # Você atualizaria simplesmente, todos os objetos referenciados no comando
"PROBLEMA"                 # Tudo aquilo que estiver no campo [ descricao ] e [ preco ] terão seus valores alterados


def update_parte_1():
    """
    TABELA = tipos_produto
    --------------------
    codigo || descricao
    1      /  computador
    2      /  impressora
    3      /  notebook
    --------------------
    APLICAÇÃO:
        UPDATE tipos_produto set descricao = 'Nobreak' WHERE codigo = 3;

    DISSECAÇÃO:
        parte 1 -> WHERE pk = INT;
        parte 2 -> set campo = valor
        parte 3 -> UPDATE tabela
    """


def update_parte_2():
    """
    TABELA = produtos
    --------------------------------------------
    codigo || descricao  || preco || codigo_tipo
    1      /  computador /  1.200 /  1
    2      /  impressora /  700   /  2
    --------------------------------------------
    APLICAÇÃO:
        UPDATE produtos set descricao = 'Notebook', preco = 2.800 WHERE codigo = 20;

    DISSECAÇÃO:
        parte 1 -> WHERE pk = INT;
        parte 2 -> set campo = valor, campo2 = valor2
        parte 3 -> UPDATE tabela
    """


"--------------------------------------------------- COMANDO DELETE ---------------------------------------------------"
"OBS"  # O comando DELETE deve vir acompanhado com frequência, por outros comando: FROM & WHERE
"OBS"  # O comando WHERE é essencial para filtragem correta do dado a ser deletado
"OBS"  # O comando WHERE estando ausente, pode gerar problemas sérios

"EXEMPLO ERRADO/PERIGOSO"  # DELETE FROM tipos_produto;
"PROBLEMA"                 # Você deletaria simplesmente, todos os objetos referenciados no comando
"PROBLEMA"                 # Os campos permaneceriam, os valores seriam todos apagados

def delete_parte_1():
    """
    TABELA = tipos_produto
    --------------------
    codigo || descricao
    1      /  computador
    2      /  impressora
    3      /  notebook
    --------------------
    APLICAÇÃO:
        DELETE FROM tipos_produto WHERE codigo = 3;
    """
