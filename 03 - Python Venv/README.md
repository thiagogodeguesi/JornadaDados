# Python

## Pyenv

Criação do ambiente virtual e controlar suas bibliotecas

[Link do Pyenv](https://github.com/pyenv-win/pyenv-win/blob/master/README.md)

[Link possivel erro de Excução](https://pt.stackoverflow.com/questions/220078/o-que-significa-o-erro-execu%C3%A7%C3%A3o-de-scripts-foi-desabilitada-neste-sistema)

*Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser*

Configuração das Variaveis de Ambiente


# PROJETOS

Sempre antes de criar um projeto de uma determinada biblioteca temos que validar qual é a versão do python que ela esta estavel. 

**python -m venv .venv** - Criação de ambiente virtual dentro do Python

**source .venv/Scripts/activate** - Ativar o ambiente virtual

**deactivate** - Desativar o ambiente virtual

## Poetry

**pip install poetry** - Instalar o Poetry 

**poetry config virtualenvs.in-project true** - Configurar variaveis

**poetry new ProjetoDjango** - Criar pasta com o Poetry

**poetry env use 3.12.1** - Definir o poetry rodar o python 3.12.1

**poetry add *BIBLIOTECA*** - Instalar a biblioteca no projeto (Ao invez de usar o pip install *biblioteca*)

**poetry remove *BIBLIOTECA*** - Desinstalar a biblioteca no projeto (Ao invez de usar o pip uninstall *biblioteca*)


**poetry shell** - Inicia o ambiente de desenvolvimento


## Ipython

**pip install ipython** - Instalar o ipython

## 1 - Pandas + Python 3.12.1


## 2 - Stramlit + Python 3.11.5


## 3 - Django + Python 2.7
