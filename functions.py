# def miss_you(mother, father):
#     mother = mother.capitalize()
#     father = father.capitalize()
#     print(f"hi {mother} and {father}, i miss you so much!")


# miss_you("sunitha", "sudheer")


# def add():
#     z = 1 + 2
#     return z

# print(add())

# def personal_dashboard(data):
#     print("\n----------PERSONAL DASHBOARD----------")

#     for key, value in data.items():
#         print(f"{key.capitalize()} : {value}")


#     if "age" in data:
#         age = int(data["age"])
#         if age  < 13:
#             print("Age Group: Child")
#         elif age  < 20:
#             print("Age Group: teen")
#         elif age  < 60:
#             print("Age Group: Adult")
#         else:
#             print("Senior")

# user_data = {}

# while True:
    
#     key = input("enter detail name(done to quit): ").strip().lower()
#     if key == "done":
#         break
#     value = input("enter value: ")

#     user_data[key] = value

# personal_dashboard(user_data)


# def analyze_number(num):
#     if num < 0:
#         print("skipping negative numbers")
#         return None
#     if num == 0:
#         print("0 is nuetral")
#         return None
#     if num > 0:
#         if num%2 == 0:
#             print(f"{num} is an even number")
#         else:
#             print(f"{num} is an odd number")

#     return num


# def run_number_analyzer():
#     count = 0
#     total = 0
#     while True:
#         user_input = input("enter any number(q for quit): ")

#         if user_input.lower() == "q":
#             break
        
#         try:
#             num = int(user_input)
#             result = analyze_number(num)

#             if result is not None:
#                 total += num
#                 count += 1
        
#         except ValueError:
#             print("please enter a valid number")
    
#     print(f"total numbers entered: {count}")
#     print(f"total sum is: {total}")

# run_number_analyzer()



# def run_is_positive():
#     count = 0
#     total = 0
#     while True:
        
#         user_input = input("enter a number(or enter q to quit!): ")
#         if user_input.lower() == "q":
#             print("Thank you for your time! see you next time")
#             break
#         try:
#             num = int(user_input)
#         except ValueError:
#             print("Please enter a valid number")
#             continue

#         result = check_is_positive(num)
#         print(f"your number is {result}")

#         count += 1
#         total += num

#     print(f"the total sum of all numbers is {total}")
#     print(f"total numbers you entered: {count}")



# def check_is_positive(num):
#     if num < 0:
#         return "negative"
#     else:
#         return "positive"

# run_is_positive()

# def run_marks_list():
#     marks = []
#     while True:

#         user_input = input("enter your marks one by one(q to quit): ")
#         if user_input == "q":
#             break

#         try: 
#             num = int(user_input)
#         except ValueError:
#             print("please enter a valid number")
#             continue

#         if num < 0:
#                 print("skipping negative numbers")
#                 continue   
#         marks.append(num)
#         if len(marks) == 0:
#             print("Please enter valid marks")
#             continue

#     total = addition(marks)
#     average_list = average(marks)
#     list_size = len(marks)

#     print(f"no of marks you entered: {list_size}")
#     print(f"Total marks: {total}")
#     print(f"average of your marks : {average_list}")
#     print(f"List of your marks:" )
#     list_of_marks(marks)

# def addition(marks):
#     total_sum = 0
#     for el in marks:
#         total_sum += el
#     return total_sum

# def average(marks):
#     return addition(marks)/len(marks)

# def list_of_marks(marks):
#     for el in marks:
#         print(el)
          
          
# run_marks_list()


# def fact_n():
#     n = int(input("enter a number: "))
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i

#     print(f"fact of {n} is {fact}")

# fact_n()