# kodland-diario
Projeto de apresentação da Kodland com o objetivo de servir como diário escolar.

# Escopo técnico
Este projeto visa mostrar a utilização da biblioteca flask juntamente com o flask-login. Também é abordado aqui uma arquitetura MVC básica, utilizaçao de classes, autenticação, e separação de rotas com blueprint.
O que não é foco neste projeto? Persistencia de dados em banco de dados relacional, não  relacional ou em arquivos, código seguro e UX.

# Funcionalidades
## Incluir estudante
## Registrar presença do estudante
## Registrar notas informativas do estudante


# Configuração

## Pré-requisitos
### Python 3
sudo apt install python3

### Ambiente virtual para isolamento
sudo apt install python3.12-venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate

# Execução
## Iniciando o projeto localmente
source .venv/bin/activate
python3 src/app.py


