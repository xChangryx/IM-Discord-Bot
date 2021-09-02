# IM-Discord-Bot
**A discord bot to add roles through reactions**

## How to use
To use the bot write:
```py
!roles
:emoji: -> @role
:emoji2: -> @role2
:emoji3: -> @role3
```
You can add as many roles as you want, replace `->` with whatever you want, you can even add your own text within the message, just make sure that each new role is on a separate line and the first line only says `!roles`.  
An embed will be generated containing the entire message except the first line and the bot will automatically react to the message with the emojis used.

Supported emojis:
- Native
- Custom
- Animated

Dont use:
- Emojis from other servers

## How to host
To host the bot you must first create one through the [Discord Developer Portal](https://discord.com/developers/applications).  
Next you must copy the token and put it in a `.env` file in the same folder as the code.  
The `.env` file should look like this:
```env
TOKEN='your_token_here'
```
Now you can run [main.py](main.py) to start the bot.
