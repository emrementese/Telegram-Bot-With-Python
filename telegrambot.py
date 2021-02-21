'''
Created by Emre MENTEŞE on 28.01.2021.
'''
import requests

# if you don't know chat id and bot token, please read the createbot.txt file.
bot_token = "Your bot token"
chat_id = "Your chat id"

"-----------------------------------------------------------------------------------------------------------------------------"
# Send a message.

#1. Method
text = "Hello World !"
message = {'text': text}
requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id ,data=message)

#2. Method
message = "Hello World !"
requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id +"&text=" + message)

"-----------------------------------------------------------------------------------------------------------------------------"
# Send a HTML, Hyperlink and Text.

#For example https://www.google.com --> Google | www.instagram.com/emre_mentese  --> myprofile

message = '<a href="www.instagram.com/emre_mentese">My Profile</a>'
requests.get("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id + "&parse_mode=HTML&disable_web_page_preview=true&text=" + message)

"-----------------------------------------------------------------------------------------------------------------------------"
# Send a Emoji

# Find the utf code of the emoji you want to send. For example: 😉 --> '\U0001F609'
message = '\U0001F609'
requests.post("https://api.telegram.org/bot" + bot_token +"/sendMessage?chat_id=" + chat_id +"&text=" + message)

"-----------------------------------------------------------------------------------------------------------------------------"
# Send a image.

image_path = "file path"
myimage = open(image_path, "rb")
image = {"photo": myimage}
requests.post("https://api.telegram.org/bot" + bot_token +"/sendPhoto?chat_id=" + chat_id ,files=image)

"-----------------------------------------------------------------------------------------------------------------------------"
# Send a File.

myfilepath = "file path"
with open(myfilepath, 'rb') as myfile:
    file = {'document': myfile}
    requests.post("https://api.telegram.org/bot" + bot_token +"/sendDocument?chat_id=" + chat_id ,files=file)

"-----------------------------------------------------------------------------------------------------------------------------"
#Thanks a read. Please give STAR :)
