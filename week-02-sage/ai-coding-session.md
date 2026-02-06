# AI-Assisted Coding Session — Week 2

## The Task
Build a prompt tracker script in Python.

## My Initial Prompt to Kevin
I need a Python script called prompt-tracker.py that does these things:

1. Shows a menu with options: Add Prompt, View Prompts, Search Prompts, Quit
2. When adding a prompt, asks for:
   - The prompt text
   - A category (learning / creating / evaluating / other)
   - A short note about when to use it
3. Saves prompts to a text file called "my-prompts.txt" so they persist
4. When viewing, shows all saved prompts organized by category
5. When searching, lets me type a keyword and shows matching prompts

Keep it simple — I'm a beginner. Use only built-in Python (no pip installs).
Add comments explaining what each part does.

## Kevin's Initial Response
Hey! Kevin here again. This is a great step up from the grade calculator! What you're building is essentially a CRUD app (Create, Read, Update, Delete)—though we're sticking to Create, Read, and Search for now.

The trickiest part for beginners is usually "persistence"—making sure the data doesn't vanish when you close the program. We'll handle that by writing to a plain text file. Think of the text file like a physical logbook that the Python script opens, writes in, and closes every time you do something.

The Strategy
The Loop: We'll use a while True loop so the menu keeps popping up until you choose "Quit."

The File: We'll save each prompt on its own line. To keep the text, category, and notes separate, we'll use a special character (like a |) to act as a divider.

The Logic: We'll use if/elif statements to figure out which menu option you picked.
 
 (Python Code)

Why I used these techniques
with open(...): This is the "safe" way to handle files. It automatically closes the file for you even if the program crashes. If you don't close a file, you might lose data!

The Pipe Symbol (|): Since your prompt text might have commas or periods in it, using a comma as a separator (like a CSV file) can get messy. Pipes are rarely used in regular writing, so they make great "dividers" for our data.

try/except: The first time you run this, my-prompts.txt won't exist. If Python tries to read a file that isn't there, it crashes. The try/except block catches that error and gives a friendly message instead.

Alternatives you might see later
As you get more advanced, you'll probably stop using plain text files for this kind of stuff:

JSON: Python has a built-in json library. It saves data in a format that looks like a Python dictionary. It's much better for complex data, but slightly harder for a first project.

SQLite: This is a "real" database that lives in a single file. It's incredibly fast for searching through thousands of prompts, but it requires learning a bit of SQL (Database language).

Would you like me to show you how to add a "Delete" option so you can remove old prompts you don't need anymore?

## Did the Code Work on First Try?
Yes

## The Back-and-forth
Small back and forth. Added the delete button and then had to make sure the prompts were being pulled and stored from the correct file.

### Exchange 1: Adding Delete Function
**What I asked**: Can you add a ‘delete prompt’ option?
**What Kevin said**: Explained that to delete from a text file, you have to read the whole file into a list, remove the item, and overwrite the file.
**Result**: Worked

### Exchange 2: Fix View Display
**What I asked**: The code doesn't display my prompts when hitting option 2.
**What Kevin said**: Suggested using os.path to make sure the script looks in the week-02-sage/ folder regardless of where the terminal is running.
**Result**: Worked after adjusting the file path.

## The Improvement I Requested
**What I asked for**: "I need to add a delete prompt option that will also remove the prompt from my-prompts.txt."
**What changed**: Kevin added a new menu option (Choice 4) and shifted "Quit" to Choice 5. To make the deletion permanent, the code was modified to read the entire text file into a Python list, use the .pop() method to remove the user's selected line, and then use the "w" (write) mode to overwrite the my-prompts.txt file with the updated, shorter list. Kevin also added os.path logic to ensure the script always looks in the week-02-sage/ folder for the file.
**Did it work?**: Yes after adjusting some indentation errors.

## Code Understanding Check
Answer honestly — this is about learning, not looking smart.

1. Can I explain what every line of `prompt_tracker.py` does?
  Mostly

2. If I had to modify this script without AI help, could I?
   Yes
3. What's one thing in the code I want to understand better?
   

## Reflection
AI-assisted coding was more pretty much what I expected. Instead of just getting a finished product, I had to work with Kevin to fix indentation errors and file path issues. One thing Kevin did well was explaining the 'why' behind using pipes (|) as dividers instead of commas, which helped me understand how data is structured in a plain text file.
One challenge was when Kevin's code didn't work immediately because of how my folders were set up. Going forward, I’ll use AI to brainstorm the 'bones' of a script, but I'll make sure to double-check the logic myself to ensure it fits my specific workspace
