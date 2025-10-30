from rich import print
from os import system
system("clear||cls")

print("You run as fast as you can.")
print("But the bear is following you from behind.")
print("Finally, you got trappd with river at your back.")
print("")
print("1.Stay and fight.")
print("2.Jump into the river")  
print("")

choice = input("Choose 1 or 2")
if choice == "1":
 print(" ")
 print("It was reckless to challenge bear...")
 print(" ")
 print("[bold red]GAME OVER[/bold red]")
elif choice == "2": 
    import _212
else:
    print("[bold red]Error![/bold red] Swallowed by the darkness of the forest.")