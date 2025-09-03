# Write your code here

# HINT: create a dictionary from flowers.txt
def getName():
    name = input("Enter your First [space] Last name only: ")
    return name
# HINT: create a function to ask for user's first and last name

theDict = dict()
with open("flowers.txt", "r") as f:
    for line in f:
        toAdd = line.split(":", 1)
        theDict[toAdd[0]] = toAdd[1].strip()

name = getName()
first_letter = name.strip()[0].upper()

message = "Unique flower name with the first letter: {}".format(theDict[first_letter])
print(message)

# print the desired output

