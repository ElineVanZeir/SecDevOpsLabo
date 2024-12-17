print("Hello, Secure World!")

import hashlib

# Hardcoded wachtwoorden (detecteerbaar door scanners)
PASSWORD = "SuperSecret123!"  # Simpele hardcoded wachtwoord
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"  # AWS access key format
GITHUB_TOKEN = "ghp_1a2b3c4d5e6f7g8h9ijklmnopqrstuvwxyz1234"  # GitHub token format
API_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"  # Stripe API key format
DB_PASSWORD = "postgres://username:password@localhost:5432/dbname"  # Database URL format met wachtwoord

# Kwetsbare code (SAST trigger)
user_input = input("Enter something: ")
exec(user_input)  # Kwetsbaar voor code injection!

# Simpele hashing (voor SAST test)
print(hashlib.md5(b"example").hexdigest())
