from rich import print
from os import system
system("clear||cls")

print("Gasping for breath, you struggled ashore,tossed around by the raging current.")
print("")
print("While catching your breath, you find small cave.")
print("You decided to enter the cave curiosity.")
print("")
print("As you walked through the dark cave, you came to a place briightly lit up by torches.")
print(" ")
print("There is a treasure box bleaming with gold.")
print("Would you open it, or it might be cursed box so avoid it.")
print("1.Open the box")
print("2.Avoid it and head toward exit")
print(" ")

choice = input("Choose 1 or 2")
if choice == "1":
    import _1111
elif choice == "2": 
    import _1112
else:
    print("[bold red]Error![/bold red] Swallowed by the darkness of the forest.")