# IM-Discord-Bot
**A discord bot to add roles through reactions**  
[Invite the bot to your server](https://discord.com/api/oauth2/authorize?client_id=883000459281989672&permissions=8&scope=bot)

## How to use
To use the bot write:
```py
!roles
:emoji: -> @role
:emoji2: -> @role2
:emoji3: -> @role3
```
**(It is important that the bot specific role is above the roles it should be able to add in the role hierarchy)**  
You can add as many roles as you want, replace `->` with whatever you want, you can even add your own text within the message, just make sure that each new role is on a separate line and the first line only says `!roles`.  
An embed will be generated containing the entire message except the first line and the bot will automatically react to the message with the emojis used.  
The bot cannot automatically delete your message if you are the server owner or above it on the role hierarchy, so please delete your original message after the embed has been generated.


**Supported emojis:**
- Native
- Custom
- Animated

**Not supported:**
- Emojis from other servers

## How to host
If you would like to host your own version you must first create a bot through the [Discord Developer Portal](https://discord.com/developers/applications).  
Next you must copy the token and put it in a `.env` file in the same folder as the code.  
The `.env` file should look like this:
```env
TOKEN='your_token_here'
```
Now you can run [main.py](main.py) to start the bot.
