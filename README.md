# Password Manager 🔐
 
A command-line password manager built in Python that stores, encrypts, and manages passwords for websites and apps.
 
## Features
 
- **Add** passwords with a username and website
- **View** all stored passwords
- **Search** for a specific password by website
- **Edit** existing passwords
- **Delete** passwords
- **Password Generator** — generates a secure random password
- **Password Strength Checker** — rates your password and forces re-entry if too weak
- **Duplicate Detection** — warns you if a password for that website already exists
- **Encryption** — all passwords are encrypted using Fernet symmetric encryption
## Requirements
 
- Python 3.x
- `cryptography` library
Install dependencies:
 
```bash
pip install cryptography
```
 
## Usage
 
Run the script:
 
```bash
python password_manager.py
```
 
You'll be presented with a menu:
 
```
------Menu------
1. Add Password
2. View
3. Search
4. Edit
5. Delete
6. Exit
```
 
## How It Works
 
**Encryption** — passwords are encrypted using the `cryptography` library's Fernet module. A key is generated on first run and saved to `key.key`. The same key is reused on every run to decrypt existing passwords.
 
**Storage** — passwords are saved in `pw.json` as a list of objects containing the website, username, and encrypted password.
 
**Password Strength** — when manually entering a password, it is scored based on five rules: uppercase letters, lowercase letters, digits, special characters, and minimum length of 10. Passwords scoring below 3 rules are rejected and the user is asked to re-enter.
 
**Password Generator** — uses Python's `secrets` module for cryptographically secure random password generation.
 
## File Structure
 
```
password_manager.py   # main script
pw.json               # stores encrypted passwords (auto-created)
key.key               # encryption key (auto-created)
```
 
## Security Notes
 
> ⚠️ Keep `key.key` safe. If it is lost, your saved passwords cannot be decrypted. If someone gets both `key.key` and `pw.json`, they can decrypt all your passwords.
 
> ⚠️ Do not share or commit `key.key` or `pw.json` to version control. Add them to `.gitignore`.
 
## .gitignore
 
Make sure to add these to your `.gitignore`:
 
```
key.key
pw.json
```
 