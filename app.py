import string 
import random

# TODO: Extend the script to garantee if the user special charachter wishes --> the choices, sample should have also sepcial charachter
# TODO: allow the user to enter y or yes / n or no

charachter_db = string.ascii_letters + string.digits


# User inputs phase
password_length = int(input("Enter you password length: "))
special_char = input("With Special Charachter [y/n] ?").lower() 
with_duplicate = input("With Duplcation [y/n] ?").lower()


# Extend the charachter_db
if special_char == "y":
    charachter_db += string.punctuation  

# Password generation phase
if with_duplicate == "y":
    generated_password = random.choices(charachter_db, k = password_length)
elif with_duplicate == "n":
    generated_password = random.sample(charachter_db, k = password_length)

# Convert the list to a string string
generated_password = "".join(generated_password)

# Export phase (Terminal, text file)
print(generated_password)