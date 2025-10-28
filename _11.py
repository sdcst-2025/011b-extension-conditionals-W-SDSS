from rich import print
from os import system
system("clear||cls")

print("Your throat is refreshed, and your stamina has recovered.")
print(" ")
print("You can see a small cave on the opposite side.")
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