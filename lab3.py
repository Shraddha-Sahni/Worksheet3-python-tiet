# Q1
# def diff(n):
#     diff=abs(n-17)
#     return diff*2 if n>17 else diff
# x=int(input("enter a number"))
# result=diff(x)
# print("Result:",result)


# Q2
# def test_range(n):
#     return True if( n>=100 and n<=1000) or (n==2000) else False
# x=int(input("enter a number"))
# result=test_range(x)
# print("Result:",result)


# Q3
# def reverse_string(s):
#     return s[::-1]
# x=(input("enter a string"))
# result=reverse_string(x)
# print("Result:",result)


# Q4
# def count_case(s):
#     counts={'uppercase':0,'lowercase':0}
#     for char in s:
#         if char.isupper():
#             counts["uppercase"] += 1
#         elif char.islower():
#             counts["lowercase"] += 1
#     return counts
# str= input("Enter a string: ")
# result = count_case(str)
# print("Uppercase letters:",result['uppercase'])
# print("Lowercase letters:",result['lowercase'])


# Q5
# def unique_elements(lst):
#     return list(set(lst))
# elements=[1,2,5,6,7,8,3,5,2,8]
# result= unique_elements(elements)
# print("Unique elements from the list:",result)


# Q6
# def even_numbers(lst):
#     return [num for num in lst if num % 2==0]
# sample_list = [1,2,3,4,5,6,7,8,9]
# print("Even numbers from the given list:\n ",even_numbers(sample_list))


# Q7
# def outer_function():
#     print("Inside outer function")

#     def inner_function():
#         print("Inside inner function")

#     inner_function()

# outer_function()



# Q8
# def student(name, age, course):
#     print("Name:", student.__code__.co_varnames[0])
#     print("Age:", student.__code__.co_varnames[1])
#     print("Course:", student.__code__.co_varnames[2])
#     print("Values:", name, age, course)
# student("ShraddhaSahni", 19, "RAI")


# Q9
# def move_robot(x, y, direction):
#     if direction =="up":
#         y += 1
#     elif direction =="down":
#         y -= 1
#     elif direction =="left":
#         x -= 1
#     elif direction =="right":
#         x += 1
#     return (x, y)
# print(move_robot(0, 0, "up"))


# Q10
# def classify_temperature(temp):
#     if temp < 15:
#         return "Cold"
#     elif 15 <= temp <= 30:
#         return "Moderate"
#     else:
#         return "Hot"

# print("Temperature:",classify_temperature(10))   
# print("Temperature:",classify_temperature(25))   
# print("Temperature:",classify_temperature(35)) 


# Q11
# def is_goal_reached(path):
#     x, y = 0, 0
#     for move in path:
#         if move == "up":
#             y += 1
#         elif move == "down":
#             y -= 1
#         elif move == "left":
#             x -= 1
#         elif move == "right":
#             x += 1
#     return (x, y) == (0, 0)

# path = ["up","right","right","down","left","left"]
# print(is_goal_reached(path)) 
    

# Q12
# class Student:
#     def __init__(self,student_id,student_name,student_class):
#         self.student_id = student_id
#         self.student_name = student_name
#         self.student_class = student_class

#     def display_attributes(self):
#         print(f"Student ID: {self.student_id}")
#         print(f"Student Name: {self.student_name}")
#         print(f"Student Class: {self.student_class}")

# s1 = Student("1024230044","Shraddha Sahni","2W12")
# s1.display_attributes()


# Q13
# class Student:
#     def __init__(self,student_id,student_name,student_class):
#         self.student_id = student_id
#         self.student_name = student_name
#         self.student_class = student_class

#     def display(self):
#         print(f"ID: {self.student_id}, Name: {self.student_name}, Class: {self.student_class}")

# student1 = Student("1024230043", "Sudiksha", "RAI-2nd Year")
# student2 = Student("1024230044", "Shraddha Sahni", "RAI-2nd Year")

# student1.display()
# student2.display()


# Q14
# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return math.pi*self.radius**2

#     def perimeter(self):
#         return 2*math.pi*self.radius

# c = Circle(3)
# print(f"Area: {c.area()}")
# print(f"Perimeter: {c.perimeter()}")


# Q15
# class String:
#     def __init__(self):
#         self.text = ""

#     def get_String(self):
#         self.text = input("Enter a string: ")

#     def print_String(self):
#         print(self.text.upper())

# s = String()
# s.get_String()
# s.print_String()


# Q16
# class Robot:
#     def __init__(self,name,task):
#         self.name = name
#         self.task = task
#         self.battery_level = 100

#     def perform_task(self):
#         if self.battery_level >= 10:
#             print(f"{self.name} is performing: {self.task}")
#             self.battery_level -= 10
#         else:
#             print(f"{self.name} has low battery. Please recharge.")

#     def recharge(self):
#         self.battery_level = 100
#         print(f"{self.name} is fully recharged.")

#     def status(self):
#         print(f"Name: {self.name}")
#         print(f"Task: {self.task}")
#         print(f"Battery Level: {self.battery_level}%")

# r1 = Robot("Robo", "Drawing")
# r1.status()
# r1.perform_task()
# r1.status()
# r1.recharge()
# r1.status()
