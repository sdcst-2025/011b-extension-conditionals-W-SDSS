from rich import print
from os import system
system("clear||cls")

print("You cross the river and arrived to the cave.")
print(" ")
print("As you walked through the dark cave, you came to a place briightly lit up by torches.")
print(" ")
print("1.walk toward the cave")
print("2.keep walking along the river")
print(" ")

choice = input("Choose 1 or 2")
if choice == "1":
    import _111
elif choice == "2": 
    import _112
else:
    print("[bold red]Error![/bold red] Swallowed by the darkness of the forest.")