# Task 3: Return Pass for marks >= 35, Fail otherwise, and Distinction for marks >= 85.
def get_result(marks):
    if marks >= 85:
        return "Distinction"
    elif marks >= 35:
        return "Pass"
    else:
        return "Fail"

result = get_result(90)
print("Result:", result)  # Output: Distinction