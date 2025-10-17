## SDSS Computing Studies Python Assignment
### Extension: Choose Your Own Adventure

Now that we can do output using print() and input using input() and can make decisions using conditional statements (if statements) we can now complete the choose your own adventure assignment!

We can run another file from within a program by importing the file.  Note: this is really not the best way to structure code, but it works well for what we are doing here.  There are far better ways to accomplish the same thing.

You can check out the sample code starting with the landing page, page1.py.  Note that when you want to run a separate file, you can do that at any time by using the *import* command, and you only need to include the filename, not the file extension.

To include the page2.py file, just import page2

### Advanced Options

We can include color in our print output!

This requires that you make use of a Python Library that is not normally included in your Python installation.  We will have retrieve and install it from the Python Package Repository (pypi).

Type the following command into your terminal:
```
pip install rich
```
If that one doesn't work, you can also try:
```
python3 -m pip install rich
```
The difference is that the first one installs it for everyone on the computer (which might not work due to the way Delta controls permissions on the computers) whereas the second one is only for you when you use the computer.

Once you are done, you can just start using their new print command if you do the following:
```
from rich import print
```
This tells Python to start using the print command that is in the *rich* package instead of it's regular one.  We can add colours or text formatting by adding a markup code to the beginning of a block of text:
```
print("This is not colored, but [bold blue]this is blue[/bold blue]")
```
Note that when you want to end the formatting, you need to put a closing to your markup that begins with a / symbol.  If you end a line, the formatting is reset. (see page 9.py). 

Experiment or google to find some of the options available to you!
You can also check out the documentation at https://rich.readthedocs.io/en/latest/index.html