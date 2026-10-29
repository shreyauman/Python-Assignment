# import math

# print("square root:",math.sqrt(100))
# print("sqare of :",math.pow(5,3))
# print("factorial:",math.factorial(5))

# import random

 # number=random.randint(1,10)
 # print(number)

# print(random.choice(["anjli","nikita","nidhi","shreya"]))

# import datetime

# today=datetime.date.today()
# print(today)

# currenttime=datetime.datetime.now()
# print(currenttime)


# import statistics

# marks=[50,60,60,70,75,80,85]



# print(statistics.mean(marks))
# print(statistics.median(marks))  #[50,60,60,70,75,80,85]
# print(statistics.mode(marks))


# import os

# print(os.name) #nt-windows posix-linux/mac
# print(os.getcwd) #current working directory
# os.mkdir("module_today")

# user-defined modules

# import module
# print(module.add(12,5))

# print(module.sub(12,5))

# print(module.mul(12,5))

# print(module.div(12,5))

# total=module.x + module.y
# print(total)
# from module import mul,xyz

# print(xyz(12,5))

# pip is an standard package installer  for python

# Basic module

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Cannot divide by zero"
#     return a / b


# # Taking input from user
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# # Displaying results
# print("Addition:", add(a, b))
# print("Subtraction:", subtract(a, b))
# print("Multiplication:", multiply(a, b))
# print("Division:", divide(a, b))

#math module


# import math

# num = int(input("Enter a number: "))

# print("Square:", num ** 2)

# if num >= 0:
#     print("Square Root:", math.sqrt(num))
# else:
#     print("Square root is not possible for negative numbers.")

# if num >= 0:
#     print("Factorial:", math.factorial(num))
# else:
#     print("Factorial is not possible for negative numbers.")


# Random quiz

import random

questions = [
    ("What is 2 + 3?", "5"),
    ("What is 5 * 2?", "10"),
    ("What is 10 - 4?", "6"),
    ("What is the square of 4?", "16"),
    ("What is 12 / 3?", "4")
]

question, answer = random.choice(questions)

print("Random Quiz!")
print(question)

user_answer = input("Enter your answer: ")

if user_answer.strip() == answer:
    print("Correct Answer!")
else:
    print("Wrong Answer!")
    print("Correct answer is:", answer)