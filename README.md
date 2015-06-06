SmartConfigParser
=================

SmartConfigParser add missing default value in ConfigParser module. It use RawConfigParser module from ConfigParser. 

```python
from smartconfigparser import Config

config = Config()
config.read('config.ini')

user = config.get('SECTION', 'user', 'Guillaume')
age = config.getint('SECTION', 'age', 28)
weight = config.getfloat('SECTION', 'weight', 80.2)
is_developer = config.getboolean('SECTION', 'is_developer', True)
hobbies = config.getlist('SECTION', 'hobbies', ['diving', 'making software'])

# if SECTION does not exist in config.ini get default values
print(user, age, weight, is_developer, hobbies)
# ('Guillaume', 28, 80.2, True, ['diving', 'making software'])

```


Installation
============

Install it with pip:

    pip install smartconfigparser


Requirements
============

Work with python 2.7 and python 3.4

Tested with python 2.7.10 and python 3.4.3


Usage
=====

## smartconfigparser.get

config.get(section, option, default_value)

same as ConfigParser.get() method except that it return default value if section or option does not exists
    
    
## smartconfigparser.getint


config.getint(section, option, default_value)

same as ConfigParser.getint() method except that it return default value if section or option does not exists


## smartconfigparser.getfloat


config.getfloat(section, option, default_value)

same as ConfigParser.getfloat() method except that it return default value if section or option does not exists



## smartconfigparser.getboolean

config.getboolean(section, option, default_value)

same as ConfigParser.getboolean() method except that it return default value if section or option does not exists


## smartconfigparser.getlist

config.getlist(section, option, default_list)

Return a list of the words in the option value, using comma (',') as the delimiter string

config.ini file 

    [section]
    list = a,b,c

example 

```python
print(config.getlist('section', 'list', []))
# ['a', 'b', 'c']
print(config.getlist('section_does_not_exists', 'list', []))
# []
```

## smartconfigparser.set

config.set(section, option, value)

same as ConfigParser.set() method except that it create section if section does not exists

example 

```python
from smartconfigparser import Config

config = Config()
config.set('section_does_not_exist', 'user', 'Guillaume Vincent')
with open('config.ini', 'wt') as configfile:
    config.write(configfile)
```

config.ini

    [section_does_not_exist]
    user = Guillaume Vincent

Test
====

install smartconfigparser

    pip install smartconfigparser

run tests

    cd tests
    python test_smartconfigparser.py
    
Example
=======

## DATABASE dict in django settings file

```python
from smartconfigparser import Config

config = Config()
config.read('config.ini')

DATABASES = {
    'default': {
        'ENGINE': config.get('DATABASE', 'engine', 'django.db.backends.postgresql_psycopg2'),
        'NAME': config.get('DATABASE', 'name', 'oslab'),
        'USER': config.get('DATABASE', 'user', 'oslab'),
        'PASSWORD': config.get('DATABASE', 'password', ''),
        'HOST': config.get('DATABASE', 'host', ''),
        'PORT': config.get('DATABASE', 'port', ''),
    }
}
```

config.ini file for a developer

    [DATABASE]
    engine = django.db.backends.sqlite3
    name = db.sqlite3

config.ini file for production server
    
    [DATABASE]
    user = postgres_db_user
    password = very_strong_password
    host = localhost
    port = 5432

## ALLOWED_HOSTS list in django settings file

```python
ALLOWED_HOSTS = config.getlist('DJANGO', 'allowed_hosts', ['localhost', '127.0.0.1'])
```

config.ini file for production server

    [DJANGO]
    allowed_hosts=127.0.0.1,localhost,*.example.com
    
    
License
=======
SmartConfigParser's License is the WTFPL – Do What the Fuck You Want to Public License.

        DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

0. You just DO WHAT THE FUCK YOU WANT TO.



