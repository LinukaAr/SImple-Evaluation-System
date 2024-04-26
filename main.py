import random

operators = ['+', '-', '*']
min_operand = 1
max_operand = 20
total_problems = 3

def generate_question():
    first = random.randint(min_operand, max_operand)
    second = random.randint(min_operand, max_operand)
    operator = random.choice(operators)
    question = f"{first} {operator} {second}"
    answer = eval(question)
    return question, answer

for i in range(total_problems):
    question, answer = generate_question()
    while True:
        user_answer = int(input(f"Q{i+1}. {question} = "))
        if user_answer == answer:
            print("Correct!")
            break
        else:
            print("Incorrect. Try again.")
