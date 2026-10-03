# Task 6: Calculate discount and final payable amount using the requested purchase thresholds.
def calculate_discount(purchase_amount):
    if purchase_amount >= 5000:
        discount_rate = purchase_amount * 20 / 100
    elif purchase_amount >= 3000:
        discount_rate = purchase_amount * 10 / 100
    elif purchase_amount < 300:
        discount_rate = purchase_amount * 5 / 100
    else:
        discount_rate = 0


    final_payable_amount = purchase_amount - discount_rate

    return discount_rate, final_payable_amount


discount, payable = calculate_discount(6000)
print("Discount amount:", discount)
print("Final payable amount:", payable)