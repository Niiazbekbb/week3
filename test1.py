try:
    hours = float(input("Enter the number of hours worked: "))
    rate = float(input("Enter the hourly rate: "))
    if hours <= 40:
        salary = hours * rate
    else:
        salary = 40 * rate + (hours - 40) * 1.5 * rate
    print("The total salary is:", salary)
except ValueError:
    print("Error, please enter numeric input.")
except Exception as e:
    print("An error occurred:", str(e))
