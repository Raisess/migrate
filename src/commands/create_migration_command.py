import datetime
from yacli import Command

from util.file_manager import FileManager

class CreateMigrationCommand(Command):
  def __init__(self, file_manager: FileManager):
    super().__init__(
      "create",
      "Create a new '.sql' file into migrations directory.",
      args_len=1
    )
    self.__file_manager = file_manager

  def handle(self, args: list[str]) -> None:
    filename = args[0]
    timestamp = int(datetime.datetime.utcnow().timestamp())
    migration_filename = f"{timestamp}_{filename}.sql"
    file_path = self.__file_manager.create(migration_filename)

    print(f"Created new migration: ./{file_path}")
