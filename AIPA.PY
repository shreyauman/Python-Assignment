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
#      print("welcome",name)

# greeting("shreya")    

# Addition function

# def addition(a,b):
#     return a + b

# result=addition(30,20)
# print("sum=",result)

# def even_odd(n):
#     if n % 2 == 0:
#         return"Even"
#     else:
#         return"odd"

#     print(even_odd(8))
#     print(even_odd(5))


#python file handling


# file=open("test.txt","mode") #syntax

# file=open("aipa.txt","w")
# file.write("hello student of aipa")
# file.close()

# with open("aipa2.txt","w") as file:
#    file.write("hello student of aipa nsti ald")


# with open("aipa2.txt","a") as file:
#     file.write("\n prayagraj , uttar pradesh")
#     file.write("\n india")


# read -"r" read all the content of File
# import time 
# with open("aipa.txt","r") as file:
#     for line in file:
#         print(line.strip())
#         time.sleep(2)

#         x=file.read()
#         print(x)

#         x=file.read(52)
#         print(x)

#         print(file.readline())
#         print(file.readline())
#         print(file.readline())

#         print(file.readline().strip())
#         print(file.readline().strip())
#         print(file.readline().strip())

#         lines=file.readlines()

#         print(lines)

# "x" - creates a new file if the file does not already existtry:
#try: 
# 
# with open("aipa3.txt","x") as file:
#     file.write("x mode")

#  except:
# print(file already exists)

# import csv
# std=[
#     ["shreya",27,"aipa"],
#     ["abhay",27,"aipa"],
#     ["ankit",27,"aipa"],
#     ["nikita",27,"aipa"],
#  [nikita",27"aipa"],]


# with open("student.csv","w",newline="") as file:
# writer=csv.writer(file)
#  writeriter.writerows(std)
   
# with open "student".csv"w") as file:


#handling directories & files

# import os,shutil,pathlib

# print(os.getcwd())  # current working directory
# os.mkdir("21 oct")  # create a directory
# os.rmdir("21 oct")  #  remove a directory only if empty
# print(os.listdir("."))  # list file and directories

# shutil.rmtree("21 oct") # remove everything in a directory
# os.rename("csa.txt","copa.txt") # rename a file 
# shutil.copy("aipa2.txt","aipa3.txt") # copy a file
# shutil.move("a.txt","b.txt") # move a file 

# with open ("21oct/22oct/aipa/aipa.txt","w") as file: # nested directory
#     file.write("hello")


# from pathlib import Path

# filename=input("enter the filename:")

# Path=Path(filename)

# if Path.exists():
#     print("file exists")
# else:
#     print("file does not exist")

# Directory information

# import os

# print("Current Working Directory:")
# print(os.getcwd())

# print("\nFiles and Folders:")
# print(os.listdir())

# File existence

# from pathlib import Path

# filename = input("Enter filename: ")

# file = Path(filename)

# if file.exists():
#     print("File exists")
# else:
#     print("File does not exist")

# Create nested folders

# from pathlib import Path

# folder = Path("College/Students/AIPA")

# folder.mkdir(parents=True, exist_ok=True)

# print("Folders created successfully")

# Find file types

# from pathlib import Path

# folder = Path(input("Enter folder path: "))

# print("CSV and TXT files:")

# for file in folder.iterdir():
#     if file.is_file() and file.suffix in [".csv", ".txt"]:
#         print(file.name)

# Backup a file

# import shutil
# from pathlib import Path

# source = Path("aipa.txt")
# backup = Path("Backup")

# backup.mkdir(exist_ok=True)

# if source.exists():
#     shutil.copy2(source, backup / source.name)
#     print("File backed up successfully")
# else:
#     print("File not found")


# move file

# import shutil
# from pathlib import Path

# source = Path("Practice")
# destination = Path("PDF")

# destination.mkdir(exist_ok=True)

# for file in source.glob("*.pdf"):
#     shutil.move(str(file), str(destination / file.name))

# print("PDF files moved successfully")

# Directory backup

# import shutil
# from pathlib import Path

# source = Path("Test")
# destination = Path("Test_Backup")

# if source.exists():
#     if not destination.exists():
#         shutil.copytree(source, destination)
#         print("Directory backed up successfully")
#     else:
#         print("Backup folder already exists - isliye naya nahi bana")
# else:
#     print("Test directory not found")

# # demo.txt ko padhne ke liye sahi code
# with open("Test/demo.txt", "r") as f:
#     data = f.read()
#     print("demo.txt ka data:", d

# Exception handling

# try: #it contais code that might raise ans error

#     x=10
#     y=0
# except ZeroDivisionError: #it handles a matching exception
#     print("No. cannopt be devided by 0")


# a=10
# b=10
# print(a * b)



# x="10"
# y=5
# print(x+y)

# std ={
#     "name":"shreya",
#     "trade":"aipa",
#     "session":2026
# }

# print(std["age"])




# try:
#     age=int(input("enter you age:"))
#     print("age is ",age)

# except ValueError:
#      print("please enter a valid whole no.")


#  try:
#    a=int(input("enter first no. "))
#    b=int(input("enter second no."))

#  print(a / b)

# (except ZeroDivisionError):
#     print("invalid entry!")

#  print("successful.")





# try:
#       a=int(input("enter first no. "))
#       b=int(input("enter second no."))

#       print(a /b )
# except (ValueError,ZeroDivisionError):
#       print("invalid entry!")

# print("successful. ")      



# try:
#     num=int(input("enter number:"))

# except ValueError:
#     print("invalid input.")

# else:
#     print("square of on. :",num ** 2)

# finally:
#     print("Run successful!")


# marks=int(input("enter your marks:"))

# if marks <0 or marks >100:
#     raise ValueError("marks cannot be less than 0 or more than 100.")

# print("marks accepted:" ,marks)

# print("successful")

# try:
#     marks=int(input("enter your marks:"))
#     if marks <0 or marks >100:
#      raise ValueError("marks cannot be less than 0 or more than 100.")

# except ValueError as shreya:
#    print("invalid marks",shreya)

# else:
#    print("marks accepted:", marks)

# finally:
#    print("coding completed")

# class AIPAError(Exception):
#     pass

# try:
#     eligible=int(input("enter you qualification:"))
#     if eligible <10 :
#         raise AIPAError("you are not qualified for aipa admission.")
#     print("you are eligible.")
# except ValueError:
#     print("please neter valid number.")

# except AIPAError as ai:
#     print("eligibility issue: " ,ai)


# try:
#     num=int(input("enter number:"))
#     print(100 / num)

# except Exception as e: 
#     print("enter occured:",e) 


# custom Exception


# class InsufficientBalanceError(Exception):
#     pass

# balance = 5000

# try:
#     amount = float(input("Enter withdrawal amount: "))

#     if amount > balance:
#         raise InsufficientBalanceError(
#             "Insufficient balance!"
#         )

#     if amount <= 0:
#         raise ValueError("Amount must be positive.")

#     balance -= amount

#     print("Withdrawal successful!")
#     print("Remaining balance:", balance)

# except InsufficientBalanceError as e:
#     print("Error:", e)

# except ValueError as e:
#     print("Invalid input:", e)


# Employee Salary validation

# try:
#     salary = float(input("Enter employee salary: "))

#     if salary < 0:
#         raise ValueError("Salary cannot be negative.")

#     print("Employee salary:", salary)

# except ValueError as e:
#     print("Invalid salary:", e)



#safe division calculator


# try:
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     result = a / b
#     print(f"Result: {result}")
# except ValueError:
#     print("Invalid input! Please enter numbers only.")
# except ZeroDivisionError:
#     print("Error! Division by zero is not allowed.")

# Positive Number Validator


# try:
#     num = float(input("Enter a number: "))
#     if num < 0:
#         raise ValueError("Number is negative")
#     print(f"Positive number: {num}")
# except ValueError as e:
#     print(f"Error: {e}")


# List Index Handling

# numbers = [10, 20, 30, 40, 50]
# print(f"List: {numbers}")
# try:
#     index = int(input("Enter index (0-4): "))
#     print(f"Value at index {index} is {numbers[index]}")
# except ValueError:
#     print("Please enter a valid integer index.")
# except IndexError:
#     print("Invalid index! Index out of range.")


# Dictionary Lookup

# student = {"name": "Shreya", "trade": "IT", "marks": 85}
# key = input("Enter key: ")
# try:
#     print(f"{key} : {student[key]}")
# except KeyError:
#     print(f"Key '{key}' not found.")


# File Reading

# try:
#     filename = input("Enter filename: ")
#     with open(filename, "r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File not found!")

# Integer Input Validation

# while True:
#     try:
#         num = int(input("Enter an integer: "))
#         print(f"You entered: {num}")
#         break
#     except ValueError:
#         print("Invalid! Enter integer only.")


# class aipa:
#      def __int__(self,name,roll_no,trade,marks):  #Contructor
#         self.name=name
#         self.roll_no=roll_no
#         self.trade=trade
#         self.marks=marks

# std1=aipa("shreya",1,"Aipa",75)
# std2=aipa("abhay",2,"Aipa",85)

# # std1.name("Abhay")

# print(std1.name)
# print(std1.roll_no)
# print(std1.trade)
# print(std1.marks)


# print(std2.name)
# print(std2.roll_no)
# print(std2.trade)
# print(std2.marks)


# class Student:
#     def __init__(self, name, roll_no, trade, marks):    # Constructor
#         self.name = name
#         self.roll_no = roll_no
#         self.trade = trade
#         self.marks = marks

#     def display_details(self):
#         print("Name:", self.name)
#         print("Roll No:", self.roll_no)
#         print("Trade:", self.trade)
#         print("Marks:", self.marks)

#     def check_result(self):
#         if self.marks >= 40:
#             print("Pass")
#         else:
#             print("Fail")

#     def percentage(self,total_marks):
#         return (self.marks/total_marks)*100

# # Object creation
# student1 = Student("Nidhi", 1, "AIPA", 75)
# student2 = Student("Nikita", 2, "AIPA", 85)

# # Method calls
# student1.display_details()
# student1.check_result()

# student2.display_details()
# student2.check_result()




class car:
    def __init__(self,name,brand,speed,price):
        self.name = name
        self.brand = brand
        self.speed = speed
        self.price = price

    def display_details(self):
        print("name:", self.name)
        print("brand:", self.brand)
        print("speed:", self.speed)
        print("price:", self.price)

    def check_result(self):
        if self.price >= 10000000:
            print("luxury car")  
        else:
            print("Affordable Car")

    # Object creation
car1 = car("Fortuner", "Toyota", 180, 4500000)   # 45 lakh
car2 = car("La Rose Noire Droptail", "Rolls-Royce", 250, 2850000000)  # 285 crore

car1.display_details()
car1.check_result()

car2.display_details()
car2.check_result()             