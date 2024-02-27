'''
nao ta com todas as configs no .vscode
'''

'''
26.02.2024: Criei a pasta project, a .vscode para configurar meu vscode
            configurei todo o ambiente, criei o venv, instalei o django,
            tudo certo, a pasta project foi criada com uma linha de código que cria automaticamente.
            python -m venv venv
            venv/Scripts/Activate
            pip install django
            django-admin startproject project . (cria a pasta projeto na raiz)

            Configurar o git no repositório
            '''
            git config --global user.name 'Hariel'
            git config --global user.email 'harielpimenta@hotmail.com'
            git config --global init.defaultBranch main
            git init
            git add
            git commit -m 'Mensagem do commit'
            git remote add origin URL_DO_GIT, cria o repositorio noo github
'''

'''
27.02.2024: python manage.py startapp contact(criei o app main na 
            pasta  do projeto)
            fui no arquivo settings do project e adicionei na lista de INSTALLED_APPS a linha 'contact', que faz com que o django reconheça o app que eu acabei de criar, evitando erros!