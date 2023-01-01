from datetime import datetime
from hashlib import sha256
from uuid import uuid4

class DatabaseConnectionOpts:
  def __init__(self, database: str, host: str, user: str, password: str, port: int):
    self.database = database
    self.host = host
    self.user = user
    self.password = password
    self.port = port


class DatabaseMigrationModel:
  def __init__(self, name: str, query: str):
    self.name = name
    self.query = query
    self.id = str(uuid4())
    self.date = datetime.utcnow().isoformat()
    self.hash = sha256(query.encode("utf-8")).hexdigest()


class AbstractDatabase:
  def __init__(self, connection_opts: DatabaseConnectionOpts):
    self.__connection_opts = connection_opts

  def query(self, sql: str, args: list[str | int | bool] | dict = ()) -> list[any]:
    pass

  # Should execute a migration file once and make sure will run only once
  def execute(self, migration: DatabaseMigrationModel) -> bool:
    pass

  def prepare(self) -> None:
    self.query(self.__get_create_table_query())

  def get_connection_opts(self) -> DatabaseConnectionOpts:
    return self.__connection_opts

  def __get_create_table_query(self) -> str:
    return """
      CREATE TABLE IF NOT EXISTS __migrations(
        id   VARCHAR(36)  UNIQUE PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        hash VARCHAR(64)  UNIQUE NOT NULL,
        date VARCHAR(30)  NOT NULL
      );
    """
