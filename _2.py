from rich import print
from os import system
system("clear||cls")

print("You chosen the dark way.")
print(" ")
print("It is so dark to down the road that you can not see anything.")
print("After waking for a while, [red]you hear the growl of beast[/red].")
print(" ")
print("A [#842C00]bear[/#842C00] appeared.")
print("Your eyes met[#FFFFFF]...[/#FFFFFF]what now?")
print("")
print("Choose 1 if you run away. Choose 2 if you fight.",end="")
choice = input()
if choice == "1" :
 import _21
elif choice == "2": 
 print(" ")
 print("It was reckless to challenge bear[#FFFFFF]...[/#FFFFFF]")
 print(" ")
 print("[bold red]GAME OVER[/bold red]")
else:
    print("[bold red]Error![/bold red] Swallowed by the darkness of the forest.")