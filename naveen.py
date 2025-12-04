n=int(input("enter no of rows: "))
m= int(input("enter no of columns: "))

for i in range(n):
    if i == 0:
        print("* " * (m - 1) + " ")
    elif (i < n // 2):
        print("* " + "  " * (m - 2) + "*")
    elif i == n // 2:
        print("* " * (m - 1) + " ")
    elif i<(n-1):
        print("*" + "  " * (m - 2) + " *")
    else:
        print("* " * (m - 1) + " ")










