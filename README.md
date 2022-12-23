# Migrate

A simple CLI to manage database migrations.

## Available databases

- [x] Sqlite
- [ ] PostgreSQL
- [ ] MariaDB
- [ ] MySQL

## Commands

### `init`:

Create `__migrations` table into the target database.

E.g.:

```shell
$ migrate init database
```

### `create`:

Create a new `.sql` file into migrations directory.

E.g.:

```shell
$ migrate create migration-name
```

### `run`:

Run all `.sql` files from the migrations directory into the target database.

E.g.:

```shell
$ migrate run database
```

### `help`:

Show commands description.

E.g.:

```shell
$ migrate help
```
