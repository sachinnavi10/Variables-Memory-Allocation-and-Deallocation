# Task 2: Check whether an integer is even or odd and divisible by 3 and 5.
def check_number(number):
    if number % 2 == 0:
        even_or_odd = "Even"
    else:
        even_or_odd = "Odd"

    divisible_by_3 = number % 3 == 0
    divisible_by_5 = number % 5 == 0    

    return even_or_odd, divisible_by_3, divisible_by_5

even_or_odd, divisible_by_3, divisible_by_5 = check_number(10)

print("Number is:", even_or_odd)
print("Divisible by 3:", divisible_by_3)
print("Divisible by 5:", divisible_by_5)