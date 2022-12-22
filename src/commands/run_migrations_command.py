import os

from commands.abs_command import AbstractCommand
from database.abs_database import DatabaseConnectionOpts
from database.database_factory import DatabaseFactory
from util.file_manager import FileManager

class RunMigrationsCommand(AbstractCommand):
  def __init__(self, file_manager: FileManager):
    super().__init__("run", 1)
    self.__file_manager = file_manager

  def handle(self, args: list[str]) -> None:
    if len(args) < self.get_required_args_len():
      raise Exception(f"Invalid arguments, database name not provided")

    database_name = args[0]
    opts = DatabaseConnectionOpts(
      os.getenv("DB_NAME") or database_name,
      os.getenv("DB_HOST") or "localhost",
      os.getenv("DB_USER") or "root",
      os.getenv("DB_PASS"),
      os.getenv("DB_PORT") or 5432
    )
    database = DatabaseFactory.Init(database_name, opts)

    files = self.__file_manager.list()
    if not len(files):
      raise Exception("No migrations found")

    files.sort()
    for file in files:
      database.query(self.__file_manager.read(file))
