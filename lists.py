# def movies():
#     fav_movies = []
    
#     for i in range(3):
#         user_input = input("enter your fav movie: ")

#         fav_movies.append(user_input)

#     print(f"your fav movies are {fav_movies}")

# movies()

def is_palindrome(nums):
    n = len(nums)-1

    for i in range(len(nums)):
        if nums[i] != nums[n-i]:
            print("not palindrome")
            return
    print("palindrome")        
  
    
is_palindrome([])


# def palindrome(n):
#     l = len(n)-1
#     for i in range(len(n)):
#         if n[i] != n[l-i]:
#            print("not palindrome")
#            return
    
#     print("palindrome")

# palindrome([1,2,3,2,1])
