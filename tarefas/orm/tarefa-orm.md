# Resumo sobre ODBC 

## Etapa 1: Configurar o ambiente de desenvolvimento Python pyodbc

### Pré-requisitos

* Python 3

- Se ainda não possui o Python, instale o runtime e o gerenciador de pacotes PyPI 
- Não quer usar seu próprio ambiente? [GitHub Codespaces](https://github.com/features/codespaces)

### Instalar o driver ODCB

#### Linux

1. Obtenha e instale [Microsoft ODBC Driver for SQL Server (Linux)](https://learn.microsoft.com/pt-br/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16)

2. Verifique se você instalou o driver.

### Instale o pacote pyodbc

Obtenha o [pacote pyodbc](https://pypi.org/project/pyodbc/) do PyPI.

1. Abra um prompt de comando em um diratório vazio.

2. Instale o [pacote pyodbc](https://pypi.org/project/pyodbc/)
> pip install pyodbc

### Verifique os pacotes instalados

Você pode o usar a ferramenta de linha de comando PyPI para verificar se os pacotes pretendidos estão instalados.

1. Verifique a lista de pacotes instalados com *pip list*.

> pip list

## Etapa 2: criar um banco de dados SQL para desenvolvimento Python pyodbc