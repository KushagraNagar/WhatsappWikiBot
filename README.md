# WhatsappWikiBot
A Whatsapp Bot that takes the command !wiki TOPIC and searches that topic on Wikipedia and sends back the result.

# Usage
It's simple, run the code via whatsapp_automation1.py, enter the phone number you want the bot to be initialized to and it'll start listening on that number for !wiki commands.
For example, the sender can type !wiki Tesla and the bot will send information about Tesla to the sender. 

You can also use !stop to stop the bot.


# Files
Whatsapp.py is used to read and write messages 
Whatsapp_automation1.py is used to open and instance of Whatsapp Web to send the very first message using the URL method after that the new messages are stored in the clip board and copy-pasted into the chatbox.
