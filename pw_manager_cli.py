
from getpass import getpass
import json
import os 

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

def add():
    website = input("Website / App: ")
    username = input("Username: ")
    password = getpass("Password: ")
    pw = {
        "website": website,
        "username": username,
        "password": password
    }
    pws.append(pw)
    dump_pws()
    

def view():
    if not pws:
        print ("No password stored to view")
        return
    else:
        for i, pw in enumerate(pws):
            print (f'\n{i+1}. Website: {pw["website"]} | Password: {pw["password"]} ')
        
def search():
    search_key = input("Which web/app pw do you want to search? ").lower()

    found = False

    for pw in pws:
        if pw["website"].lower() == search_key:
            print(f"Username: {pw['username']}")
            print(f"Password: {pw['password']}")
            found = True
            break

    if not found:
        print("Password not found") 
         
def delete():
    if not pws:
        print ("No pw available to delete")
        return
    while True:
        view()
        try:
            delete_num = int(input("Enter the number of pw you want to delete: "))
            pws.pop(delete_num-1)
            break
        except ValueError:
            print("\nEnter valid number")
    dump_pws()
    
while True:
    try:
        menu_chosen = int(input("\n------Menu------\n1.Add Password \n2.View Password \n3.Search Password \n4.Delete Password \n5.Exit\n"))
        if menu_chosen == 1:
            add()
        elif menu_chosen == 2:
            view()
        elif menu_chosen == 3:
            search()
        elif menu_chosen == 4:
            delete()
        elif menu_chosen == 5:
            break
        else:
            print("Please enter a valid number from 1 to 5")
    except ValueError:
        print ("Please enter a valid number from 1 to 5")
    

