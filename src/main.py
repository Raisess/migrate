#! /usr/bin/env python3

import datetime
import sys

from database.abs_database import DatabaseConnectionOpts
from database.database_factory import DatabaseFactory
from util.file_manager import FileManager

DEFAULT_MIGRATION_DIR = "__migrations"

if __name__ == "__main__":
  if len(sys.argv) < 2:
    raise Exception(f"Invalid arguments, try {sys.argv[0]} command")

  fm = FileManager(DEFAULT_MIGRATION_DIR)

  command = sys.argv[1]
  if command == "create":
    if len(sys.argv) < 3:
      raise Exception(f"Invalid arguments, filename not provided")

    filename = sys.argv[2]
    timestamp = int(datetime.datetime.utcnow().timestamp())
    migration_filename = f"{timestamp}_{filename}.sql"
    fm.create(migration_filename)

    print(f"Created new migration: ./{DEFAULT_MIGRATION_DIR}/{migration_filename}")
  elif command == "run":
    if len(sys.argv) < 3:
      raise Exception(f"Invalid arguments, database name not provided")

    database_name = sys.argv[2]
    opts = DatabaseConnectionOpts("localhost", "user", "pass", 5432)
    database = DatabaseFactory.Init(database_name, opts)

    files = fm.list()
    for file in files:
      print(fm.read(file))
  else:
    raise Exception("Invalid command")
