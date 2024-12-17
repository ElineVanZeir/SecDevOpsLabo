print("Hello, Secure World!")

import hashlib
import os
import sqlite3
import requests

# Hardcoded wachtwoorden en secrets (detecteerbaar door scanners)
PASSWORD = "SuperSecret123!"  # Simpele hardcoded wachtwoord
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"  # AWS access key format
GITHUB_TOKEN = "ghp_1a2b3c4d5e6f7g8h9ijklmnopqrstuvwxyz1234"  # GitHub token format
API_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"  # Stripe API key format
DB_PASSWORD = "postgres://username:password@localhost:5432/dbname"  # Database URL format met wachtwoord

# Kwetsbare code (SAST trigger: Code Injection)
user_input = input("Enter something: ")
exec(user_input)  # Kwetsbaar voor code injection!

# Onveilige hashing (MD5 is verouderd en kwetsbaar)
password = "user_password123"
hashed_password = hashlib.md5(password.encode()).hexdigest()
print(f"MD5 Hash van wachtwoord: {hashed_password}")

# SQL-injectie (Kwetsbare database query)
db_connection = sqlite3.connect(":memory:")
cursor = db_connection.cursor()
cursor.execute("CREATE TABLE users (id INTEGER, username TEXT, password TEXT);")

print("Voer een gebruikersnaam in:")
username = input()
query = f"SELECT * FROM users WHERE username = '{username}';"  # SQL-injection kwetsbaarheid!
cursor.execute(query)
print("User data retrieved:", cursor.fetchall())

# Onveilige bestandsoperatie (Path Traversal)
print("Voer een bestandsnaam in:")
filename = input()
with open(f"/tmp/{filename}", "r") as f:  # Path traversal mogelijk!
    print(f.read())

# Hardcoded API Call met gevoelig token
response = requests.get(
    "https://api.example.com/data",
    headers={"Authorization": "Bearer sk_test_4eC39HqLyjWDarjtT1zdp7dc"},  # Gevoelige API-key
)
print("API Response:", response.status_code)

# Onveilige random generator voor cryptografie
import random
secret_key = "".join([str(random.randint(0, 9)) for _ in range(16)])  # Niet cryptografisch veilig
print(f"Generated secret key: {secret_key}")

# Onveilige gebruik van eval()
print("Voer een uitdrukking in:")
expression = input()
result = eval(expression)  # Kwetsbaar voor code execution!
print(f"Resultaat: {result}")
