#! /usr/bin/env python3

import datetime
import sys

from database import DatabaseConnectionOpts
from databases.postgres_impl import Postgres
from file_manager import FileManager

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
    opts = DatabaseConnectionOpts("localhost", "user", "pass", 5432)
    database = Postgres(opts)

    files = fm.list()
    for file in files:
      print(fm.read(file))
  else:
    raise Exception("Invalid command")
