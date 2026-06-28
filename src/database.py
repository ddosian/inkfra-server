from utils import *
import environment

import psycopg2

def connect(db=environment.POSTGRES_DB, user=environment.POSTGRES_USER, password=environment.POSTGRES_PASSWORD, host=environment.POSTGRES_HOST, port=environment.POSTGRES_PORT):
    host = dns_lookup(host) or host
    log.debug(f"Attempting to connect to postgres at {host}:{port}")
    try:
        connection = psycopg2.connect(dbname=db, user=user, password=password, host=host, port=port)
        cursor = connection.cursor()

        log.debug("Connection successful!")
        return connection, cursor
    except psycopg2.OperationalError as exception:
        log.error(f"Connection attempt failed: {exception}.")

def execute(sql):
    db = connect()
    connection = db[0]
    cursor = db[1]
    log.debug(f"Executing SQL: {sql}")

    try:
        cursor.execute(sql)
        try:
            result = cursor.fetchall()
            log.debug(f"Query result: {result}")
        except psycopg2.ProgrammingError:
            result = None

        if sql.lstrip().upper().startswith(("CREATE", "INSERT", "UPDATE", "DELETE", "ALTER", "DROP", "TRUNCATE")):
            connection.commit()

        return result
    finally:
        cursor.close()
        connection.close()

def initialize():
    log.debug("Initializing database...")
    log.debug("Initializing 'devices' table...")
    execute("""CREATE TABLE IF NOT EXISTS devices (
        id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        hostname VARCHAR(255) NOT NULL,
        ip_address INET NOT NULL,
        mac_address MACADDR NOT NULL,
        device_type VARCHAR(50) NOT NULL,
        last_seen TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )""")
    log.debug("'devices' table initialized.")