#!/usr/bin/python

# This file illustrates the basic use of the bcrypt salted password 
# hash

import bcrypt

# The registerd password to hash and store (must be in bytes -- note the leading b)
password = b"hello"

########### GENERATE A SALTED HASH OF THE PASSWORD "hello" #############
# Generate the salt value
salt = bcrypt.gensalt()

# Hash the password + salt combination
hashed = bcrypt.hashpw(password, salt)

# Print the salted hash
print("The hash is: ", hashed)

####################################################################

print("**** Wrong password test **** ")

# Pretend that the user has entered the wrong password
wrongPassword = b"blah!"

# Verify if the password matches
if bcrypt.checkpw(wrongPassword, hashed):
    print("Passwords match!")
else:
    print("Passwords DO NOT match!")

########################################################################

print("**** Correct password test **** ")

# Pretend that the user has entered the correct password
correctPassword = b"hello"

# Verify if the password matches
if bcrypt.checkpw(correctPassword, hashed):
    print("Passwords match!")
else:
    print("Passwords DO NOT match!")

