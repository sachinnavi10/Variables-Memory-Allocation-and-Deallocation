# Task 8: Check whether the requested skill exists in ["Python", "SQL", "Git", "HTML"].
required_skills = ["Python", "SQL", "Git", "HTML"]


def check_skill(skill_name):
    if skill_name in required_skills:
        return "Skill available"
    else:
        return "Skill not available"


skill_name = input("Enter a skill name: ")
result = check_skill(skill_name)
print("Result:", result)