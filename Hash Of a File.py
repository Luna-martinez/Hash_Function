#  A Function to create Hash of a file - In the HexDecimal Format.

import hashlib as hlib
def hash_file(filename):
    h = hlib.sha1()

    with open(filename, "rb")as file:
        chunk = 0
        while chunk != b"":
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()
message = hash_file("requirements.txt")
print(message)

# Hashes the name and returns the hash string

Expected_Output = "add564b5920b7f9ee6e97a5e836040a73f5efb3d"