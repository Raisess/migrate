import sqlite3

from database.abs_database import AbstractDatabase, DatabaseConnectionOpts, DatabaseMigrationModel

class SqliteDatabase(AbstractDatabase):
  def __init__(self, connection_opts: DatabaseConnectionOpts):
    super().__init__(connection_opts)

    self.__conn = sqlite3.connect(
      database = connection_opts.database + ".db",
      check_same_thread = False
    )

  def query(self, sql: str, args: list[str | int | bool] = ()) -> list[any]:
    try:
      cursor = self.__conn.cursor()
      cursor.execute(sql, args)
      self.__conn.commit()
      return cursor.fetchall()
    except Exception as exception:
      self.__conn.rollback()
      raise exception

  def execute(self, migration: DatabaseMigrationModel) -> bool:
    result = self.query("SELECT COUNT(1) FROM __migrations WHERE hash = ?", [migration.hash])
    execute_times = result[0][0]

    if execute_times >= 1:
      return False

    self.query(migration.query)
    self.query(
      "INSERT INTO __migrations(id, name, hash, date) VALUES(?, ?, ?, ?);",
      [migration.id, migration.name, migration.hash, migration.date]
    )
    return True
