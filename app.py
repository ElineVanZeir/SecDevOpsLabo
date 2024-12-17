print("Hello, Secure World!")

import hashlib


# Kwetsbare code (SAST trigger)
user_input = input("Enter something: ")
exec(user_input)  # Kwetsbaar voor code injection!

# Simpele hashing (voor SAST test)
print(hashlib.md5(b"example").hexdigest())

