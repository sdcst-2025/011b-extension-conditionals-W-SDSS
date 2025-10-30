from rich import print
from os import system
system("clear||cls")

print("You chosen bright way.")
print(" ")
print("As you walked, you arrived at the [bright_cyan]river[/bright_cyan].")
print("You are thirsty.")
print("Would you drink the river water, or cross the river.")
print(" ")
print("1.drink water")
print("2.cross the river")
print(" ")
choice = input("Choose 1 or 2")
if choice == "1":
    import _11
elif choice == "2": 
    import _111
else:
    print("[bold red]Error![/bold red] Swallowed by the darkness of the forest.")