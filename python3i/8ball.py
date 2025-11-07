import random


def get_response():
    responses = [
        "yes.", "no.", "maybe.", "ask again later.",
        "definitely!", "i don't think so.", "absolutely.", "not sure."
    ]
    return random.choice(responses)

def magic_8_ball():
    print(" welcome to the magic 8 ball!")
    while True:
        question = input("ask a yes/no question (or type 'quit' to stop): ")
        if question.lower() == 'quit':
            print("goodbye!")
            break
        print("Answer:", get_response())


magic_8_ball()
