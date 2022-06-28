
class Skill:
    def __init__(self, skill_name, name_variations, weight):
        self.skill_name = skill_name
        self.name_variations = name_variations
        self.weight = weight

PYTHON = Skill("Python", ["Python", "python"], 1)
RUBY = Skill("Ruby", ["Ruby", "ruby"], 2)
BASH = Skill("Bash", ["Bash", "bash"], 4)
GIT = Skill("Git", ["Git", "git"], 8)
HTML = Skill("HTML", ["HTML", "Html", "html"], 16)
TDD = Skill("TDD", ["TDD", "Tdd", "tdd"], 32)
CSS = Skill("CSS", ["CSS", "Css", "css"], 64)
JAVASCRIPT = Skill("JavaScript", ["JavaScript", "Javascript", "javascript", "JS", "js"], 128)

SKILL_LIST = [PYTHON, RUBY, BASH, GIT, HTML, TDD, CSS, JAVASCRIPT]

welcome = "\n---ACME CODING SKILL TEST---\nWelcome to ACME Corporation's skill assessment tool. This program will evaluate your potential suitability for a developer role\nbased on which skills you have.\n"

instructions = "\n---INSTRUCTIONS---\n\n1. Enter skill\n2. Press Enter key\n3. Repeat for all of your skills\n4. Once completed, enter 'X'"


def print_message(section):
    print(section)
    next()

# def get_name(name):
#     name = input("What is your name?")

def next():
    answer = input("Are you ready to continue? (Y or N):  ")
    if answer == "Y":
        return True  

def get_input(index):
    user_input = input(f"Skill {index}: ")
    return user_input

def check_input():
    done = "X"
    index = 1
    score = 0
    while True:
        input = get_input(index)
        index += 1
        if input == done:
            break
        for i in SKILL_LIST:
            if input in i.name_variations:
                score += i.weight
    return score

def calculate_max_score(list_of_skills):
    max_score = 0
    for i in list_of_skills:
        value = i.weight
        max_score += value
    return max_score


def print_results(score, max_score):
    title = "\n---RESULTS---\n"
    results = f"You scored {score} out of {max_score}"
    print(title + results)

def main_program():
    max_score = calculate_max_score(SKILL_LIST)
    print_message(welcome)
    print_message(instructions)
    score = check_input()
    results = print_results(score, max_score)


main_program()







