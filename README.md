# GradeMaker

O projeto a seguir visa auxiliar a montagem de grade
da uerj no início de período, visto que a utilização 
do sistema atual é muito díficil

## Instalação
Para rodar o programa, você primeiramente precisa do python na
versão 3.0+ instalado na sua máquina.

#### Dependências
O programa utiliza duas dependências:
- selenium
- openpyxl
- python-dotenv

Para instalar, vá no seu prompt de comando e digite: <br>
`$ pip install openpyxl selenium python-dotenv`

Para rodar o selenium, você precisará de um driver para que o
scapper possa executar no navegador.
Acesse o site:<br>
https://selenium-python.readthedocs.io/installation.html
Baixe o driver para seu navegador de preferência e
cole na sua pasta raiz do python/script

Após isso, você deverá criar um arquivo .env na raiz do projeto
com as informações de matricula e senha do aluno online
desse modo.
```
MATRICULA=MINHA_MATRICULA
SENHA=MINHA_SENHA
```
