# Projeto Flask

### Objetivo: Criar uma aplicação web de Lista de Tarefas que possa se comunicar e manipular um Banco de Dados Postgresql.

É uma aplicação que cria, edita e deleta uma lista de tarefas pelo mini-framework Flask, em Python, juntamente com um Banco de Dados gerenciado pelo PostgreSQL. Na interface web nós podemos manipular o Banco de Dados para adiconar tarefas, altera-las e remove-las. 

É uma aplicação simples, em que o foco não é a aplicação web, mas sim entender conceitos de API, como rotas, portas, verbos e códigos HTTP, entre outros, assim como criar um Banco de Dados para uma aplicação.

> Como já explicado, o foco não é na construção da API em sí, por isso os códigos html e css foram tirados do vídeo [Lean Flask for Python - Full Tutorial](https://www.youtube.com/watch?v=Z1RJmh_OqeA&list=PLVURzHiHgu5U2eeEMjd2E1ITahT9BUNqc&index=3), do canal [freeCodeCamp.org](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ), com algumas alterações.

___
### Caso queria testar essa aplicação, basta seguir os seguintes passos:

1. Editar o seguinte trecho do arquivo "config.py" para se conectar a outro Banco de Dados PostgreSQL:

> "SQLALCHEMY_DATABASE_URI = 'URI para o Banco de dados'"

2. Executar os seguintes comando no terminal:

```bash
python3               # Para abrir o Terminal Integrado Python
```

```python
from app import db    # Importar instancia do Banco de Dados

db.create_all()       # Para criar a tabela dentro do Banco de Dados
```

3. Agora basta executar o arquivo "run.py" e abrir no navegador a URL fornecida no termianl, ou "localhost:5000" se essa porta não estiver utilizada.
