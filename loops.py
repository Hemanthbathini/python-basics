# i = 1
# while i <= 100:
#     print(i)
#     i += 1


# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# n = int(input("enter any number: "))

# i = 1
# while i <= 10:
#     mul = n * i
#     print(f"{n} * {i} = {mul}")
#     i += 1

# nums = [1, 4, 9, 16, 25, 36, 49, 64]

# idx = 0

# while idx < len(nums):
#     print(nums[idx])
#     idx += 1

# nums = (1, 4, 9, 16, 25, 36, 49, 64)

# i = 0
# x = 16
# while i < len(nums):
#     if nums[i] == x:
#         print("found at idx ", i)
#     i += 1

# i = 0

# while i <= 5:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     i += 1

# nums = (1, 4, 9, 16, 25, 36, 49, 64)
# x = 25
# idx = 0
# for el in nums:
#     if el == x:
#         print(f"found {x} at idx {idx}")
#         break
#     else:
#         print("finding")
#     idx += 1

# else:
#     print("end")

# n = 5
# for i in range(1, 11):
#     mul = n*i
#     print(f"{n} * {i} = {mul}")

# for i in range(5):
#     pass

# print("hey")

# n = int(input("enter any number: "))
# i = 1
# sum = 0
# while i <= n:
#     sum = sum + i
#     i += 1
# print(f"toatl sum: {sum}")

# for i in range(10,0,-1):
#     print(i)

# i = 1
# while i <= 20:
#     if i%2 == 0:      
#         print(i)
#     i += 1

# n = int(input("enter a number: "))

# for i in range(1, n+1):
#     print(i)

# for el in range(1,11):
#     if el == 6:
#         break
#     print()


# while True:
#     password = input("enter your password: ")
#     if password == "python123":
#         print("Access Granted!")
#         break
#     else:
#         print("Try again")

# while True:
#     input_user = input("enter any input: ")
#     if input_user == "q":
#         print("Thank You")
#         break
    
# for i in range(1,11):
#     if i == 3 or i == 7:
#         continue
#     print(i)


# for i in range(5):
#     user_input = int(input("enter a number "))
#     if user_input < 0:
#         continue
#     print(user_input)

# word = input("enter any word: ")

# for i in word:
#     if i in "aeiou":
#         continue
#     print(i)


# secret_number = 7

# while True:
#     try:
#         guess_num = int(input("guess the number: "))
#         if guess_num == secret_number:
#             print("Correct Guess!")
#             break
#         elif guess_num < secret_number:
#             print("too low, try again")
#         elif guess_num > secret_number:
#             print("too high, try again")

#     except ValueError:
#         print("guessing value should only be number! \ncontinue guessing!")


# sum = 0
# while True:
#     num = int(input("enter a number: "))
#     if num == 0:
#         break
#     sum = sum + num
    
# print(f"final sum is {sum}")

# password = "hemu123"
# chances = 3
# while chances > 0:
#     password_user = input("enter your password: ")
#     if password_user == password:
#         print("You successfully logged in!")
#         break
#     chances -= 1
#     print(f"you have {chances} chances left!")

# else:
#     print("oops you are out of chances!")
        
# for i in range(1,21,2):
#     print(i)

# for i in range(1,101):
#     if i%7 == 0:
#         break
#     print(i)

# sentence = input("enter any sentence: ")
# for ch in sentence:
#     if ch == " ":
#         continue
#     print(ch)


# n = int(input("enter any number: "))

# for i in range(1, n):
#     for j in range(1, i+1):
#         print("*", end = " ")
#     print()


# for i in range(n):
#     for j in range(n):
#         if j == 3:
#             break
#         print(j, end = " ")
#     print()

# for i in range(1,4):
#     for j in range(1,i+1):
#         print(j,end = " ")
#     print()

# for ch in ["A", "B", "C"]:
#     for j in range(3):
#         print(ch, end = " ")
#     print()
        
# for i in range(4):
#     for j in range(i+1):
#         print("*", end = " ")
#     print()

# for i in range(1,4):
#     for j in range(1,4):
#         if i == j:
#             continue
#         print(i,j)