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
    opts = DatabaseConnectionOpts("localhost", "user", "pass", 5432)
    database = DatabaseFactory.Init(database_name, opts)

    files = self.__file_manager.list()
    if not len(files):
      raise Exception("No migrations found")

    for file in files:
      print(self.__file_manager.read(file))
