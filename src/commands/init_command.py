import os

from commands.abs_command import AbstractCommand
from database.abs_database import DatabaseConnectionOpts
from database.database_factory import DatabaseFactory

class InitCommand(AbstractCommand):
  def __init__(self):
    super().__init__(
      "init",
      "Create '__migrations' table into the target database.",
      required_args_len=1
    )

  def handle(self, args: list[str]) -> None:
    self.validate_args_len(
      args,
      Exception("Invalid arguments, database name not provided")
    )

    database_name = args[0]
    database_opts = DatabaseConnectionOpts(
      os.getenv("DB_NAME") or database_name,
      os.getenv("DB_HOST") or "localhost",
      os.getenv("DB_USER") or "root",
      os.getenv("DB_PASS"),
      os.getenv("DB_PORT") or 5432
    )
    database = DatabaseFactory.Init(database_name, database_opts)
    database.prepare()
