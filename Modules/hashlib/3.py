import hashlib

data = [b'bardia123' , b'amir456' , b'ho3ein789']

for d in data:
    print(hashlib.sha256(d).hexdigest())
