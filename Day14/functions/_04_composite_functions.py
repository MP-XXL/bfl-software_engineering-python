# Summing a list
numbers = [10, 7, 6, 9, 0, 1, 5, 8]

def total(nums):
    total = 0
    for num in nums:
        total += num
    print(total)


total(numbers#[1, 2])


# Tithes and percentage
tithes = [1000,100,2000,2500,3000]

def total(amount):
    total_amount = 0
    for cash in amount:
        total_amount = total_amount + cash
    print(f"total amount is:{total_amount}")
    return total_amount


def calculate_percent(total):
    return total * 10/100

value = total(tithes)
calculate_percent(value)
