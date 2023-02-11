from postgres import Postgres

from database.abs_database import AbstractDatabase, ArgumentsType, DatabaseConnectionOpts, DatabaseMigrationModel

class PostgresDatabase(AbstractDatabase):
  def __init__(self, connection_opts: DatabaseConnectionOpts):
    super().__init__(connection_opts)
    uri = f"postgresql://{connection_opts.user}:{connection_opts.password}@{connection_opts.host}:{connection_opts.port}/{connection_opts.database}"
    self.__conn = Postgres(uri)

  def query(self, sql: str, args: ArgumentsType = (), ret: bool = False) -> list[any]:
    if ret:
      return self.__conn.all(sql.strip(), args)
    else:
      self.__conn.run(sql.strip(), args)
      return []

  def execute(self, migration: DatabaseMigrationModel) -> bool:
    result = self.query("SELECT COUNT(1) FROM __migrations WHERE hash = %(hash)s;", { "hash": migration.hash }, True)
    executed_times = result[0]

    if executed_times >= 1:
      return False

    self.query(migration.query.strip())
    self.query(
      "INSERT INTO __migrations(id, name, hash, date) VALUES(%(id)s, %(name)s, %(hash)s, %(date)s);",
      { "id": migration.id, "name": migration.name, "hash": migration.hash, "date": migration.date }
    )
    return True
