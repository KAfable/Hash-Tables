import hashlib

n = 10
key = b'my_value'
key2 = 'string'.encode()
key3 = b'lunchtime'
key4 = b'lunchtime'

index = hash(key) % 8
index2 = hash(key2) % 8
index3 = hash(key3) % 8
# index4 = hashlib.sha256(key4).hexdigest() % 8

print(index)
print(index2)
print(index3)

# a string is a object in python, it has a metadata associated with it
# for i in range(n):
#     print(hash(key))
