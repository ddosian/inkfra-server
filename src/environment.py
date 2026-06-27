import os

def get_env(name):
    return os.environ.get(name)

# Postgres environment variables
postgres_user       = get_env("POSTGRES_USER")
postgres_password   = get_env("POSTGRES_PASSWORD")
postgres_db         = get_env("POSTGRES_DB")
postgres_host       = get_env("POSTGRES_HOST")
postgres_port       = int(get_env("POSTGRES_PORT"))