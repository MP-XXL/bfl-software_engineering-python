def calculate_fact(number):
    #Base case
    if number == 1 or number == 0:
        return 1
    else:
        #Recurseive case
        return number * calculate_fact(number -1)

print(calculate_fact(5))


def fib(num):
    #Base case
    if num == 0:
        return []
    elif num == 1:
        return [num]
    series = [0, 1]
    while len(series) < num:
        next_series = series[-1] + series[-2]
        series.append(next_series)
    return series
print(fib(10))
