pip from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("My ChatterBot")

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

while True:
    request = input("You: ")
    response = chatbot.get_response(request)
    print("Bot: ", response)

import tkinter as tk
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def get_response():
    request = user_input.get()
    response = chatbot.get_response(request)
    bot_response.set(response)

root = tk.Tk()
root.title("My ChatterBot")
root.geometry("400x600")

chatbot = ChatBot("My ChatterBot")

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

user_input = tk.StringVar()
bot_response = tk.StringVar()

user_input_frame = tk.Frame(root)
user_input_frame.pack()

user_input_entry = tk.Entry(user_input_frame, textvariable=user_input)
user_input_entry.pack(fill=tk.X, padx=10)

send_button = tk.Button(user_input_frame, text="Send", command=get_response)
send_button.pack(side=tk.RIGHT, padx=10)

bot_response_frame = tk.Frame(root)
bot_response_frame.pack(pady=10)

bot_response_label = tk.Label(bot_response_frame, textvariable=bot_response)
bot_response_label.pack()

root.mainloop()
