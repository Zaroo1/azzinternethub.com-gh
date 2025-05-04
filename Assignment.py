# 1. User Information Program
def user_info():
    full_name = input("Enter your full name: ")
    department = input("Enter your department: ")
    age = input("Enter your age: ")
    sex = input("Enter your sex (male/female): ")

    print(f"\nHello, my name is {full_name} and I am a student of the {department} department. I am a good {sex}.")

# 2. Month Program
def show_month():
    month_number = int(input("\nEnter a number between 1 and 12 to find the month: "))
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]

    if 1 <= month_number <= 12:
        print(f"The month is {months[month_number - 1]}.")
    else:
        print("Invalid input. Please enter a number between 1 and 12.")

# 3. Simple Calculator
def calculator():
    print("\nSimple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operation (+, -, *, /): ")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero.")
            return
    else:
        print("Invalid operator.")
        return

    print(f"The result of {num1} {operator} {num2} is {result}")

# 4. Bubble Sort Program
def bubble_sort():
    print("\nEnter 6 numbers:")
    numbers = []
    for i in range(6):
        num = int(input(f"Number {i+1}: "))
        numbers.append(num)

    # Bubble Sort
    for i in range(len(numbers)):
        for j in range(0, len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print("Sorted numbers in ascending order:", numbers)

# Run all programs
user_info()
show_month()
calculator()
bubble_sort()
