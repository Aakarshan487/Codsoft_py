import random
import string

print("!!!WELCOME TO PASSWORD GENERATOR!!!")
print()
print("WE HELP YOU TO CREATE THE STRONGEST PASSWORD IN THE WORLD")
print()
again = "s"

while again == "s":
    length = int(input("Enter length of password you want:"))
    if length >= 4: 
        possible_letters = string.ascii_letters+string.digits+string.punctuation
        passw = ''.join(random.choices(possible_letters,k=length))
        print()
        print("Generated Password:",passw)
        print()
        again=input("Do you want to generate again(press 's'):").lower()
    else:
        print("Please enter the length more than 3, password under 4 letters is  very weak")
        again=input("Do you want to generate again(press 's'):").lower()
print()
