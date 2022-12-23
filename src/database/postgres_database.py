from database.abs_database import AbstractDatabase, DatabaseConnectionOpts

class PostgresDatabase(AbstractDatabase):
  def __init__(self, connection_opts: DatabaseConnectionOpts):
    super().__init__(connection_opts)
