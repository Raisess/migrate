#! /usr/bin/env python3

from yacli import CLI

from commands.create_migration_command import CreateMigrationCommand
from commands.init_command import InitCommand
from commands.run_migrations_command import RunMigrationsCommand
from util.file_manager import FileManager

DEFAULT_MIGRATION_DIR = "__migrations"

if __name__ == "__main__":
  file_manager = FileManager(DEFAULT_MIGRATION_DIR)
  cli = CLI("migrate", [InitCommand(), CreateMigrationCommand(file_manager), RunMigrationsCommand(file_manager)])
  cli.handle()
