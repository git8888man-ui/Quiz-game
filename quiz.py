import random

print("Welcome to the Trivia Quiz!")
print("-----------------------------")

num_correct = 0

questions = [
    {
        "question": "What is 2 + 2?",
        "type": "number",
        "answer": "4"
    },
    {
        "question": "What is the color of the sky on a clear day?",
        "type": "text",
        "answer": "blue"
    },
    {
        "question": "Which one is a fruit?\nA) Carrot\nB) Apple\nC) Potato",
        "type": "choice",
        "answer": "b"
    },
    {
        "question": "How many legs does a spider have?",
        "type": "number",
        "answer": "8"
    },
    {
        "question": "What do bees make?",
        "type": "text",
        "answer": "honey"
    }
]

random.shuffle(questions)

for q in questions:
    if q["type"] == "number":
        while True:
            try:
                answer = input(q["question"] + " ")
                if answer == q["answer"]:
                    print("Correct!\n")
                    num_correct += 1
                    break
                else:
                    print("Wrong, try again.\n")
                    break
            except ValueError:
                print("Please enter a valid integer.")
                continue
    elif q["type"] == "text":
        answer = input(q["question"] + " ")
        if answer.lower() == q["answer"]:
            print("Correct!\n")
            num_correct += 1
        else:
            print("Wrong, the answer is", q["answer"] + ".\n")
    elif q["type"] == "choice":
        answer = input(q["question"] + "\nYour answer (A, B, or C): ")
        if answer.lower() == q["answer"]:
            print("Correct!\n")
            num_correct += 1
        else:
            print("Wrong, the answer is B.\n")

print("-----------------------------")
print("You got", num_correct, "out of 5 correct.")
percent = num_correct / 5 * 100
print("Your score:", percent, "%")
