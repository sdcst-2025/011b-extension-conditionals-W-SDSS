from rich import print
from os import system
system("clear||cls")

print("Welcome to the [bold dark_green]Forest of Confusion[/bold dark_green]!!")
print("You are lost in the forest.")
print("")
print("Which way to go?")
print("1. Go right into the slightly bright way")
print("2. Go left into the dark way")  
print("")

choice = input("Choose 1 or 2")
if choice == "1":
    import _1
elif choice == "2": 
    import _2
else:
    print("[bold red]Error![/bold red] Swallowed by the darkness of the forest.")