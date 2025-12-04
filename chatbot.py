import random


GREETINGS = ["hi", "hello", "hey", "yo", "hola"]
GOODBYES = ["bye", "goodbye", "see you", "quit", "exit"]


def respond_to_greeting() -> str:
    replies = [
        "Hello! 👋",
        "Hi there!",
        "Hey, how can I help you today?",
    ]
    return random.choice(replies)


def respond_to_feeling(message: str) -> str:
    if "sad" in message or "depressed" in message:
        return "I'm sorry you're feeling down. Want to talk about it?"
    if "happy" in message or "good" in message:
        return "Nice! I'm glad you're feeling good 😄"
    if "stressed" in message:
        return "Maybe take a short break, drink some water, and come back fresh."
    return "Tell me more about how you're feeling."


def respond_to_study(message: str) -> str:
    if "python" in message:
        return "Python is great! Try building small projects and practicing daily."
    if "exam" in message or "test" in message:
        return "Plan a schedule, revise past questions, and sleep well before the exam."
    if "engineering" in message:
        return "Engineering is awesome! Keep your math strong and practice problem solving."
    return "Studying consistently every day helps more than last-minute cramming."


def generate_response(user_message: str) -> str:
    msg = user_message.lower().strip()

    # Greeting
    if any(word in msg for word in GREETINGS):
        return respond_to_greeting()

    # Goodbye
    if any(word in msg for word in GOODBYES):
        return "Goodbye! It was nice chatting with you. 😊"

    # Feelings
    if "feel" in msg or "feeling" in msg or "mood" in msg:
        return respond_to_feeling(msg)

    # Study / learning
    if "study" in msg or "learn" in msg or "exam" in msg or "python" in msg or "engineering" in msg:
        return respond_to_study(msg)

    # Fallback
    return "Hmm, I'm not sure I understand. Can you explain in another way?"


def main():
    print("🤖 Simple Chatbot")
    print("Type 'quit' or 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        if not user_input.strip():
            continue

        if any(word in user_input.lower() for word in GOODBYES):
            print("Bot:", "Goodbye! 👋")
            break

        reply = generate_response(user_input)
        print("Bot:", reply)


if __name__ == "__main__":
    main()
