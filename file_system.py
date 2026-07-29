import math
username = "Ahmad"
print(username)
print("Hello, ", username)


# >>> open('file_system.py')
# <_io.TextIOWrapper name='file_system.py' mode='r' encoding='cp1252'>
# >>> f = open('file_system.py')
# >>> f.readline() 
# 'import math\n'
# >>> f.readline()
# 'username = "Ahmad"\n'
# >>> f.readline()
# 'print(username)\n'
# >>> f.readline()
# 'print("Hello, ", username)'
# >>> f.readline()
# ''
# >>> f.readline()
# ''
# >>> f = open('file_system.py')
# >>> f.__next__()
# 'import math\n'
# >>> f.__next__()
# 'username = "Ahmad"\n'
# >>> f.__next__()
# 'print(username)\n'
# >>> f.__next__()
# 'print("Hello, ", username)'
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     f.__next__()
#     ~~~~~~~~~~^^
# StopIteration
# >>> for linr in open('file_system.py'):
# ...     print(line)
# ... 
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
#     print(line)
#           ^^^^
# NameError: name 'line' is not defined. Did you mean: 'linr'?
# >>> for linr in open('file_system.py'):
# ... print(line)
#   File "<stdin>", line 2
#     print(line)
#     ^^^^^
# IndentationError: expected an indented block after 'for' statement on line 1
# >>> for line in open('file_system.py'):
# ... print(line)
#   File "<stdin>", line 2
#     print(line)
#     ^^^^^
# IndentationError: expected an indented block after 'for' statement on line 1
# >>> for line in open('file_system.py'):
# ...     print(line)
# ... 
# import math

# username = "Ahmad"

# print(username)

# print("Hello, ", username)
# >>> f = open('file_system.py')
# >>> while true:
# ...     line = f.readline()
# ...     if not line: break
# ...     print(line)
# ... 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     while true:
#           ^^^^
# NameError: name 'true' is not defined. Did you mean: 'True'?
# >>> while True:            
# ...     line = f.readline()
# ...     if not line: break    
# ...     print(line)
# ... 
# import math

# username = "Ahmad"

# print(username)

# print("Hello, ", username)