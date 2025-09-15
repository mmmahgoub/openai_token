import tkinter as tk
from tkinter import scrolledtext, messagebox
import openai

# ---- SETUP YOUR API KEY ----
openai.api_key = "YOUR_OPENAI_API_KEY_HERE"   # Replace with your token

# ---- MAIN APP CLASS ----
class ChatGPTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Muhand ChatGPT Desktop App")
        self.root.geometry("600x600")
        self.root.configure(bg="#f0f0f0")

        # Chat Display (ScrolledText)
        self.chat_display = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, state="disabled", 
            bg="#ffffff", fg="#333333", font=("Arial", 11), relief="flat"
        )
        self.chat_display.pack(padx=10, pady=10, fill="both", expand=True)

        # Input Frame
        self.input_frame = tk.Frame(root, bg="#f0f0f0")
        self.input_frame.pack(fill="x", padx=10, pady=5)

        # Entry Widget
        self.input_box = tk.Entry(
            self.input_frame, font=("Arial", 12), bg="#ffffff", fg="#000000", relief="solid"
        )
        self.input_box.pack(side="left", fill="x", expand=True, padx=(0, 5))
        self.input_box.bind("<Return>", self.send_message)

        # Send Button
        self.send_button = tk.Button(
            self.input_frame, text="Send", command=self.send_message, 
            bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), relief="flat", width=10
        )
        self.send_button.pack(side="right")

    def send_message(self, event=None):
        user_input = self.input_box.get().strip()
        if not user_input:
            return

        # Show user message
        self.display_message("You", user_input)
        self.input_box.delete(0, tk.END)

        try:
            # Call ChatGPT
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or "gpt-4" if you have access
                messages=[{"role": "user", "content": user_input}],
                max_tokens=200,
                temperature=0.7,
            )
            bot_reply = response["choices"][0]["message"]["content"].strip()
            self.display_message("ChatGPT", bot_reply)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_message(self, sender, message):
        self.chat_display.configure(state="normal")
        self.chat_display.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_display.configure(state="disabled")
        self.chat_display.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatGPTApp(root)
    root.mainloop()
