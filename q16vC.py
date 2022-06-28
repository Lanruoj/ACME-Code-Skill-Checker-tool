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

YES_VARIATIONS = ("Y", "Yes", "y", "YES", "yes")
NO_VARIATIONS = ("N", "No", "n", "NO", "no")

def calculate_max_score(list_of_skills):
    max_score = 0
    for i in list_of_skills:
        value = i.weight
        max_score += value
    return max_score

def next(prompt):
    answer = ""
    while True:
        answer = input(f"\n{prompt}  ")
        if answer in (YES_VARIATIONS):
            return True

def get_input(index):
    user_input = input(f"Skill {index}: ")
    return user_input

def check_skills():
    done = "X"
    index = 1
    score = 0
    remaining_skills = []
    while True:
        input = get_input(index)
        index += 1
        if input == done:
            break
        for i in SKILL_LIST:
            if input in i.name_variations:
                score += i.weight
                SKILL_LIST.remove(i)
    return score

def get_percentage(score, max_score):
    percentage = int((score / max_score) * 100)
    return percentage

def print_results(score, max_score, user_name):
    title = "\n---RESULTS---\n"
    percentage = get_percentage(score, max_score)
    results = f"You scored {percentage}% ({score} out of {max_score})\n"
    message = evaluate_results(user_name, percentage)
    print(results)

def evaluate_results(name, percentage):
    message = "your suitability for the role is"
    print("\n---RESULTS---\n")
    if percentage <= 33:
        print(f"Sorry {name}, {message} low.")
    elif percentage > 33 and percentage <=66:
        print(f"Good job {name}, {message} average.")
    elif percentage > 66 and percentage <= 90:
        print(f"Well done {name}, {message} high.")
    else:
        print(f"Congratulations {name}, you're hired!")

def give_feedback(unmet_criteria):
    title = "\n---RECOMMENDED LEARNING---\n"
    print(f"{title}\nTo meet the full requirements for this role, you must also learn these skills:")
    for i in unmet_criteria:
        if i.weight < 2:
            print(f"\n--{i.skill_name}--\nIf you learn {i.skill_name} you will improve your score by {i.weight} point")
        else:
            print(f"\n--{i.skill_name}--\nIf you learn {i.skill_name} you will improve your score by {i.weight} points")
    print("\n")
    

def main_program():
    #CALCULATE MAX SCORE OF TEST#
    max_score = calculate_max_score(SKILL_LIST)
    #MESSAGES#
    intro = "\n---ACME CODING SKILL TEST---\n\nWelcome to ACME Corporation's skill assessment tool. This program will evaluate your potential suitability for a developer role\nbased on which skills you have.\n"
    instructions = "\n---INSTRUCTIONS---\n\n1. Enter skill\n2. Press Enter key\n3. Repeat for all of your skills\n4. Once completed, enter 'X'"
    next_continue = "Are you ready to continue?"
    #PRINT WELCOME MESSAGE#
    print(intro)
    #TAKE NAME#
    user_name = input("Please enter your name:  ")
    #WELCOME THEM WITH THEIR NAME#
    welcome = "\nWelcome {user_name}!"
    #PRINT INSTRUCTIONS#
    print(instructions)
    #IF USER WANTS TO PROCEED#
    if next(next_continue):
        goodbye = f"\n---GOODBYE---\n\nThank you for choosing to use the ACME Code Skill Test program, {user_name}!\nGood luck with your application.\n\n---END PROGRAM---\n"
        #CALCULATE RESULTS#
        score = check_skills()
        percentage = get_percentage(score, max_score)
        results = print_results(score, max_score, user_name)
        #IF ANY CRITERIA NOT MET#
        if percentage < 100:
            #ASK IF USER WANTS TO SEE HOW TO IMPROVE#
            see_feedback = input("Would you like to see how you can improve your score? ")
            #IF NO, EXIT#
            if see_feedback in NO_VARIATIONS:
                print(goodbye)
            #IF YES, SHOW REMAINING SKILLS TO LEARN#
            elif see_feedback in YES_VARIATIONS:
                feedback_message = give_feedback(SKILL_LIST)
                if next(next_continue):
                    print(goodbye)
            
        

main_program()