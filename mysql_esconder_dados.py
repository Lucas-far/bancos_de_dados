

"""
Módulo: mysql_esconder_dados.py
Objetivo: inviabilizar nome, user, e senha do seu banco de dados
Palavra chave: esconder dados mysql
"""

""  # Abrir o terminal
""  # cd Desktop
""  # mkdir mysql_project
""  # cd mysql_project
""  # python3 -m venv .venv
""  # exit
""  # Pycharm / File / Open
""  # git init
""  # pip install django==2.2.17 mysqlclient
""  # django-admin startproject pp .
""  # django-admin startapp pa
""  # pip freeze > requirements.txt
""  # Abrir o MySQL Workbench
""  # CREATE DATABASE dtb_mysql_project;
""  # raiz/new/file/.gitignore -------------------------------------------------------> adicionar texto [ dtb_data.py ]
""  # raiz/new/file/dtb_data.py

# Conteúdo [ dtb_data.py ]
def raiz():
    """
    def show_dtb_name():
        return 'nome do seu bdd mysql'

    def show_dtb_user():
        return 'nome da sua conta mysql'

    def show_dtb_password():
        return 'sua senha mysql'

    if __name__ == '__main__':
        print(show_dtb_name())
        print(show_dtb_user())
        print(show_dtb_password())
    """

# Configuração do bdd
def pp_settings():
    """
    from dtb_data import show_dtb_name, show_dtb_user, show_dtb_password

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': f'{show_dtb_name()}',
            'USER': f'{show_dtb_user()}',
            'PASSWORD': f'{show_dtb_password()}',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    """

""  # git add .
""  # git commit -m 'first commit'
""  # criar um repositório vazio no Github
""  # git remote add origin git@github.com:Lucas-far/test_mysql.git
""  # git branch -M main
""  # git push -u origin main
""  # atualizar a página do Github, onde está o repositório remoto
""  # -------------------------------------------> Pela lógica, o arquivo ignorado não deve estar no repositório remoto

"OBS"  # Quem clonar seu repositório, não terá acesso aos seus dados
"OBS"  # Mas também é preciso saber se o projeto está funcionando

""  # Voltar ao terminal do projeto
""  # python manage.py shell
""  # from nome_seu_pacote_projeto.settings import DATABASES
""  # DATABASES
""  # ---------------------------------------> as chaves [ NAME, USER, PASSWORD ] devem ter o retorno das funções
""  # exit()
""  # python manage.py migrate ------------------------------------------------------------------> não deve haver erros
""  # python manage.py runserver ----------------------------------------------------------------> não deve haver erros
