

"""
Módulo: aula_13.py

Curso || Bancos de Dados SQL e NoSQL do básico ao avançado
Local || Seção 3:Modelagem de Dados
Aula  || 13. Primeira Forma Normal
"""

"OBS"           # conhecida como 1FN
"OBS"           # 1FN é uma aplicadora de regras de normalização em tabelas
"OBS"           # No total, há 5, mas 3 formas normais são mais usadas
"Condição 1FN"  # todos os seus campos possuirem valor singular
"OBS"           # Tabelas não devem possuir campos nulos, caso contrário, é uma tabela problemática

"Problema"  # o campo [ endereço ] é multivalorado
"Solução"   # retira-se o campo [ endereço ], e criam-se novos campos, passando para eles, os valores em [ endereço ]
def exemplo():
    """
    Código cliente / Nome  / Telefone                   / Endereço
    C001           / José  / ('9563-6352', '9847-2501') / ('Rua Seis 85', 'Morumbi', '12536-965')
    C002           / Maria / 3265-8596                  / ('Rua Onze 64', 'Moema', '65985-963')
    C003           / Janio / ('8545-8956', '9598-6301') / ('Praça Ramos', 'Liberdade', '68858-633')
    """

# Correção
def exemplo2():
    """
    Código cliente / Nome  / Telefone                   / Rua         / Bairro    / CEP
    C001           / José  / ('9563-6352', '9847-2501') / Rua Seis 85 / Morumbi   / 12536-965
    C002           / Maria / 3265-8596                  / Rua Onze 64 / Moema     / 65985-963
    C003           / Janio / ('8545-8956', '9598-6301') / Praça Ramos / Liberdade / 68858-633
    """

"Problema"  # o campo [ telefone ] é multivalorado

# Correção
def exemplo3():
    """
    Código cliente / Nome  / Rua         / Bairro    / CEP
    C001           / José  / Rua Seis 85 / Morumbi   / 12536-965
    C002           / Maria / Rua Onze 64 / Moema     / 65985-963
    C003           / Janio / Praça Ramos / Liberdade / 68858-633

    Código cliente / Telefone
    C001           / 9563-6352
    C001           / 9847-2501
    C002           / 3265-8596
    C003           / 8545-8956
    C003           / 9598-6301
    """

# Minha tentativa e dúvidas
def minha_tentativa():
    """
    1 - /home/lucas/PycharmProjects/primeira_forma_normal

    PROCEDIMENTOS
        - Eu criei 3 modelos: [ ClientCode ] [ Client ] [ ClientPhone ]
        - Eu criei um modelo [ ClientCode ], pensando que, por ser um modelo a ser herdado, só pode ter um campo
        - O modelo [ ClientCode ] passa herança para [ Client ]
        - O modelo [ Client ] passa herança para [ ClientPhone ]

    DÚVIDAS
        - Será se o que eu fiz está certo?
    """
