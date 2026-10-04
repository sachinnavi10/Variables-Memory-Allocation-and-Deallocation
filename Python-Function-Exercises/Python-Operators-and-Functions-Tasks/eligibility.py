# Task 4: Return whether the student is eligible with marks >= 60, attendance >= 75, and no backlog.
def check_eligibility(marks, attendence, backlog_status):
    if marks >= 60 and attendence >= 75 and backlog_status == False:
        return "Eligible"
    return "Not eligible"

eligibility = int(input("Enter marks: "))
attendance = int(input("Enter attendance percentage: "))
backlog_status = input("Enter backlog status (True/False): ").lower() == "true"

result = check_eligibility(eligibility, attendance, backlog_status)
print("Eligibility:", result)