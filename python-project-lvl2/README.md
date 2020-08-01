# Gendiff

A console utility for comparing two files with each other.

## How to run

Deploy code for development or with minimal impact on the system

```
# clean installation without virtual environment
$ git clone https://github.com/merkushov/hexlet.git merkushov-gendiff
$ cd merkushov-gendiff/python-project-lvl2

$ python3 -m gendiff.scripts.gendiff --help

# ... or installation through package manager 'poetry' (for developing)
$ git clone https://github.com/merkushov/hexlet.git merkushov-gendiff
$ cd merkushov-gendiff/python-project-lvl2

$ make install

$ poetry run gendiff --help
$ poetry run gendiff before.json after.json
```

Install as a local package

```
$ git clone https://github.com/merkushov/hexlet.git merkushov-gendiff
$ cd merkushov-gendiff/python-project-lvl2

$ python3 -m pip install .

$ gendiff --help
$ gendiff before.json after.json -f plain
```

## Example of application launch

```
$ gendiff ./tests/fixtures/a.json ./tests/fixtures/b.json 
{
    "host":localhost,
  - "port":5432,
  + "port":3306,
    "replication":{
        "books":master,
      + "users":master,
    }
  - "software":PostgreSQL,
  + "software":MySQL,
}

$ gendiff ./tests/fixtures/a.json ./tests/fixtures/b.json -f plain
Setting "port" changed from "5432" to "3306".
Setting "replication.users" added with value "master".
Setting "software" changed from "PostgreSQL" to "MySQL".

```
