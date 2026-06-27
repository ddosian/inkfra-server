import os

# Postgres environment variables
postgres_user       = os.environ.get("POSTGRES_USER")
postgres_password   = os.environ.get("POSTGRES_PASSWORD")
postgres_db         = os.environ.get("POSTGRES_DB")
postgres_host       = os.environ.get("POSTGRES_HOST")
postgres_port       = int(os.environ.get("POSTGRES_PORT"))