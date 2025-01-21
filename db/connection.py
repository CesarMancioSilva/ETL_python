import psycopg2
from psycopg2 import OperationalError, Error
from dotenv import load_dotenv
import os

load_dotenv()

def connect_to_db():
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT"),
        )
        print("Conexão com o banco de dados estabelecida com sucesso.")
        return connection

    except OperationalError as e:
        print(f"Erro de conexão com o banco de dados: {e}")
        return None

    except Error as e:
        print(f"Erro desconhecido: {e}")
        return None