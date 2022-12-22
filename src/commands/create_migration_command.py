import datetime

from commands.abs_command import AbstractCommand
from util.file_manager import FileManager

class CreateMigrationCommand(AbstractCommand):
  def __init__(self, file_manager: FileManager):
    super().__init__(command="create", required_args_len=1)
    self.__file_manager = file_manager

  def handle(self, args: list[str]) -> None:
    self.validate_args_len(
      args,
      Exception("Invalid arguments, filename not provided")
    )

    filename = args[0]
    timestamp = int(datetime.datetime.utcnow().timestamp())
    migration_filename = f"{timestamp}_{filename}.sql"
    file_path = self.__file_manager.create(migration_filename)

    print(f"Created new migration: ./{file_path}")
