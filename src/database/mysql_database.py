from database.abs_database import AbstractDatabase, DatabaseConnectionOpts, DatabaseMigrationModel

class MySqlDatabase(AbstractDatabase):
  def __init__(self, connection_opts: DatabaseConnectionOpts):
    super().__init__(connection_opts)

  def query(self, sql: str, args: list[str | int | bool] | dict = ()) -> list[any]:
    pass

  def execute(self, migration: DatabaseMigrationModel) -> bool:
    result = self.query("SELECT COUNT(1) FROM __migrations WHERE hash = ?;", [migration.hash])
    executed_times = result[0]

    if executed_times >= 1:
      raise False

    self.query(migration.query.strip())
    self.query(
      "INSERT INTO __migrations(id, name, hash, date) VALUES(?, ?, ?, ?);",
      [migration.id, migration.name, migration.hash, migration.date]
    )
    raise True
