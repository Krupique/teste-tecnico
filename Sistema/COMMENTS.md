# Explicação do sistema e seu funcionamento

## Sobre o Sistema

**Tecnologias**<br/>

Para realizar o projeto eu utilizei as seguintes tecnologias:
* (Front-end): `HTML`, `CSS`, `JavaScript`, `Jquery`.
* (Back-end): `Django`

**Estrutura de arquivos e diretórios**<br/>

O projeto está estruturado da seguinte maneira:
* **(Diretório)**: `venv_projeto`: É a máquina virtual que foi criada para este projeto.
* **(Diretório)**: `teste_tecnico`: É o projeto propriamente dito.
* **(Diretório)**: `layout`: Imagens obtidas no escopo do projeto.

Dentro do diretório teste_tecnico temos:
* **(Diretório)**: `portal_noticias`: É a app que eu criei para realização das funcionalidades.
* **(Diretório)**: `teste_tecnico`: É a estrutura padrão criada pelo Django com todos os seus arquivos de configuração. 
* **(arquivo)**: `db.sqlite3`: É o arquivo de banco de dados (database) padrão do Django, é com ele que vamos armazenar as informações.
* **(arquivo)**: `manage.py`: É o principal arquivo de execução do Django, é a partir dele que tudo começa.

## Como executar

Para executar o projeto, você precisará ter o Python instalado em sua máquina e o pacote virtualenv, que é o pacote responsável por criar ambientes virtuais com python, com os pacotes instalados execute:

* No diretório raiz que contém o diretório venv_projeto: `source venv_projeto/bin/activate`;
* No mesmo diretório execute: `python teste_tecnico/manage.py runserver`
