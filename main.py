import random

opetators = ['+', '-', '*', '/']
min_operann = 1
max_operann = 20

def generate_question():
    first = random.randint(min_operann, max_operann)
    second = random.randint(min_operann, max_operann)
    operator = random.choice(opetators)
    question = str(first) + operator + str(second)
    print(question)
    return question

def get_input():
    return print(int(input("Enter your answer: ")))
    


def main():
    generate_question()
    import random

opetators = ['+', '-', '*']
min_operann = 1
max_operann = 20

def generate_question():
    first = random.randint(min_operann, max_operann)
    second = random.randint(min_operann, max_operann)
    operator = random.choice(opetators)
    question = str(first) + operator + str(second)
    answer = eval(question) # evaluates a string expression and returns the result
    print(question)
    print(answer)
    return question, answer

def get_input():
    return print(int(input("Enter your answer: ")))
    
def validation(answer):
    user_answer = get_input()
    if user_answer == answer:
        print("Good job!")
    else:
        print("wrong anwser! Try again.")
            


def main():
    answer = generate_question()
    validation(answer)

if __name__ == "__main__":
    main()