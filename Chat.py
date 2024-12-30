import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello, %1, How are you today ?",]
    ],
    [
        r"what is your name ?",
        ["My name is Chatty, how can I help you today ?",]
    ],
    [
        r"how are you ?",
        ["I am doing well, thank you for asking.",]
    ],
    [
        r"sorry (.*)",
        ["Its alright",]
    ],
    [
        r"i'm (.*) (.*)",
        ["Is it really ?",]
    ],
    [
        r"I want (.*)",
        ["What would it take for you to get %1"]
    ],
    [
        r"(.*) (.*)",
        ["Why %1 %2 ?",]
    ],
    [
        r"I can't (.*) (.*)",
        ["You don't have to %1 %2",]
    ],
    [
        r"Is there (.*)",
        ["Why do you ask ?",]
    ],
    [
        r"I don't (.*)",
        ["You don't ?",]
    ],
    [
        r"I (.*) you",
        ["Why do you %1 me ?",]
    ],
    [
        r"Why (.*)",
        ["Why %1 ?",]
    ],
    [
        r"I (.*)",
        ["Interesting, can you tell me more ?",]
    ],
    [
        r"Hi|hey|hello|hola",
        ["Hello there!",]
    ],
    [
        r"What (.*) want ?",
        ["Why do you ask ?",]
    ],
    [
        r"(.*) (.*) ?",
        ["Why do you ask that ?",]
    ],
    [
        r"How (.*) (.*) ?",
        ["Why do you ask that ?",]
    ],
    [
        r"Because (.*)",
        ["Is that really the reason ?",]
    ],
    [
        r"(.*)",
        ["Please, go on.",]
    ],
]

def chatty():
    print("Hi, I am a chatbot for customer support. Ask me anything!")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatty()
