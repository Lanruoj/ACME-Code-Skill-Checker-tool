
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








