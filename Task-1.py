import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ['hi|hello|hey', ['Hello,Sir!', 'Hi Sir!', 'Hey,Sir!']],
    ['how are you?', ['I am doing well,sir, thank you Sir!', 'I am good Sir, thanks for asking Sir!']],
    ['what is your name?', ['I am a simple chatbot.', 'I am a chatbot designed for your assistance sir']],
    ['what can you do?', ['I can produce any source of information you need sir. Feel free to ask me anything!']],
    ['bye|goodbye', ['Have a great day,Sir!,Bye']],
    ['(.*) weather (.*)', ['Its 25 degress right now,Sir!']],
    ['(.*) news (.*)', ['India has Won  T20 World cup, Kalki movie crossed 1000 crore mark today.']],
    ['(.*) time (.*)', ['Its 12"0 clock sir!.']]
]

chat = Chat(pairs, reflections)

def chat_respond(inputs):
    return chat.respond(inputs)

def main():
    print("Hello sir! How May I Help you .")
    
    while True:
        inputs = input("You : ")
        response = chat_respond(inputs)
        print("Bot:",response)
        if inputs.lower() == 'bye':
            break
        
if __name__ == "__main__":
    main()