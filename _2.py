from rich import print
from os import system
system("clear||cls")

print("You chosen the dark way.")
print(" ")
print("It is so dark to down the road that you can not see anything.")
print("Do you want to walk carefully?")
print("Or do you want to run because you are scary?")
print("")

choice = input("Choose 1 if you walk. Choose 2 if you run.")
if choice == "1" :
 import _3
elif choice == "2": 
 import _4
else:
    import _2