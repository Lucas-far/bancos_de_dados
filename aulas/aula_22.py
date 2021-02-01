

"""
Uma empresa fabricante de picolés deseja armazenar informações acerca de seus negócios. Os picolés fabricados são
divididos em normal (com água) e ao leite. As informações comuns armazenadas dos picolés são: sabor, ingredientes, preço
e tipo da embalagem. Especificamente, picolés normais possuem um conjunto de aditivos nutritivos (vitaminas ou sais
minerais) cada um com nome e fórmula química; e picolés ao leite contêm um conjunto de conservantes, cada um com nome e
descrição. Os dois tipos de picolés são vendidos em lotes exclusivos (ou normais, ou ao leite) para os revendedores e
cada venda gera uma nota fiscal que pode conter um ou vários lotes. As notas fiscais possuem data, valor, número de
série e descrição. Revendedores possuem uma pessoa de contato para eventuais resoluções de problemas, além disso,
armazena-se do revendedor o CNPJ e a razão social. Deseja-se obter relatórios sobre as vendas mensais dos picolés de
cada tipo e quais revendedores compraram mais picolés nos últimos meses.
"""

tipos_de_picole = ('com água', 'ao leite')
ingredientes = ('sabor', 'ingredientes', 'preço', 'tipo de embalagem')
picole_com_agua_aditivos = ('vitaminas', 'sais minerais')  # um ou outro
picole_com_agua_aditivos_tipos = ('nome', 'fórmula química')
picole_ao_leite_conservates = ('nome', 'descrição')
lote = {'picole_com_agua': 0, 'picole_ao_leite': 1}
revendedores = ('cnpj', 'razão social')
nota_fiscal = ('data', 'valor', 'número de série', 'descrição')
pessoa_de_contato = ('nome', 'contato')
