
word = input("enter any word: ")
bold_choice = input("do you want to format your word to bold(yes/no): ").lower()
italic_choice = input("do you want to format your word to italic(yes/no): ").lower()
underline_choice = input("do you want to format your word to underlined(yes/no): ").lower()

ansi_code = ""
if bold_choice == "yes":
    ansi_code += "\033[1m"
elif bold_choice != "no":
    print("invalid choice for bold. skipping bold")
if italic_choice == "yes":
    ansi_code += "\033[3m"
elif italic_choice != "no":
    print("invalid choice for italic. skipping italic")
if underline_choice == "yes":
    ansi_code += "\033[4m"
elif underline_choice != "no":
    print("invalid choice for underline. skipping underline")

text_color = input("do you want text color(yes/no): ")
if text_color == "yes":
    text_color = input("which color do you want from yellow, green and red: ").lower()
if text_color == "red":
    ansi_code += "\033[31m"
elif text_color == "green":
    ansi_code += "\033[32m"
elif text_color == "yellow":
    ansi_code += "\033[33m"
else:
    print("we dont have the color you entered")

bg_color = input("do you want background color(yes/no): ")
if bg_color == "yes":
    bg_color = int(input("choose one color in the listed colors: 1)magenta 2)white 3)red "))
    if bg_color == 1:
        ansi_code += "\033[45m"
    elif bg_color == 2:
        ansi_code += "\033[47m"
    elif bg_color == 3:
        ansi_code += "\033[41"
    else:
        print("we dont have the color you selected")

if ansi_code:
    print(f"{ansi_code}{word}")
