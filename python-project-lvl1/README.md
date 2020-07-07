# Brain Games

A set of simple text math games launched from the console. Training project "Mind Games"

## How to run 

Deploy code for development or with minimal impact on the system

```
# clean installation without virtual environments  
$ git clone https://github.com/merkushov/hexlet.git merkushov-hexlet
$ cd merkushov-hexlet/python-project-lvl1

$ python3 -m brain_games.scripts.brain_calc
$ python3 -m brain_games.scripts.brain_even
$ python3 -m brain_games.scripts.brain_gcd
$ python3 -m brain_games.scripts.brain_prime
$ python3 -m brain_games.scripts.brain_progression

# ... or installation through package manager 'poetry'
$ git clone https://github.com/merkushov/hexlet.git merkushov-hexlet
$ cd merkushov-hexlet/python-project-lvl1

$ make install

$ poetry run brain-calc
$ poetry run brain-even
$ poetry run brain-gcd
$ poetry run brain-prime
$ poetry run brain-progression
```

Install as a local package

```
$ git clone https://github.com/merkushov/hexlet.git merkushov-hexlet
$ cd merkushov-hexlet/python-project-lvl1

$ python3 -m pip install .

$ brain_calc
$ brain_even
$ brain_gcd
$ brain_prime
$ brain_progression
```
