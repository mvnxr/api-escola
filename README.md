# Projeto API #

 O objetivo principal do projeto é criar e disponibilizar uma <i>**API Rest**</i> </br>
 Consumir os endpoints e realizar operações de CRUD.

#Requisitos

Criar uma API que seja capaz de armazenar dados e realizar operações <i>**CRUD**</i>

#Este projeto foi feito com:

- [Python 3.9.1](https://www.python.org/downloads/release/python-391/)
- [Django 3.1.5](https://www.djangoproject.com/download/)
- [Django Rest Framework - LTS](https://www.django-rest-framework.org/community/release-notes/#312x-series)

**Como rodar o projeto ?**

- Clone esse reposiório.
- Crie um virualenv com Python
- Ative o virtualenv.
- Instale as depêndencias.
- Rode as Migrações

**Comandos**:

_git clone<br />
cd api<br />
python3 -m venv .venv<br />
source .venv/bin/activate<br />
pip install -r requirements.txt<br />
python manage.py makemigrations<br />
python manage.py migrate<br />_


**Criando SuperUser**

python manage.py createsuperuser </br>
username : admin</br>
email : admin@api.com</br>
senha : admin</br>
confirmar senha: admin</br>

python manage.py drf_create_token admin</br>

**Notas sobre a API**

A autenticação desse projeto foi baseada em [TokenAuthentication](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication) usando um formato de client-server ou seja requisições autenticadas nos endpoints.


Testes Unitários

Para realizar os testes realizados com TestCase


Endpoints do projeto



http://127.0.0.1:8000/api/alunos/api/alunos - Lista todos os alunos </br>
http://127.0.0.1:8000/api/alunos/create - Cria um aluno </br>
http://127.0.0.1:8000/api/alunos/api/alunos/{ID} - Filtra aluno por ID</br>
http://127.0.0.1:8000/api/alunos/api/alunos/{ID}/update - Atualiza dados do aluno </br>
http://127.0.0.1:8000/api/alunos/api/alunos/{ID}/delete - Deleta aluno(ID)


Limite de Requisições

- Usuario não autenticado : 5 Rrequisições por minuto
- Usuario autenticado : 10 Requisições por minuto

 Paginação 

- 3 objetos por página

Criando usuario/Consumindo Endpoints

Para gerar um token entre na url http://127.0.0.1:8000/admin </br>
com um usuario do tipo superuser, acesse o **APP - Token de Autorização**
adicione uma chave Token ao seu usuario.

Criando um aluno#

Requisição POST
    Endpoint: http://127.0.0.1:8000/api/alunos/create

                Header: 'Content-Type' : 'application/json'
                Authorization: 'Token 67f885ffce9364fc3b6d770c95acfcbabc661db0'

{
	"nome":"aluno 111",
	"is_student": true,
	"turma": "Fundamental"
}

