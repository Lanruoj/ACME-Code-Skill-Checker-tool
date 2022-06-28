
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



def get_input(index):
    user_input = input(f"Skill {index}: ")
    return user_input

def check_input():
    # user_input_list = []
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
                print(score)
    return score

def calculate_max_score(list_of_skills):
    max_score = 0
    for i in list_of_skills:
        value = i.weight
        max_score += value
    return max_score


def print_results(score, max_score):
    # score = check_input()
    results = f"You scored {score} out of {max_score}"
    print(results)

def main_program():
    max_score = calculate_max_score(SKILL_LIST)
    score = check_input()
    results = print_results(score, max_score)

main_program()







