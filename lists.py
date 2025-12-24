# def movies():
#     fav_movies = []
    
#     for i in range(3):
#         user_input = input("enter your fav movie: ")

#         fav_movies.append(user_input)

#     print(f"your fav movies are {fav_movies}")

# movies()

# def is_palindrome(nums):
#     n = len(nums)-1

#     for i in range(len(nums)):
#         if nums[i] != nums[n-i]:
#             print("not palindrome")
#             return
#     print("palindrome")        
  
    
# is_palindrome([])


# def palindrome(n):
#     l = len(n)-1
#     for i in range(len(n)):
#         if n[i] != n[l-i]:
#            print("not palindrome")
#            return
    
#     print("palindrome")

# palindrome([1,2,3,2,1])


# def find_max_min():
#     nums = []
#     while True:

#         user_input = input("Enter any number(q to quit): ").strip().lower()
#         if user_input == "q":
#             break

#         try:
#             num = int(user_input)
#             nums.append(num)
#         except ValueError:
#             print("Please enter a valid number")
#     if len(nums) > 0:
#         max_number = find_max(nums)
#         min_number = find_min(nums)
#         print(f"Maximum number is {max_number}")
#         print(f"Minimum number is {min_number}")

# def find_max(nums):
#     max_number = nums[0]
#     for num in nums:
#         if num > max_number:
#             max_number = num

#     return max_number

# def find_min(nums):
#     min_number = nums[0]
#     for num in nums:
#         if num < min_number:
#             min_number = num

#     return min_number



# find_max_min()



# nums = [65, 87, 98, 44, 98, 75, 89, 34, 28]

# count_even = 0
# count_odd = 0

# for num in nums:
#     if num%2 == 0:
#         count_even += 1
#     else:
#         count_odd += 1
    

# print(f"The total no of even numbers are: {count_even}")
# print(f"The total no of odd numbers are: {count_odd}")



#Reverse a list

# nums = [65, 87, 98, 44, 98, 75, 89, 34, 28]

# for i in range(len(nums)-1, -1, -1):
#     print(nums[i])

# nums = [26, 27, 28]

# is_sorted = False

# for i in range(1,len(nums)):
#     if  nums[i] >= nums[i-1]:
#         is_sorted = True
#         break

# print(is_sorted)



# create a new list with only postive numbers
# nums = [55, 76, -28, 32, 98, -25]

# positive_nums = []

# for i in range(len(nums)):
#     if nums[i] >= 0:
#         positive_nums.append(nums[i])
       

# print(f"Original list: {nums}")
# print(f"Updated list with all positve numbers: {positive_nums}")


    
#show the list with positive numbers without creating a new list

# nums = [55, 76, -28, 32, 98, -25]

# idx_pos = 0

# for i in range(len(nums)):
#     if nums[i] >= 0:
#         nums[idx_pos] = nums[i]
#         idx_pos += 1

# del nums[idx_pos : ]

# print(nums)


#find the second largest element



#find second largest element
# nums = [10, 5, 5, 20, 20]
# second_highest = float('-inf')
# highest = float('-inf')

# for i in range(len(nums)):
#     if nums[i] > highest:
#         second_highest = highest
#         highest = nums[i]

#     elif nums[i] < highest and nums[i] > second_highest:
#         second_highest = nums[i]

# print(f"The Second Largest Element from the list is {second_highest}")



#count frequency
#and max frequency element

# nums = [10, 5, 5, 20, 20]
# elements = {}
# for num in nums:
#     if num in elements:
#         elements[num] += 1
#     else:
#         elements[num] = 1

# max_count = 0
# max_element = None

# for key, value in elements.items():
#     if value > max_count:
#         max_count = value
#         max_element = key


# print(f"Most Frequent Element: {max_element} appears {max_count} times")

#remove duplicates
# nums = [10, 5, 5, 20, 20]

# unique_vals = []

# for num in nums:
#     if num not in unique_vals:
#         unique_vals.append(num)
# print(unique_vals)


#print common elements

# nums1 = [35, 47, 68, 98, 55, 20]
# nums2 = [55, 76, -28, 32, 98, -25]

# common_elemnts = []


# for i in range(len(nums1)):
#     if nums1[i] in nums2:
#         common_elemnts.append(nums1[i])

# print(f"The common elements from both the lists are: {common_elemnts}")


#subarray sum

# nums = [35, 47, 68, 98, 55, 20]

# n = len(nums)

# for i in range(n):

#     current_sum = 0

#     for j in range(i, n):
#         current_sum += nums[j]
#         print(f"Subarray ({i},{j}) sum = {current_sum}")
    


#Given this list, print the sum of each subarray only if the sum becomes greater than 50. Stop expanding that subarray once it exceeds 50.

# nums = [12, 18, 7, 25, 30, 4]

# n = len(nums)

# for i in range(n):
#     current_sum = 0


#     for j in range(i, n):
#         current_sum += nums[j]
#         if current_sum <= 50:
#             continue
            
#         print(f"Subarray ({i},{j} sum = {current_sum})")

#         if current_sum > 50:
#             break
        

        
#Try all subarrays, but only consider ones whose sum is strictly less than 60. Among them, print the length of the longest subarray you found.

nums = [10, 15, 5, 20, 8, 12]

max_length = 0
best_range = None

n = len(nums)

for i in range(n):
    
    current_sum = 0

    for j in range(i, n):

        current_sum += nums[j]

        if current_sum >= 60:
            break

        length = j - i + 1
        if length > max_length:
            max_length = length
            best_range = (i, j)

        print(f"Subarray ({i},{j} sum = {current_sum})")

print("\nLongest subarray with sum < 60 is:", best_range, "with length:", max_length)


