SmartConfigParser
=================

SmartConfigParser add missing default value in ConfigParser module.

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

License
=======
SmartConfigParser's License is the WTFPL – Do What the Fuck You Want to Public License.

        DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

0. You just DO WHAT THE FUCK YOU WANT TO.



