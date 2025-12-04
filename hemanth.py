
with open("hemanth.txt", "w") as f:
    f.write(" I want to learn python\nlearning python is great thing\n")
    f.write("I am very excited about python")

with open("hemanth.txt", "r") as f:
    data = True
    word = "learning"
    line_no = 1
    while data:
        data = f.readline()
        if word in data:
            print(line_no)
        else:
            line_no += 1





