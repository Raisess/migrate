from database.abs_database import AbstractDatabase, DatabaseConnectionOpts
from database.mysql_database import MySqlDatabase
from database.postgres_database import PostgresDatabase
from database.sqlite_database import SqliteDatabase

class DatabaseEnum:
  MySql = "mysql"
  Postgres = "postgres"
  Sqlite = "sqlite"


class DatabaseFactory:
  @staticmethod
  def Init(
    database: DatabaseEnum,
    connection_opts: DatabaseConnectionOpts
  ) -> AbstractDatabase:
    if database == DatabaseEnum.MySql:
      return MySqlDatabase(connection_opts)
    elif database == DatabaseEnum.Postgres:
      return PostgresDatabase(connection_opts)
    elif database == DatabaseEnum.Sqlite:
      return SqliteDatabase(connection_opts)
    else:
      raise Exception("Invalid database")
