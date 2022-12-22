import sqlite3

from database.abs_database import AbstractDatabase, DatabaseConnectionOpts

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
    except Exception as err:
      self.__conn.rollback()
      raise err
