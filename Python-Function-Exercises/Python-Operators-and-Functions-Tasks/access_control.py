# Task 7: Grant access to adults with ID or to any employee; otherwise deny access.
def check_access(age, has_id, is_employee):
    if (age >= 18 and has_id == True) or is_employee == True:
        return "Access granted"
    else:
        return "Access denied"

age = int(input("Enter age: "))
has_id = input("Do you have ID? (True/False): ") == "True"
is_employee = input("Are you an employee? (True/False): ") == "True"
result = check_access(age, has_id, is_employee)
print(result)