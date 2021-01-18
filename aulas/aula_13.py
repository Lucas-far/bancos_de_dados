

"""
Módulo: aula_13.py

Curso / Bancos de Dados SQL e NoSQL do básico ao avançado
Local / Seção 3:Modelagem de Dados
Aula  / 13. Primeira Forma Normal
"""

"OBS"  # conhecida como 1FN
"OBS"  # 1FN é uma aplicadora de regras de normalização em tabelas
"OBS"  # No total, há 5, mas 3 formas normais são mais usadas
"OBS"  # 1 tabela/entidade está 1FN se: todos campos tiverem apenas um valor
"OBS"  # Tabelas não devem possuir campos nulos, caso contrário, é uma tabela problemática

def exemplo():
    """
    1. Código cliente 2. Nome 3. Telefone 4. Endereço
    1. C001 2. José  3. ('9563-6352', '9847-2501') 4. ('Rua Seis 85', 'Morumbi', '12536-965')
    1. C002 2. Maria 3. 3265-8596                  4. ('Rua Onze 64', 'Moema', '65985-963')
    1. C003 2. Janio 3.('8545-8956', '9598-6301')  4. ('Praça Ramos', 'Liberdade', '68858-633')
    """

"Problema 1?"  # nos campo [ endereço ] multivalorado
"Solução"      # criar novos campos, passando para eles, os valores já existentes aglomerados em [ endereço ]
"Resultado"    # Endereço <-- divide seus dados para --> Rua, Bairro, CEP

"Problema 2?"   # O campo [ telefone ], não deve ser separado pela criação de outro campo
"Por que?"      # Pode acontecer de o objeto/cliente registrado, não ter um dos campos, tornando o campo vazio
"O que fazer?"  # 3 procedimentos
"1"             # Criar uma tabela só para o [ código do cliente ], para ser herdada em outra tabela [ cliente ]
"2"             # Criar uma tabela para o [ telefone ], recebendo herança da tabela [ cliente ]
"3"             # Tabela [ código do cliente ] passa para [ cliente ], que passa para [ telefone ]

def exemplo2():
    """ /home/lucas/PycharmProjects/primeira_forma_normal """

"OBS"              # Após a primeira forma normal ser aplicada, pode-se prosseguir com a segunda forma normal
"Objetivo da 1FN"  # Evitar redundância de dados
