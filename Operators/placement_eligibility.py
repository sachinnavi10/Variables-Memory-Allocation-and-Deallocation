# Task 10: Determine placement eligibility from age, marks, attendance, and backlog; categorize by experience.
def check_placement_eligibility(age, marks, attends, experience, has_backlog):
    if age >= 18 and marks >= 60 and attends >= 75 and has_backlog == False:
        placement_eligible = True
    else:
        placement_eligible = False

    if experience == 0:
        candidate_category = "Fresher"
    elif 1 <= experience <= 3:
        candidate_category = "Junior"
    else:
        candidate_category = "Senior"

    return placement_eligible, candidate_category

age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
attends = float(input("Enter attendance percentage: "))
experience = int(input("Enter years of experience: "))
has_backlog = input("Has backlog? (True/False): ").strip().lower() == "true"

placement_eligible, candidate_category = check_placement_eligibility(
    age, marks, attends, experience, has_backlog
)

print("Placement eligible:", "Yes" if placement_eligible else "No")
print("Candidate category:", candidate_category)