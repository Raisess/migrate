#! /usr/bin/env python3

import sys

from commands.abs_command import AbstractCommand
from commands.create_migration_command import CreateMigrationCommand
from commands.init_command import InitCommand
from commands.help_command import HelpCommand
from commands.run_migrations_command import RunMigrationsCommand
from util.file_manager import FileManager

DEFAULT_MIGRATION_DIR = "__migrations"

file_manager = FileManager(DEFAULT_MIGRATION_DIR)
help_command = HelpCommand()
init_command = InitCommand()
create_migration_command = CreateMigrationCommand(file_manager)
run_migrations_command = RunMigrationsCommand(file_manager)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    raise Exception(f"Invalid arguments, try {sys.argv[0]} command")

  commands = [init_command, create_migration_command, run_migrations_command, help_command]
  help_command.attach_commands(commands)

  command = sys.argv[1]
  arguments = AbstractCommand.SliceArguments(sys.argv)

  command_found = False
  for command_instance in commands:
    if command_instance.get_command() == command:
      command_found = True
      command_instance.handle(arguments)

  if not command_found:
    raise Exception("Invalid command")
