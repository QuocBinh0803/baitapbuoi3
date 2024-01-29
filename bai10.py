# list()
# a = 'spam'
# b = list(a)
# print(b)

# split()
# a = 'spam spam spam'
# b = a.split()
# print(b)

# split()
# a = 'spam - spam1 - spam2'
# delimiter = '-'
# b = a.split(delimiter)
# print(b)

# split()
# a = 'spam - spam1 - spam2'
# delimiter = 'a'
# b = a.split(delimiter)
# print(b)

# joint()
a = 'spam - spam1 - spam2'
delimiter = 'a'
b = a.split(delimiter)
print(b)
print(delimiter.join(b))