from rich import print
from os import system
system("clear||cls")

print("You cross the river and arrived to the cave.")
print(" ")
print("As you walked through the dark cave, you came to a place briightly lit up by torches.")
print(" ")
print("There is a [yellow]treasure box[/yellow] bleaming with gold.")
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