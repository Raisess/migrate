class DatabaseConnectionOpts:
  def __init__(self, database: str, host: str, user: str, password: str, port: int):
    self.database = database
    self.host = host
    self.password = password
    self.port = port
    self.user = user

class AbstractDatabase:
  def __init__(self, connection_opts: DatabaseConnectionOpts):
    self.__connection_opts = connection_opts

  def get_connection_opts(self) -> DatabaseConnectionOpts:
    return self.__connection_opts

  def query(self, sql: str, args: list[str | int | bool] = ()) -> list[any]:
    pass
