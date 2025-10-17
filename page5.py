from rich import print
from os import system
system("clear||cls")

print("[bold red]Page 5: Introduction to colors!")
print("")
print("[bold cyan underline]We[/bold cyan underline] can add [bold yellow underline]multiple[/bold yellow underline] colors on a line")
print("")
choice = input("Where do you want to go next? (hint: type in a 2)")
if choice == "2":
    import page2
else:
    import page1