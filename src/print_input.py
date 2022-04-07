#############################
# Collaborators: (enter people or resources who/that helped you)
# If none, write none
#
#
#############################

# Write code here:
name = input("Please enter your name: \n")
print(f"Hello {name}!")
fav = int(input("Please enter your favorite number: \n"))
print(f"Fun fact, your favorite number squared is {fav*fav}")
password = input("What would you like your password to be? \n")
entered = ""
while entered != password:
    i = 0
    for i in range(100):
        print("\n")
    entered = input("Please enter your password to access the rest of this code: \n\n\n\n\n\n\n\n\n\n\n")
print("Get scammed.")