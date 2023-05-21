"""
1. Prompts the user to enter two options:
   (1) create an account; 
   (2) login into the existing account.
2. If the user chooses option (1), they are prompted to select a user name and a password. 
   The program will then check file called db.txt that has the following format: each line 
   consists of the user name, space separator, and the salted hashed password (computed using 
   the bcrypt library) associated with the user.
"""
import bcrypt
import pwinput

def create_account():
    """
    This function creates a new account for the user
    """
    username = input("Please enter the username: ")
    password = pwinput.pwinput(prompt="Please enter the password: ")

    # Generate the salt value
    salt = bcrypt.gensalt()

    # Hash the password + salt combination
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)

    # Print the salted hash
    print("The hash is: ", hashed)

    # Store the username and hashed password in the file
    with open("db.txt", "a") as f:
        f.write(username + ":" + hashed.decode() + "\n")
    print("Your account was successfully created!")

def login():
    """
    This function logs the user into the system
    """
    username = input("Please enter your registered username: ")
    password = pwinput.pwinput(prompt = "Please enter your password: ")

    # Read the file to check if the username and password match
    with open("db.txt", "r") as f:
        for line in f:
            # Split the line into the username and password
            (user, hashed) = line.strip().split(":")
            # Check if the username matches
            if user == username:
                # Check if the password matches
                if bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8")):
                    print(f"Welcome {user}")
                    return
                else:
                    print("Access Denied")
                    return
    print("Username not found!")

def main():
    """
    This is the main function
    """
    option = input("Choose (1) to create an account or; (2) To login into an existing account: ")
    if option == "1":
        create_account()
    elif option == "2":
        login()
    else:
        print("Invalid option!")

if __name__ == "__main__":
    main()