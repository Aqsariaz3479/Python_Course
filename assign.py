#Question1: 
# def safe_division(a,b):
#     try:
#          divide = a /b
#          return divide
#     except:
#         print("Error: Cannot divide by zero")
# print(safe_division(10,2))
# print(safe_division(10,0))

#Question2:
# while True:
#     try:
#         number = int(input("Enter the number: "))
#         print("Thank you")
#         break
#     except ValueError:
#         print("Invalid input! Try again.")

#Question3:
# try:
#     with open('file.txt', 'r') as file:
#         result = file.read()
#         print(result)
# except FileNotFoundError:
#     print("Error: File not found.")
# finally:
#     print("Operation Complete.")

#Question4:
# def check_positive(num):
#     if num < 0:
#      raise ValueError("Number must be positive!")
#     return num
# print(check_positive(10))
# print(check_positive(-5))
    
#Question5:
# try:
#     text = input("Enter some text: ")
#     with open('file.txt', 'r') as text:
#         result = text.write("hello!")
#         print(result)
# except IOError:
#     print("could not write to file!")
# finally:
#     print("Writing Complete!")

#Question6:
# try:
#     with open('data.txt', 'r') as file:
#         result = file.read()
#         print(result)
#     with open('data.txt', 'a') as file:
#         result = file.write("line\n")
#         print(result)
# except FileNotFoundError:
#     print("file not found. Creating new file...")
#     with open('data.txt', 'w') as file:
#         sol = file.write("This is new file.")
#         print(sol)
# finally:
#     print("Operation Done!")
    
    
#Question7:
# def multiply_list(list):
#     result = 0
#     for num in list:
#         result = result * num
#     return result
# print(multiply_list([1,2,3,4]))

#Question8:
# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num
#     print(result)
# except ValueError:
#     print("Not a number!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

#Swapping the Elements in list
# list = [23,4,8,7]
# list[0],list[1] = list[1],list[0]
# list[2],list[3] = list[3],list[2]
# list[1],list[2] = list[2],list[1]
# list[2],list[3] = list[3],list[2]

# print(list)

#Second largest number from the list
# list = [2,12,45,63,55,78,9,8,23]
# largest = 0
# sec_largest = 0
# for i in list:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i
# print(largest)
# print(sec_largest)

#)Sorting the list in ascending order
# list = [2,12,45,63,55,78,9,8,23]
# asc_order = []
# while list:
#     minimum = min(list)
#     asc_order.append(minimum)
#     list.remove(minimum)
# print(asc_order)
    


    
    
    
    

