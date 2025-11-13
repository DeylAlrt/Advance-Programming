import random
import os

# Load jokes from file
def load_jokes(filename):
    jokes = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if "?" in line:
                setup, punchline = line.split("?", 1)
                jokes.append((setup + "?", punchline))
    return jokes

# Display a random joke
def tell_joke(jokes):
    setup, punchline = random.choice(jokes)
    print("\n" + setup)
    input("Press Enter to see the punchline...")
    print(punchline + "\n")

# Main program loop
def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    joke_file = os.path.join(script_dir, "randomJokes.txt")
    jokes = load_jokes(joke_file)

    print("Welcome! Type 'Alexa tell me a Joke' to hear a joke or 'quit' to exit.")
    
    while True:
        user_input = input(">> ").strip().lower()
        if user_input == "quit":
            print("Goodbye!")
            break
        elif user_input == "alexa tell me a joke":
            tell_joke(jokes)
        else:
            print("Type 'Alexa tell me a Joke' to hear a joke, or 'quit' to exit.")

if __name__ == "__main__":
    main()
