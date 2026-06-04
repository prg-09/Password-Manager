
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
            print (f'\n{i+1}. Website: {pw["website"]} | Username: {pw["username"]}')
        
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
                new_website = input(f"Website(Current:{pw["website"]}): ")
                new_username = input(f"Username(Current:{pw["username"]}): ")
                
                new_password = input(f"Passowrd: ")
                if new_website :
                    pw["website"] = new_website
                
                if new_username :
                    pw["username"] = new_username
                    
                if new_password :
                    pw["password"] = new_password
           
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
                break
            else:
                print("Enter valid integer")
            
        except ValueError:
            print("\nEnter number")
    dump_pws()
    
while True:
    try:
        menu_chosen = int(input("\n------Menu------\n1.Add Password \n2.View Password \n3.Search Password \n4.Edit \n5.Delete Password \n6.Exit\n"))
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
    

