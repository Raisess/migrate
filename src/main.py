#! /usr/bin/env python3

import datetime
import sys

from commands.abs_command import AbstractCommand
from commands.create_migration_command import CreateMigrationCommand
from database.abs_database import DatabaseConnectionOpts
from database.database_factory import DatabaseFactory
from util.file_manager import FileManager

DEFAULT_MIGRATION_DIR = "__migrations"

file_manager = FileManager(DEFAULT_MIGRATION_DIR)
create_migration_command = CreateMigrationCommand(file_manager)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    raise Exception(f"Invalid arguments, try {sys.argv[0]} command")

  command = sys.argv[1]
  arguments = AbstractCommand.SliceArguments(sys.argv)

  if command == "create":
    create_migration_command.handle(arguments)
  elif command == "run":
    if len(sys.argv) < 3:
      raise Exception(f"Invalid arguments, database name not provided")

    database_name = sys.argv[2]
    opts = DatabaseConnectionOpts("localhost", "user", "pass", 5432)
    database = DatabaseFactory.Init(database_name, opts)

    files = file_manager.list()
    for file in files:
      print(file_manager.read(file))
  else:
    raise Exception("Invalid command")
