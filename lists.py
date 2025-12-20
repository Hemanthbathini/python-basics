# def movies():
#     fav_movies = []
    
#     for i in range(3):
#         user_input = input("enter your fav movie: ")

#         fav_movies.append(user_input)

#     print(f"your fav movies are {fav_movies}")

# movies()

def is_palindrome():
    nums = [1, 2, 3, 2, 1]
    
    copy_nums = nums.copy()
    copy_nums.reverse()

    if copy_nums == nums:
        print("palindrome")
    else:
        print("not palindrome")
    

is_palindrome() 
