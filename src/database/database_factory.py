from database.abs_database import AbstractDatabase, DatabaseConnectionOpts
from database.postgres_impl import Postgres
from database.sqlite_impl import Sqlite

class DatabaseEnum:
  Postgres = "postgres"
  Sqlite = "sqlite"

class DatabaseFactory:
  @staticmethod
  def Init(
    database: DatabaseEnum,
    connection_opts: DatabaseConnectionOpts
  ) -> AbstractDatabase:
    if database == DatabaseEnum.Postgres:
      return Postgres(connection_opts)
    elif database == DatabaseEnum.Sqlite:
      return Sqlite(connection_opts)
    else:
      raise Exception("Invalid database")
