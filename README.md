# Migrate

A simple CLI to manage database migrations.

## Available databases

- [x] Sqlite
- [x] PostgreSQL
- [x] MySQL

## Enviroment variables

#### `DB_NAME`:

Stores the current database name.

#### `DB_HOST`:

Stores the current database host.

#### `DB_USER`:

Stores the current database user.

#### `DB_PASS`:

Stores the current database password.

#### `DB_PORT`:

Stores the current database port.

### Usage:

E.g.:

```shell
$ DB_NAME=name DB_PASS=password DB_PORT=5432 migrate init database
```

## Commands

#### `init`:

Create `__migrations` table into the target database.

E.g.:

```shell
$ migrate init database
```

- Need env variables.

#### `create`:

Create a new `.sql` file into migrations directory.

E.g.:

```shell
$ migrate create migration-name
```

#### `run`:

Run all `.sql` files from the migrations directory into the target database.

E.g.:

```shell
$ migrate run database
```

- Need env variables.

#### `help`:

Show commands description.

E.g.:

```shell
$ migrate help
```
