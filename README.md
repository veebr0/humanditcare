# HumandITcare - Technical solutions

## Show-off
take a look into the directory named showof, here you will find 3 files:

- fields.py: In this file is where the magic happens, two new classes add new features to Django model fields.
```python
class EncryptedEmailField (models.EmailField): 
    
class EncryptedCharField (models.CharField):
```
- encrypt.py, is a file that contains 2 important functions to encrypt and dencrypt.
```python
def encrypt(txt, unique=False)
def decrypt(txt, unique=False, fromdb=False)
```
- models.py, is just to show how you can implement the `EncryptedEmailField` and `EncryptedCharField` features into a model definition.

## Coding task
### Define Zeroes
The code for this task you will find it on directory **task_1**, this directory contains a file named: **first.py**


## Ship navigation - Part One / Part Two:
The code for this task you will find on directory **task_2**, this directory contains a file named: **second.py**

`note:` If you run this code you will get the following answers:

```python
ommand:F10| boat N10, S0, E100, W0, direcction=E
Command:N3| waypoint N4, S0, E10, W0, direcction=E
Command:F7| boat N38, S0, E170, W0, direcction=E
Command:R9| waypoint N0, S10, E4, W0, direcction=S
Command:F11| boat N0, S72, E214, W0, direcction=S
boat start point - x1: 10 | y1: 1
boat end   point - x2: 214 | y2: 72
Manhattan distance for task 1 = 18
Manhattan distance for task 2 = 275
```

## Last important things:
- Be aware that I used Python 3.10.4, and it has not been tested on higher versions.