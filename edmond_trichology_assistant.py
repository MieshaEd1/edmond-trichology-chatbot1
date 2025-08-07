import os
from openai import OpenAI
from datetime import datetime

# 🔐 Ask for API key (DO NOT hardcode it)
api_key = input("Paste your OpenAI API key here: ")
client = OpenAI(api_key=api_key)

# 📅 Consultation booking link
BOOKING_LINK = "https://miesha-k.as.me/?appointmentType=81715848"

# 🤖 Talk to GPT
def chat_with_gpt(history):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=history,
        temperature=0.7
    )
    return response.choices[0].message.content

# 💬 Starting conversation
history = [
    {"role": "assistant", "content": "Welcome! I’m the Edmond Trichology Assistant. How can I help you with your scalp or hair today?"}
]

# 🧠 SMART LOGIC
def main():
    while True:
        user_input = input("Client: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print(f"\nAssistant: Thank you for chatting. You can book your consultation here: {BOOKING_LINK}")
            break

        history.append({"role": "user", "content": user_input})
        reply = chat_with_gpt(history)

        # Smart keyword logic
        smart_keywords = ["hair loss", "scalp", "bald", "alopecia", "moisture", "itch", "dry", "breakage"]
        if any(keyword in user_input.lower() for keyword in smart_keywords):
            reply += f"\n\n📌 It sounds like a consultation may help. Book now: {BOOKING_LINK}"

        print("\nAssistant:", reply)
        history.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    main()
