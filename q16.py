
# skill_scores = {
#         "Python":1,
#         "Ruby":2,
#         "Bash":4,
#         "Git":8,
#         "HTML":16,
#         "TDD":32,
#         "CSS":64,
#         "JavaScript":128
#         }

# max_score = 255
# user_skills = []
# score = 0
# user_input = ""

# welcome = "\n---ACME CODING SKILL TEST---\nWelcome to ACME Corporation's skill assessment tool. This program will evaluate your potential suitability for a developer role\nbased on which skills you have.\n"
# instructions = "\n---INSTRUCTIONS---\n\n1. Enter skill\n2. Press Enter key\n3. Repeat for all of your skills\n4. Once completed, enter 'DONE'"
# print(f"{welcome}{instructions}")

def goodbye():
        print("\nThank you for using the ACME Coding Skill Test.\n")

# exit = "DONE"
print("\n---SKILLS---\n")
# count = 0
# while user_input != exit:
        # count += 1
        # user_input = input(f"{count}:  ")
        # user_skills.append(user_input)
        # if user_input in skill_scores:
                # score += skill_scores[user_input]
                skill_scores.pop(user_input)

print("\n---RESULTS---")
percentage = int((score / 255) * 100)
print(f"\nYour coding skill score: {score} out of {max_score} ({percentage}%)")


if percentage >= 0 and percentage <= 33:
        print("Suitability for role: LOW\n")
elif percentage >= 34 and percentage <= 66:
        print(f"Suitability for role: AVERAGE\n")
elif percentage >= 67 and percentage <= 90:
        print(f"Suitability for role: HIGH\n")
else:
        print(f"Suitability for role: YOU'RE HIRED\n")

length_of_remaining_list = len(skill_scores)
skill_list = skill_scores.keys()


if score == max_score:
        goodbye()
else:
        next = input("Would you like to see how you can improve your score? (Y or N)  ")
        if next == "Y":
                print(f"\n---RECOMMENDED LEARNING---\n\nTo meet the full requirements for this role, you must also learn these skills:\n")
                print(", ".join(skill_list))
                for i in skill_scores:
                        print(f"If you learn {i} you will gain {skill_scores[i]} points")
goodbye()










