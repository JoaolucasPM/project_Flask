1 - Cria o arquivo 'db.py" onde ficará as CONFIGURAÇÕES e conexão com o banco de DADOS
-> Documentação https://flask.palletsprojects.com/en/stable/tutorial/database/

1.1 - Pode fazer um ctrl + C e Ctrl + V e importar para o arquivo db.py

-> é necessario registrar o "db.init_app(app)" dentro no nosso "App.py"
-> Deve ser importada

    from . import db
    db.init_app(app)

antes da app ser retornada.

2 - Usando o SQLAlchmy
2.1 - link: https://flask-sqlalchemy.readthedocs.io/en/stable/quickstart/


3
->https://www.sqlalchemy.org/
podemos ir direto ao "ORM Quickstart"