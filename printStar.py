rows = int(input("enter num of rows: "))
col = int(input("enter num of columns: "))

for i in range(rows):
    if i == 0:
        print("* " * col)
    elif(i < rows-1):
        print("  " * (col//2) + "*")
    else:
        print("* " * col)
