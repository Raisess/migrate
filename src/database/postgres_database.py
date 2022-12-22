from database.abs_database import AbstractDatabase, DatabaseConnectionOpts

class PostgresDatabase(AbstractDatabase):
  def __init__(self, connection_opts: DatabaseConnectionOpts):
    super().__init__(connection_opts)

  def query(self, sql: str, args: list[str | int | bool] = ()) -> list[any]:
    pass
