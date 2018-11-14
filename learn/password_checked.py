import sys
import os
password = input("Pleas enter the password: ")
attempt_count = 1
MASTER_PASSWORD = 'openv'
while password != MASTER_PASSWORD:
    password = input("Invalid password, try again: ")
    attempt_count += 1
    if attempt_count >= 3:
        print(attempt_count)
        os._exit(1)
        
    

print("Welcome to secret town")