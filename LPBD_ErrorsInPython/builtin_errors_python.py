# Built-in errors in Python:
# IndexError
# KeyError
# Name Error
# AttributeError
# NotImplementedError
# RunTimeError
# SyntaxError
# IndentationError
# TabError
# TypeError
# ValueError
# ImportError
# DepricationWarnings

# IndexError: list index out of range -> when trying access index that not exist.
# KeyError: 'release' -> when the key used is not correct or not exist (dictionaries).
# NameError: name 'hello' is not defined -> when the variable not defined.
# AttributeError: 'list' object has no attribute 'interaction' -> when something wrong with object attributes like using attribute set object with list
# NoImplementedError -> used when code under development and when a method not implemented yet it can raise a not implemented error to explain to other users:
    # def login(self):
      # raise NotImplementedError('This feature has not been implemented yet.')
# RuntimeError -> generic error when running the program
# SyntaxError -> Error occurred when parsing the program -> illegal syntax
# IndentationError -> error raised when indentation was done incorrectly
# TabError -> error raised when switching editors, when mixed indentations used (spaces and/or tabs)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'  -> when trying to do operation like add between 2 different types like integer and string
# ValueError -> int('20.5'): ValueError: invalid literal for int() with base 10: '20.5' -> when giving a wrong value for correct type
# ImportError
