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

# Resumo sobre ORM

## O que é?

ORM(Object-Relational-Mappers) é uma ferramenta fundamental para qualquer desenvolvedor que trabalha com bancos de dados relacionais. Ele permite acessar os dados usando a sintax de objetos em vez de SQL, tornand o o código masi limpo e fácil de dar manutenção.

## Para que serve?

Ele separa a lógica de banco de dados da lógica de negócios. Além disso, ele permite que você trabalhe com dados em formato nativo de objetos Python, o que é masi intuitivo e fácil de tabalhar.

## Pony ORM 

Exsitem outros mapeadores em Python, como Django e SQLAlchemy, mas o Pony tem algumas vantagens:

* Uma sintaxe excepcionalmente xonveniente para escrever consultas

* Otimização automática de consultas

* Uma solução elegante para o problema N+1 

* Editor de [esquema de banco de dados on-line](https://editor.ponyorm.com/)

Em comparação com Django, Pony fornece:

* O padrão do IdentityMap

* Gestão automática de transações

* Cachar automaticamente de consultas e objetos

* Suporte completo de chaves compostas

* A capacidade de escrever facilmente consultas usando LEFT JOIN, HAVING entre outros.

## Instalação

> pip install pony