import pyodbc

def connect_to_db(database='postgres'):
    server = 'localhost'
    username = 'usuario'
    password = 'senha'
    port = '5432'  # Ou outra porta se necessário
    conn_string = f'DRIVER={{PostgreSQL Unicode}};SERVER={server};PORT={port};DATABASE={database};UID={username};PWD={password}'
    
    try:
        conn = pyodbc.connect(conn_string, autocommit=True)
        print(f"Conexão estabelecida com sucesso ao banco {database}!")
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados {database}: {e}")
        return None

    
def execute_sql_from_file(conn, file_path):
    if conn is not None:
        try:
            cursor = conn.cursor()
            with open(file_path, 'r') as file:
                sql_script = file.read()
                cursor.execute(sql_script)
                conn.commit()
                print("Arquivo SQL executado com sucesso!")
        except Exception as e:
            print(f"Erro ao executar o arquivo SQL: {e}")
        finally:
            cursor.close()

def main():

    conn = connect_to_db()
    file_path = 'app/scripts/create_database.sql'
    execute_sql_from_file(conn, file_path)
    conn.close()

    # Conecta ao banco de dados recém-criado
    conn = connect_to_db('AtividadesBD')
    file_path = 'app/scripts/create_tables.sql'
    execute_sql_from_file(conn, file_path)
    file_path = 'app/scripts/insert_data.sql'
    execute_sql_from_file(conn, file_path)
    conn.close()

if __name__ == '__main__':
    main()