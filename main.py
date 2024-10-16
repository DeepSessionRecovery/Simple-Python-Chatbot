
```
import nltk
from nltk.stem import WordNetLemmatizer
import json
import random 

# Initialize NLTK
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer() 

# Load intents and responses from JSON files
with open('intents.json') as f:
    intents = json.load(f) 

with open('responses.json') as f:
    responses = json.load(f) 

# Define a function to process user input
def process_input(input_text):
    input_text = input_text.lower()
    words = nltk.word_tokenize(input_text)
    words = [lemmatizer.lemmatize(word) for word in words]
    return words 

# Define a function to match user input with intents
def match_intent(words):
    for intent in intents:
        for pattern in intent['patterns']:
            pattern_words = nltk.word_tokenize(pattern)
            pattern_words = [lemmatizer.lemmatize(word) for word in pattern_words]
            if set(words).issubset(set(pattern_words)):
                return intent['intent']
    return None 

# Define a function to generate a response
def generate_response(intent):
    for response in responses:
        if response['intent'] == intent:
            return random.choice(response['responses'])
    return "I didn't understand that." 

# Define a main function to interact with the chatbot
def chatbot():
    print("Welcome to SimpleChatBot!")
    while True:
        user_input = input("You: ")
        words = process_input(user_input)
        intent = match_intent(words)
        response = generate_response(intent)
        print("Chatbot: ", response)
        if user_input.lower() == "quit":
            break 

# Run the chatbot
chatbot()
``` 

*intents.json*
```
[
  {
    "intent": "greeting",
    "patterns": ["hello", "hi", "hey"]
  },
  {
    "intent": "ask_name",
    "patterns": ["what's your name", "who are you"]
  },
  {
    "intent": "ask_age",
    "patterns": ["how old are you", "what's your age"]
  },
  {
    "intent": "ask_location",
    "patterns": ["where are you from", "what's your location"]
  }
]
``` 

*responses.json*
```
[
  {
    "intent": "greeting",
    "responses": ["Hello!", "Hi!", "Hey!"]
  },
  {
    "intent": "ask_name",
    "responses": ["I'm SimpleChatBot!", "My name is SimpleChatBot"]
  },
  {
    "intent": "ask_age",
    "responses": ["I'm ageless!", "I don't have an age"]
  },
  {
    "intent": "ask_location",
    "responses": ["I'm from the internet!", "I don't have a location"]
  }
]
``` 

*requirements.txt*
```
nltk
