import string 
import random
import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)

# TODO: read the JSON file and get the output filename and use it


def get_user_requirements():
    password_length = int(input("Enter you password length: "))
    special_char = input("With Special Charachter [y/n] ?").lower()
    with_duplicate = input("With Duplcation [y/n] ?").lower() 

    return password_length, special_char, with_duplicate

def get_allowed_charachter(special_char):
    charachter_db = string.ascii_letters + string.digits

    # Extend the charachter_db
    if special_char == "y":
        charachter_db += string.punctuation

    return charachter_db

def generate_password(with_duplicate, charachter_db, password_length ):
    if with_duplicate == "y":
        generated_password = random.choices(charachter_db, k = password_length)
    elif with_duplicate == "n":
        generated_password = random.sample(charachter_db, k = password_length)

    # Convert the list to a string string
    generated_password = "".join(generated_password)

    return generated_password

def export_password(generated_password):
    print_to_terminal(generated_password)
    save_to_file(generated_password)
   
def print_to_terminal(generated_password):
    print(generated_password) 

def save_to_file(generated_password):
    with open("./password.txt", mode = "w", encoding= "UTF-8") as file:
        file.write(generated_password)

def main():
 
    # 1. User inputs phase
    password_length, special_char, with_duplicate = get_user_requirements()


    # 2. Get Charachter DB
    charachter_db = get_allowed_charachter(special_char)

    # 3. Password generation phase
    generated_password = generate_password(with_duplicate,charachter_db ,password_length )

    # Export phase (Terminal, text file)
    export_password(generated_password)


main()
