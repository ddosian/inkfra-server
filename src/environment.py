import os

def get_env(name):
    return os.environ.get(name)

# Postgres environment variables
POSTGRES_USER       = get_env("POSTGRES_USER")
POSTGRES_PASSWORD   = get_env("POSTGRES_PASSWORD")
POSTGRES_DB         = get_env("POSTGRES_DB")
POSTGRES_HOST       = get_env("POSTGRES_HOST")
POSTGRES_PORT       = int(get_env("POSTGRES_PORT"))