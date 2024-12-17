import hashlib
import os
import sqlite3
import requests
import sys

print("Hello, Secure World!")

# Mock de API-aanroep als 'CI' wordt gedetecteerd
RUNNING_IN_CI = os.getenv("CI") == "true"

# Hardcoded secrets (detecteerbaar door scanners)
PASSWORD = "SuperSecret123!"
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"
GITHUB_TOKEN = "ghp_1a2b3c4d5e6f7g8h9ijklmnopqrstuvwxyz1234"
API_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
DB_PASSWORD = "postgres://username:password@localhost:5432/dbname"

# Kwetsbare code (SAST trigger)
user_input = input("Enter something: ")
exec(user_input)  # Kwetsbaar voor code injection!

# Onveilige hashing
password = "user_password123"
hashed_password = hashlib.md5(password.encode()).hexdigest()
print(f"MD5 Hash van wachtwoord: {hashed_password}")

# SQL-injectie
db_connection = sqlite3.connect(":memory:")
cursor = db_connection.cursor()
cursor.execute("CREATE TABLE users (id INTEGER, username TEXT, password TEXT);")
username = input("Voer een gebruikersnaam in:")
query = f"SELECT * FROM users WHERE username = '{username}';"
cursor.execute(query)
print("User data retrieved:", cursor.fetchall())

# Bestandsoperatie
filename = input("Voer een bestandsnaam in:")
with open(f"/tmp/{filename}", "r") as f:
    print(f.read())

# Mock API-aanroep
if RUNNING_IN_CI:
    print("Skipping API call in CI environment. Returning mock response.")
    response_status = 200
else:
    response = requests.get(
        "https://api.example.com/data",
        headers={"Authorization": "Bearer sk_test_4eC39HqLyjWDarjtT1zdp7dc"},
    )
    response_status = response.status_code

print("API Response:", response_status)

# Onveilige eval
expression = input("Voer een uitdrukking in:")
result = eval(expression)
print(f"Resultaat: {result}")
