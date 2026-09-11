import pyperclip
import os

FILE_NAME = "passwords.txt"

def save_password(website, username, password):
    with open(FILE_NAME, "a") as f:
        f.write(f"{website},{username},{password}\n")

def get_password(website):
    with open(FILE_NAME, "r") as f:
        for line in f:
            w, u, p = line.strip().split(",")
            if w == website:
                pyperclip.copy(p)
                print("Password copied to clipboard!")
                return
    print("Website not found.")

def main():
    while True:
        print("1. Save a password")
        print("2. Get a password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            website = input("Enter the website: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            save_password(website, username, password)
            print("Password saved successfully!")
        elif choice == "2":
            website = input("Enter the website: ")
            get_password(website)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()