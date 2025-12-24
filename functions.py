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




# def run_num_analyzer():

#     count = 0
#     total = 0

#     while True:

#         user_input = input("Enter any num(q to quit): ")

#         if user_input.lower() == "q":
#             print("Thanks for playing with us, see you next time!")
#             break

#         try:
#             num = int(user_input)
#             result = num_analyzer(num)

#             if result is not None:
#                 count += 1
#                 total += num

#         except ValueError:
#             print("Please enter a valid number")
    
#     print("The final Summary")
#     print(f"Total numbers you entered: {count} ")
#     print(f"Total sum of all numbers: {total}")



# def num_analyzer(num):

#     if num < 0:
#         print("skipping negative numbers")
#         return None

#     if num == 0:
#         print("0 is nuetral")
#         return None

#     if num%2 == 0:
#         print(f"{num} is an even number")
#     else:
#         print(f"{num} is an odd number")

#     return num



# run_num_analyzer()


# def run_bmi_calculator():
#     while True:

#         height = input("enter your height in meters(q to done ): ")
#         if height == "q":
#             print("Thanks for using our bmi calculator!")
#             break
#         weight = input("enter your weight in kg: ")

#         try: 
#             h = float(height)
#             w = float(weight)

#             if h == 0 or w == 0:
#                 print("height and weight should be more than 0")
#                 continue
            
#             bmi = bmi_calculate(h,w)
#             category = category_bmi(bmi)
#             print(f"Your BMI is {bmi} ----> {category}")

#         except ValueError:
#             print("Please enter valid height and weight")


# def bmi_calculate(h, w):
#     return round(w/h**2, 2)

# def category_bmi(bmi):
#     if bmi < 18.5:
#         return "underweight"
    
#     if bmi < 25:
#         return "Normal weight"
    
#     if bmi < 30:
#         return "Overweight"
    
#     else:
#         return "Obese"
    

# run_bmi_calculator()


# def calc_sum(nums):
#     total = 0
#     for i in range(len(nums)):
#         total += nums[i]
#     return total


# def cal_average(nums):
#     average = calc_sum(nums)/len(nums)
#     return average

# nums = []
# def run_sum_average(nums):

#     count = 0

#     print("Welcome to Sum and Average calulator!")

#     while True:
#         user_input = input("Enter a number(q to stop): ").strip()
#         if user_input == "":
#             print("Input cannot be empty")
#             continue
#         if user_input.lower() == "q":
#              break
            
#         try:
#             num = int(user_input)

#             if num <= 0:
#                 print("Numbers should be greater than 0")
#                 continue

#             nums.append(num)  
#             count += 1

#         except ValueError:
#             print("Enter a valid number")
#     if count > 0:
#         total = calc_sum(nums)
#         average = cal_average(nums)
#         print(f"Summary")
#         print(f"the total sum of all nums is {total}")
#         print(f"The average of all numbers is {average}")
#         print(f"Total numbers you entered: {count}")
#         print("The numbers you entered: ")
#         print(','.join(map(str,nums)))
#     else: 
#         print("Thank you for using our website, hope we see you again!")


# run_sum_average(nums)



def find_max_min():
    nums = []
    while True:

        user_input = input("Enter any number(q to quit): ").strip().lower()
        if user_input == "q":
            break

        try:
            num = int(user_input)
            nums.append(num)
        except ValueError:
            print("Please enter a valid number")
    if len(nums) > 0:
        max_number = find_max(nums)
        min_number = find_min(nums)
        print(f"Maximum number is {max_number}")
        print(f"Minimum number is {min_number}")

def find_max(nums):
    max_number = nums[0]
    for num in nums:
        if num > max_number:
            max_number = num

    return max_number

def find_min(nums):
    min_number = nums[0]
    for num in nums:
        if num < min_number:
            min_number = num

    return min_number



find_max_min()