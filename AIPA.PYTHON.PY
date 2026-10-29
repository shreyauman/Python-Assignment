# print("Hello")
# a=10
# b=15

# c=a+b
# age+int(input("Enter your age"))
# if age >= 18:





# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))

# std=["Shreya","Aditya","Ajeet","nikita"]
# print(std)
#python is case sensitive
# 


# Alpa Class - Student Identifier

# students = [
#     {
#         "Name": "Shreya Suman",
#         "Mobile No": "9876543210",
#         "Address": "Prayagraj, Uttar Pradesh",
#         "UID": "ALP001"
#     },
#     {
#         "Name": "Ankit Kumar",
#         "Mobile No": "9123456789",
#         "Address": "Gaya, Bihar",
#         "UID": "ALP002"
#     },
#     {
#         "Name": "Abhay Singh",
#         "Mobile No": "9988776655",
#         "Address": "Patna, Bihar",
#         "UID": "ALP003"
#     },
#     {
#         "Name": "Nitika Sharma",
#         "Mobile No": "8765432109",
#         "Address": "Lucknow, Uttar Pradesh",
#         "UID": "ALP004"
#     },
#     {
#         "Name": "Alka Verma",
#         "Mobile No": "7654321098",
#         "Address": "Kanpur, Uttar Pradesh",
#         "UID": "ALP005"
#     }
# ]

# # Display student details
# for student in students:
#     print("Name:", student["Name"])
#     print("Mobile No:", student["Mobile No"])
#     print("Address:", student["Address"])
#     print("UID:", student["UID"])
#     print("-" * 40)


#  else:

#  print("invalid operation")


# function in python

#A function is a reusable 



# 10,15 20, 25 ,30 40

# def function_name(parameter):
# return

# def add(x,y):
#     return x + y



# print(add(10,15))
# print(add(20,55))
# print(add(30,40))

# def multiply(x,y):
#     print("multiplication of number:",x*y)

# multiply(10,15)
# multiply(20,55)
# multiply(30,40)




# def multiply(x):
#     for i in range(1,11):
#         print(x, "x", i, "=", x*i)

# # multiply(5)

# multiply(3)


# def add():
#     a=10
#     b=20 
#     print(a+b)
# add()

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def div(a,b):
#     if b ==0:
#         return "cannot divide by zero"
#     return a/b

# print(multiply(12,10))

# print(sub(100,50))

# print(div(100,5))


# def calculate_total(marks):
#      return sum(marks)
# def calculate_avg(marks):
#      return sum(marks)/len(marks)
# def result(average):
#     if average >=40:
#           return "Pass"
#     else:
#         return "Fail"

# Std_name=input("Enter student name: ")

# marks=[]

# for i in range (1,6):
#     mark=int(input("Enter marks for subject "+ str(i) + ": "))
#     marks.append(mark)

# total=calculate_total(marks)
# average=calculate_avg(marks)
# result=result(average)

# print("student name:",Std_name)
# print("Total marks:",calculate_total(marks))
# print("Average marks:",calculate_avg(marks))
# print("Result:",result)


#  Greeting function

# def greeting(name):
#       print("welcome",name)

# greeting("shreya")    

# Addition function

# def addition(a,b):
#      return a + b

# result=addition(30,20)
# print("sum=",result)

# Even or odd

# def even_odd(n):
#      if n % 2 == 0:
#          return "Even"
#      else:
#          return "Odd"

# print(even_odd(8))
# print(even_odd(5))

# Factorial Calculator



# def factorial(n):
#      fact = 1
#      for i in range(1, n + 1):
#          fact = fact * i
#      return fact

# print("Factorial =", factorial(5))

# Largest of Three Numbers


# def largest(a, b, c):
#     return max(a, b, c)

# print("Largest =", largest(10, 25, 15))

# Grade Calculator

# def grade(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 75:
#         return "B"
#     elif marks >= 60:
#         return "C"
#     elif marks >= 40:
#         return "D"
#     else:
#         return "Fail"

# print("Grade =", grade(85))

# List Statistics

# def total(numbers):
#     return sum(numbers)

# def average(numbers):
#     return sum(numbers) / len(numbers)

# def minimum(numbers):
#     return min(numbers)

# def maximum(numbers):
#     return max(numbers)

# numbers = [10, 20, 30, 40, 50]

# print("Total =", total(numbers))
# print("Average =", average(numbers))
# print("Minimum =", minimum(numbers))
# print("Maximum =", maximum(numbers))

#  Banking Application


balance = 1000

def deposit(amount):
     global balance
     balance += amount
     print("Amount deposited successfully")

def withdraw(amount):
     global balance
     if amount <= balance:
         balance -= amount
         print("Amount withdrawn successfully")
     else:
         print("Insufficient balance")

def show_balance():
     print("Balance =", balance)

while True:
     print("\n1. Deposit")
     print("2. Withdraw")
     print("3. Show Balance")
     print("4. Exit")

     choice = int(input("Enter your choice: "))

     if choice == 1:
         amount = int(input("Enter amount: "))
         deposit(amount)
     elif choice == 2:
         amount = int(input("Enter amount: "))
         withdraw(amount)
     elif choice == 3:
         show_balance()
     elif choice == 4:
         print("Thank you!")
         break
     else:
         print("Invalid choice")


# Student Record Processor


# students = [
#      {"name": "Aman", "marks": [40, 30, 36]},
#      {"name": "abhay", "marks": [60, 65, 70]},
#      {"name": "shreya", "marks": [70, 80, 69]}
#  ]

# def calculate_average(marks):
#      return sum(marks) / len(marks)

# def passing_students(students):
#      for student in students:
#          avg = calculate_average(student["marks"])
#          if avg >= 40:
#              print(student["name"], "Passed")

# for student in students:
#      avg = calculate_average(student["marks"])
#      print(student["name"], "Average =", avg)

# print("Passing Students:")
# passing_students(students)



