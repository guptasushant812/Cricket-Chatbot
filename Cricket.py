import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() 

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "quit":
        print("Bot: Goodbye!")
        break

    if not user_input:
        print("Bot: Please enter a valid cricket-related question.")
        continue

    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a cricket expert bot. Answer only cricket-related queries with accurate and up-to-date information."},
                {"role": "user", "content": user_input}
            ]
        )
        if response.choices and hasattr(response.choices[0].message, 'content'):
            print("Bot:", response.choices[0].message.content.strip())
        else:
            print("Bot: (No reply received or wrong format.)")
    except Exception as e:
        print("Bot: Error occurred ->", str(e))
