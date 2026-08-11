import os

import psycopg2


def get_db_connection():
    """Cria e retorna uma conexão com o PostgreSQL usando variáveis de ambiente."""
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        port=os.getenv("DB_PORT", "5432"),
        user=os.getenv("DB_USER", "devops"),
        password=os.getenv("DB_PASSWORD", "devops"),
        dbname=os.getenv("DB_NAME", "devopsdb"),
        connect_timeout=5,
    )
