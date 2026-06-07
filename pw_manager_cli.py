
from getpass import getpass
import json
import os 
import string
import random
from cryptography.fernet import Fernet

pws = []

def load_pws():
    if os.path.exists("pw.json"):
        with open ("pw.json") as f:
            return json.load(f)
    else:
        return []
    
pws = load_pws()

def dump_pws():
    with open ("pw.json","w") as f:
        json.dump(pws,f, indent= 4)


def pw_generator(length = 10):
    characters = (string.ascii_letters + string.punctuation + string.digits)
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    print(f"Generated pw is {password}")
    return password


def pw_strength_checker(password):
    while True:
        special_chars = string.punctuation
        has_uppercase = any(char.isupper() for char in password)
        has_lowercase  = any (char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password) 
        has_symbol = any(char in special_chars for char in password)
        has_min_length = len(password) >= 10
        rules = [has_uppercase,has_lowercase,has_digit,has_symbol, has_min_length]
        
        score = sum(rules)
        
        if all(rules):
            print("Strong Password")
            break
        elif score >= 3:
            print ("Moderate Password")
            break
        else:
            print("Weak Password")
            password = getpass("Please enter strong password:")
            
    return password
        

def add():
    website = input("Website / App: ")
    username = input("Username: ")
    while True:
        choice = input("Do you want to generate password instead of typing yourself?(y/n): ")
        
        if choice.lower() == "y":
            password = pw_generator()
            break
        elif choice.lower() == "n":
            password = getpass("Password:")
            password = pw_strength_checker(password)
            
            break
        else:
            print("Please enter y or n")
    pw = {
        "website": website,
        "username": username,
        "password": encrypt_password(password)
    }
    
    pws.append(pw)
    dump_pws()


def view():
   
    if not pws:
        print ("No password stored to view")
        return
    else:
        for i, pw in enumerate(pws):
            print (f'\n{i+1}. Website: {pw["website"]} | Username: {pw["username"]} ')
    
    
def search():
    search_key = input("Which web/app pw do you want to search? ").lower()

    found = False
    
    for pw in pws:
        
        if search_key in pw["website"].lower():
            print(f"Website: {pw['website']}")
            print(f"Username: {pw['username']}")
            real_password = decrypt_password(pw["password"])
            print(f"Password: {real_password}")
            found = True
            break

    if not found:
        print("Password not found") 


def edit():
    
    if not pws:
        print("No pw stored")
        return
    view()
    while True:
        try:
            edit_num = int(input("Enter the no of pw you want to edit: "))
            if 1 <= edit_num <= len(pws):
                pw = pws[edit_num - 1]
                print("Press enter if you don't want to update")
                new_website = input(f"Website(Current:{pw['website']}): ")
                new_username = input(f"Username(Current:{pw['username']}): ")
                new_password = input(f"Password: ")
                
                if new_website :
                    pw["website"] = new_website
                
                if new_username :
                    pw["username"] = new_username
                    
                if new_password :
                    pw["password"] = encrypt_password(new_password)
           
                dump_pws()
                break
            else:
                print("Enter a valid integer")
        except ValueError:
            print("Enter an integer")    
            
     
def delete():
    if not pws:
        print ("No pw available to delete")
        return
    while True:
        view()
        try:
            
            delete_num = int(input("Enter the number of pw you want to delete: "))
            if 1 <= delete_num <= len(pws): 
                deleted = pws.pop(delete_num-1)
                print(f"Succesfully deleted pw of {deleted['website']} ")
                dump_pws()
                break
            else:
                print("Enter valid integer")

        except ValueError:
            print("\nEnter number")


def load_key():
    if os.path.exists("key.key"):
        with open("key.key", "rb") as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open("key.key", "wb") as f:
            f.write(key)
        return key


key = load_key()
fer = Fernet(key)


def encrypt_password(password):
    encrypted_password = fer.encrypt(password.encode()).decode()
    return encrypted_password


def decrypt_password(encrypted_password):
    decrypted_password = fer.decrypt(encrypted_password.encode()).decode()
    return decrypted_password


    
while True:
    try:
        menu_chosen = int(input("\n------Menu------\n1.Add Password \n2.View \n3.Search \n4.Edit \n5.Delete \n6.Exit\n"))
        if menu_chosen == 1:
            add()
        elif menu_chosen == 2:
            view()
        elif menu_chosen == 3:
            search()
        elif menu_chosen == 4:
            edit()
        elif menu_chosen == 5:
            delete()
        elif menu_chosen == 6:
            break
        else:
            print("Please enter a valid number from 1 to 6")
    except ValueError:
        print ("Please enter a number from 1 to 6")
    

