

"""
Módulo: metodos.py

Objetivo: retornar a quantidade de arquivos no escopo deste ambiente virtual
"""
from os import getcwd
print(getcwd())

def file_counter(the_path_string):
    """"""
    from os import scandir

    the_path = tuple(scandir(the_path_string))
    the_result = [str(item.is_file()) for item in the_path].count('True')
    return f'Há {the_result} arquivos em {the_path_string}'

# if __name__ == '__main__':
#     print(file_counter(getcwd()))
