

"""
Módulo: aula_15.py

Curso || Bancos de Dados SQL e NoSQL do básico ao avançado
Local || Seção 3:Modelagem de Dados
Aula  || 14. Terceira Forma Normal
"""

"OBS"  # conhecida como 3FN
"OBS"  # dependente da 1FN e 2FN
"OBS"  # numa tabela 3FN, campos não primários, não devem estar vinculados a qualquer outro campo não chave

def exemplo():
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

"Problema"  # O campo [ subtotal ] depende dos campos não chave [ v_unit ] e [ qtd ]
"Problema"  # A sua existência é desnecessária

# Correção
def exemplo2():
    """
    TABELA PEDIDOS
    n_pedido / codigo_produto / qtd / v_unit
    1005     / 1-934          / 5   / 1500
    1006     / 1-956          / 3   / 350
    1007     / 1-923          / 1   / 190
    1008     / 1-908          / 6   / 980
    """

"Problema"  # O campo [ v_unit ] também não deveria estar aqui
"Problema"  # A questão para isso não é normalização, mas por não fazer sentido, este deveria estar numa TABELA PRODUTO

# Correção
def exemplo3():
    """
    TABELA PEDIDOS
    n_pedido / codigo_produto / qtd
    1005     / 1-934          / 5
    1006     / 1-956          / 3
    1007     / 1-923          / 1
    1008     / 1-908          / 6

    TABELA PRODUTO
    codigo_produto / produto              / v_unit
    1-934          / impressora laser     / 1500
    1-956          / impressora desjet    / 350
    1-923          / impressora matricial / 190
    1-908          / impressora mobile    / 980
    """

"Lógica"  # Os campos [ produto ] e [ v_unit ] continuam na TABELA PEDIDOS, só que acessíveis indiretamente
"Lógica"  # O acesso acontece pelo campo estrangeiro [ codigo_produto ]
