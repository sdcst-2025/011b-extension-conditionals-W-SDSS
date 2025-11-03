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
print("Choose 1 or 2", end="")
choice = input()
if choice == "1":
    import _111
elif choice == "2":
    print("")
    print("You have wandered through the forest for the days, yet you can not find your way out.")
    print("")
    print("[bold red]GAME OVER[/bold red]")
else:
    print("[bold red]Error![/bold red] Swallowed by the darkness of the forest.")