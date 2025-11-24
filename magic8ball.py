import random

# List of possible answers
answers = [
    "Yes, definitely!",
    "It is certain.",
    "Without a doubt.",
    "Most likely.",
    "Ask again later.",
    "Cannot predict now.",
    "Better not tell you now.",
    "Don't count on it.",
    "My reply is no.",
    "Very doubtful."
]

print("Welcome to the Magic 8 Ball!")
question = input("Ask your question: ")

# Pick a random answer
response = random.choice(answers)

print("\nThinking...\n")
print("Magic 8 Ball says:", response)
