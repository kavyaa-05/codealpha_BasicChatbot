import tkinter as tk
import random
responses = {
    "greeting": ["Hey there! 😊", "Hello 👋", "Hi! How can I help you?"],
    "how_are_you": ["I'm doing great! 😄", "All good here! What about you?", "Feeling awesome! 😎"],
    "name": ["I'm your smart Python chatbot 🤖", "You can call me PyBot!"],
    "help": ["Try saying hi, ask my name, or say bye!", "I'm here to chat with you 😊"],
    "bye": ["Goodbye! 👋", "See you soon!", "Take care! 😊"]
}
def get_response(user):
    user=user.lower()
    if any(word in user for word in ["hi", "hello", "hey"]):
        return random.choice(responses["greeting"])
    elif "how are you" in user:
        return random.choice(responses["how_are_you"])
    elif "your name" in user or "who are you" in user:
        return random.choice(responses["name"])
    elif "help" in user:
        return random.choice(responses["help"])
    elif "bye" in user:
        return random.choice(responses["bye"])
    elif "time" in user:
        import datetime
        return "Current time is " + datetime.datetime.now().strftime("%H:%M:%S")
    elif "date" in user:
        import datetime
        return "Today's date is" + datetime.datetime.now().strftime("%d-%m-%Y")
    else:
        return random.choice([
            "Hmm... can you rephrase that? 🤔",
            "I'm still learning! Try something else 😊",
            "Interesting... tell me more!",
            "I didn't quite get that 😅"
        ])
def send_message(event=None):
    user_input = entry.get().strip()
    if user_input == "":
        return
    chat_box.insert(tk.END, "You: " + user_input + "\n")
    reply = get_response(user_input)
    chat_box.insert(tk.END, "Bot: " + reply + "\n\n")
    entry.delete(0, tk.END)
    chat_box.yview(tk.END)
    if "bye" in user_input.lower():
        window.after(1500, window.destroy)
window = tk.Tk()
window.title("🤖 Smart Chatbot")
window.geometry("420x520")
chat_box = tk.Text(window, height=22, width=50)
chat_box.pack(pady=10)
entry = tk.Entry(window, width=35)
entry.pack(pady=5)
send_btn = tk.Button(window, text="Send", command=send_message)
send_btn.pack()
window.bind('<Return>', send_message)
window.mainloop()