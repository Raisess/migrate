import mysql.connector as mysql

from database.abs_database import AbstractDatabase, ArgumentsType, DatabaseConnectionOpts, DatabaseMigrationModel

class MySqlDatabase(AbstractDatabase):
  def __init__(self, connection_opts: DatabaseConnectionOpts):
    super().__init__(connection_opts)
    self.__conn = mysql.connect(
      host=connection_opts.host,
      port=connection_opts.port,
      user=connection_opts.user,
      password=connection_opts.password,
      database=connection_opts.database
    )

  def begin(self) -> None:
    self.__conn.start_transaction()

  def commit(self) -> None:
    self.__conn.commit()

  def rollback(self) -> None:
    self.__conn.rollback()

  def query(self, sql: str, args: ArgumentsType = ()) -> list[any]:
    data = []
    with self.__conn.cursor() as cursor:
      cursor.execute(sql, args)
      if not sql.startswith("INSERT"):
        data = cursor.fetchall()

    return data

  def execute(self, migration: DatabaseMigrationModel) -> bool:
    result = self.query("SELECT COUNT(1) FROM __migrations WHERE hash = %s;", (migration.hash, ))
    self.commit()
    executed_times = result[0][0]

    if executed_times >= 1:
      return False

    self.begin()
    try:
      self.query(migration.query.strip())
      self.query(
        "INSERT INTO __migrations(id, name, hash, date) VALUES(%s, %s, %s, %s);",
        (migration.id, migration.name, migration.hash, migration.date)
      )
      self.commit()
      return True
    except Exception as ex:
      self.rollback()
      raise ex
