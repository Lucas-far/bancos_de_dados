

"""
Módulo: aula_14.py

Curso || Bancos de Dados SQL e NoSQL do básico ao avançado
Local || Seção 3:Modelagem de Dados
Aula  || 14. Segunda Forma Normal
"""

"OBS"  # conhecida como 2FN
"OBS"  # dependente da 1FN, ou seja, que a tabela tenha campos de valor singular
"OBS"  # sua regra é que todos os campos não primários devem estar relacionados ao campo primário
"OBS"  # Exemplo sem estar em 2FN
def exemplo():
    """
    TABELA PEDIDOS
    n_pedido / codigo_produto / produto              / qtd / v_unit / subtotal
    1005     / 1-934          / impressora laser     / 5   / 1500   / 7500
    1006     / 1-956          / impressora desjet    / 3   / 350    / 1050
    1007     / 1-923          / impressora matricial / 1   / 190    / 190
    1008     / 1-908          / impressora mobile    / 6   / 980    / 5880
    """

"Problema?"  # O campo [ produto ] não depende da chave primária [ n_pedido ], mas de [ codigo_produto ]
"Correção"   # Criar uma nova tabela com [ codigo_produto ] + [ produto ]
"Lógica"     # A nova tabela possui dois campos, sendo o segundo buscando referência do primeiro
def exemplo2():
    """
    TABELA PEDIDOS
    n_pedido / codigo_produto / qtd / v_unit / subtotal
    1005     / 1-934          / 5   / 1500   / 7500
    1006     / 1-956          / 3   / 350    / 1050
    1007     / 1-923          / 1   / 190    / 190
    1008     / 1-908          / 6   / 980    / 5880

    TABELA PRODUTO
    codigo_produto / produto
    1-934          / impressora laser
    1-956          / impressora desjet
    1-923          / impressora matricial
    1-908          / impressora mobile
    """

"Problema"  # O campo [ v_unit ] também não deve estar na TABELA PEDIDOS, mas na TABELA PRODUTO
"OBS"       # Nessa aula, isso foi ignorado, mas será corrigido em um contexto futuro
