from tkinter import *
from time import gmtime, strftime


chatLog = [['Matt','Hello','11:20'], ['User','hey!', '11:21']]
timestamp = strftime("%H:%M:%S", gmtime())
message = 'Welcome to Blcok Chat'
name = 'User'

def addMessage(messageInp):
    message = '[' + timestamp + '] ' + name + ': ' + messageInp + '\n'
    chatLogWindow = Label(chat, text=message, wraplength=190).pack(side=TOP)

chat = Frame()
chat.pack()

Label(chat, text="Chat Log:").pack(side=TOP)
chatLogWindow = Label(chat, text=message).pack(side=TOP)

sendMsg = Button(chat, text="Send", width=17, command=(lambda: addMessage(messageFeild.get())))
sendMsg.pack(side=BOTTOM)

messageFeild = Entry(chat)
messageFeild.pack(side=BOTTOM)

chat.mainloop()