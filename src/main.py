#! /usr/bin/env python3

import sys

from commands.abs_command import AbstractCommand
from commands.create_migration_command import CreateMigrationCommand
from commands.run_migrations_command import RunMigrationsCommand
from util.file_manager import FileManager

DEFAULT_MIGRATION_DIR = "__migrations"

file_manager = FileManager(DEFAULT_MIGRATION_DIR)
create_migration_command = CreateMigrationCommand(file_manager)
run_migrations_command = RunMigrationsCommand(file_manager)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    raise Exception(f"Invalid arguments, try {sys.argv[0]} command")

  command = sys.argv[1]
  arguments = AbstractCommand.SliceArguments(sys.argv)

  if command == "create":
    create_migration_command.handle(arguments)
  elif command == "run":
    run_migrations_command.handle(arguments)
  else:
    raise Exception("Invalid command")
