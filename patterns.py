num = int(input("enter any num: "))

# for i in range(1, num+1):
#     for j in range(num+1):
#         print("A", end = " ")

#     print()

# chars = ["A", "B", "C"]
# for ch in chars:
#     for j in range(3):
#         print(ch, end = " ")
#     print()


# for i in range(num):
#     for j in range(2 * i + 1):
#         print("*", end = " ")

#     print()


# for i in range(num):
#     for j in range(1):
#         print((num - i) * " " + "* "*i, end = " ")
#     print()



# for i in range(num):
#     print((num - i - 1) * " " + " *" * (i+1), end  = " ")
#     print()
    
# for j in range(num-1,0,-1):
#     print((num - j) * " " + " *" * j, end = " ")
#     print()


for i in range(num):
    for j in range((num - i)):
        print("*", end = " ")
    print()
    