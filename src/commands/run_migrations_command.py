import os
from yacli import Command

from database.abs_database import DatabaseConnectionOpts, DatabaseMigrationModel
from database.database_factory import DatabaseFactory
from util.file_manager import FileManager

class RunMigrationsCommand(Command):
  def __init__(self, file_manager: FileManager):
    super().__init__(
      "run",
      "Run all '.sql' files from the migrations directory into the target database.",
      args_len=1
    )
    self.__file_manager = file_manager

  def handle(self, args: list[str]) -> None:
    database_name = args[0]
    database_opts = DatabaseConnectionOpts(
      os.getenv("DB_NAME") or database_name,
      os.getenv("DB_HOST") or "localhost",
      os.getenv("DB_USER") or "root",
      os.getenv("DB_PASS") or "",
      os.getenv("DB_PORT") or 5432
    )
    database = DatabaseFactory.Init(database_name, database_opts)

    files = self.__file_manager.list()
    if not len(files):
      raise Exception("No migrations found")

    for filename in files:
      if not filename.endswith('.sql'):
        continue

      try:
        print(f"==> Executing migration: {filename}")
        executed = database.execute(DatabaseMigrationModel(filename, self.__file_manager.read(filename)))
        if executed:
          print(f"==> Executed successfully")
        else:
          print(f"==> Already executed")
      except Exception as exception:
        print(f"==> Failed to execute")
        raise exception
