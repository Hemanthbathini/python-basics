# def movies():
#     fav_movies = []
    
#     for i in range(3):
#         user_input = input("enter your fav movie: ")

#         fav_movies.append(user_input)

#     print(f"your fav movies are {fav_movies}")

# movies()

# def is_palindrome(nums):
# n = len(nums)


#     for i in range(len(nums)):
#         if nums[i] != nums[n-i -1]:
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

# nums = [10, 15, 5, 20, 8, 12]

# max_length = 0
# best_range = None

# n = len(nums)

# for i in range(n):
    
#     current_sum = 0

#     for j in range(i, n):

#         current_sum += nums[j]

#         if current_sum >= 60:
#             break

#         length = j - i + 1
#         if length > max_length:
#             max_length = length
#             best_range = (i, j)

#         print(f"Subarray ({i},{j} sum = {current_sum})")

# print("\nLongest subarray with sum < 60 is:", best_range, "with length:", max_length)




#maximum subarray sum

# nums = [10, 15, 5, 20, 8, 12]
# n = len(nums)
# max_subarray = float('-inf')
# for i in range(n):
#     current_sum = 0

#     for j in range(i, n):
#         current_sum += nums[j]
#         if current_sum > max_subarray:
#             max_subarray = current_sum
#         print(f"Subarray ({i},{j}) sum = {current_sum}")

# print(max_subarray)


#pair sum

# nums = [35, 47, 68, 98, 55, 20]

# target = 166
# n = len(nums)
# found = False

# for i in range(n):

#     for j in range(i+1, n):
#         if nums[i] + nums[j] == target:
#             print(f"pair found at indexes ({i},{j}) sum = {target}")
#             found = True
#             break
#     if found:
#         break 
# if not found:
#     print("no pair sums to target")


# nums = [10, 15, 5, 20, 8, 12]
# total_sum = 0

# for i in range(len(nums)):
#     total_sum += nums[i]

# if len(nums) == 0:
#     print("The list is empty!")
# else:
#     average_sum = total_sum//len(nums)
#     print(f"Total sum of the list is {total_sum}")
#     print(f"The average of all numbers is {average_sum}")



# nums = [10, 15, 5, 20, 8, 12]
# highest = float("-inf")
# miniumum = float("inf")

# for i in range(len(nums)):
#     if nums[i] > highest:
#         highest = nums[i]
#     if nums[i] < miniumum:
#         miniumum = nums[i]
# print(highest)
# print(miniumum)


# nums = [10, 15, 5, 20, 8, 12]
# even_count = 0
# odd_count = 0

# for i in range(len(nums)):
#     if nums[i]%2 == 0:
#         even_count += 1       
#     else:
#         odd_count += 1

# print(f"total number of even numbers: {even_count}")
# print(f"total number of odd numbers: {odd_count}")

# nums = [10, 15, 5, 20, 8, 12]

# reverse_list = []

# for i in range(len(nums)-1, -1, -1):
#     reverse_list.append(nums[i])

# print(nums)
# print(reverse_list)


# nums = [25, 26, 27]
# is_sorted = True

# for i in range(1, len(nums)):
#     if not nums[i] >= nums[i-1]:
#         is_sorted = False
#     else:
#         is_sorted = True

# print(is_sorted)



# nums = [10, 15, 5, -20, 8, -12]

# positive_nums = []

# for i in range(len(nums)):

#     if nums[i] >= 0:
#         positive_nums.append(nums[i])

# print(positive_nums)


# nums = [10, 15, 5, 20, 20, 20, 8, 12]

# largest = float("-inf")
# second_largest = float("-inf")

# for i in range(len(nums)):

#     if nums[i] > largest:
#         second_largest = largest
#         largest = nums[i]
#     elif nums[i] < largest and nums[i] > second_largest:
#         second_largest = nums[i] 

    
# print(second_largest)
# print(largest)


# nums = [10, 15, 5, 20, 20, 20, 8, 12]

# elements = {}
# n = len(nums)

# for i in range(n):
#     if nums[i] in elements:
#         elements[nums[i]] += 1
#     else:
#         elements[nums[i]] = 1

# print(elements)

# max_count = 0 
# max_element = None

# for key, value in elements.items():
#     if value > max_count:
#         max_count = value
#         max_element = key

# print(max_element)
# print(max_count)


# nums = [10, 15, 5, 20, 20, 20, 8, 12]

# unique_nums = []

# for num in nums:
#     if not num in unique_nums:
#         unique_nums.append(num)
# print(unique_nums)


# nums1 = [10, 15, 5, 20, 20, 20, 8, 12]
# nums2 = [35, 47, 68, 98, 55, 20]
# nums3 = []

# for i in range(len(nums1)):
#     if nums1[i] in nums2:
#         if nums1[i] not in nums3:
#             nums3.append(nums1[i])
        

# print(nums3)



# nums = [35, 47, 68, 98, 55, 20]

# n = len(nums)


# for i in range(n):

#     current_sum = 0


#     for j in range(n):

#         current_sum += nums[j]
#         print(f"({i},{j}) sum = {current_sum}") 



# nums = [35, 47, 68, 98, 55, 20]
# n = len(nums)
# max_subarray = float("-inf")

# for i in range(n):
#     current_sum = 0

#     for j in range(i, n):

#         current_sum += nums[j]

#         if current_sum > max_subarray:
#             max_subarray = current_sum
#         print(f"({i},{j}) sum = {current_sum}")

# print(f"max_subarray = {max_subarray}")
        

# nums = [35, 47, 68, 98, 55, 20]

# target = 166
# n = len(nums)
# found = False

# for i in range(n):

#     for j in range(i+1, n):
#         if nums[i] + nums[j] == target:
#             print(f"pair found at indexes ({i},{j}) sum = {target}")
#             found = True
#             break

#     if found:
#         break 
# if not found:
#     print("no pair sums to target")



# Given a list, overwrite it to keep only non-negative numbers (≥0) using the write_index pattern, then trim the rest with slicing delete.


# nums = [35, -47, 68, -98, 55, 20]

# pos_idx = 0

# for i in range(len(nums)):
#     if nums[i] >= 0:
#         nums[pos_idx] = nums[i]
#         pos_idx += 1

# del nums[pos_idx:]

# print(nums)



# Move All Zeros to End. * Maintain order of non-zero elements

# nums = [35, 0, -68, 0, 55, 20]

# non_zero = 0

# for i in range(len(nums)):
#     if not nums[i] == 0:
#         nums[non_zero] = nums[i]
#         non_zero += 1

# for j in range(non_zero, len(nums)):
#     nums[j] = 0

# print(nums)



# Rotate List by K Positions. k=2 

# nums = [35, 0, -68, 0, 55, 20]
# k = 2
# n = len(nums)
# k = k % n


# nums[:] = nums[n-k:] + nums[: n-k]

# print(nums)


# nums = [35, 25, 68, 56, 55, 20, 77]
# n = len(nums)
# max_len = 1
# curr_len = 1

# for i in range(1, n):
#     if nums[i] > nums[i - 1]:
#         curr_len += 1
#         if curr_len > max_len:
#             max_len = curr_len
#     else: 
#         curr_len = 1


# print(max_len)



# def majority_element(nums):
#     n = len(nums)

#     if n == 0:
#         return None


#     for i in range(n):

#         count = 0

#         for j in range(n):
#             if nums[j] == nums[i]:
#                 count += 1
#         if count > n//2:
#             return nums[i]
#     return None

# nums = [24, 67, 67, 67, 89]
# print(majority_element(nums))


# def is_palindrome(nums):
#     n = len(nums) -1

#     for i in range(len(nums)):
#         if nums[i] != nums[n - i]:
#             return False
#     return True
        
# nums = [1,2,3,2,0] 
# print(is_palindrome(nums))



# def merge_sorted_lists():
#     nums1 = [25, 36, 45, 63, 78, 90]
#     nums2 = [12, 17, 28, 30, 37]
#     merged = []

#     i = 0
#     j = 0

#     while i < len(nums1) and j < len(nums2):

#         if nums1[i] < nums2[j]:
#             merged.append(nums1[i])
#             i += 1
#         else:
#             merged.append(nums2[j])
#             j += 1

#     while i < len(nums1):
#         merged.append(nums1[i])
#         i += 1

#     while j < len(nums2):
#         merged.append(nums2[j])
#         j += 1

#     return merged


# print(merge_sorted_lists())
                                   


# def find_missing_num():

#     nums = [1, 2, 3, 4]
#     n = 5
#     expected_sum = n * (n + 1)//2
#     actual_sum = 0

#     for i in nums:
#         actual_sum += i

#     return expected_sum - actual_sum


# print(find_missing_num())


                                                  
# def sum_average(nums):

#     total_sum = 0 

#     for i in range(len(nums)):
#         total_sum += nums[i]

#     average = total_sum//len(nums)

#     return average, total_sum

# average, total_sum = sum_average([45, 78, 95, 23, 49, 37])
# print(f"average of the list is {average}")
# print(f"total sum of all numbers: {total_sum}")


# def find_largest_smallest(nums):

#     while True:

#         user_input = input("enter any number(q to quit): ").lower().strip()

#         if user_input == "q":
#             print("Thank you for joining us! See you later")
#             break

#         try:
#             num = int(user_input)
#             nums.append(num)
#         except ValueError:
#             print("Enter a valid number")
#     if len(nums) > 0: 
#         highest = largest(nums)
#         lowest = smallest(nums)

#         print(f"highest is {highest}")
#         print(f"lowest is {lowest}")

        

# def largest(nums):

#     highest = nums[0]

#     for i in range(len(nums)):
#         if nums[i] > highest:
#             highest = nums[i]
#     return highest


# def smallest(nums):

#     smallest = nums[1]

#     for i in range(len(nums)):
#         if nums[i] < smallest:
#             smallest = nums[i]

#     return smallest



# nums = []
# find_largest_smallest(nums)



# nums = [25, 36, 45, 63, 78, 90]

# even_count = 0
# odd_count = 0

# for i in range(len(nums)):
#     if nums[i]% 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print(f"the num of even numbers: {even_count}")
# print(f"the num of odd numbers: {odd_count}")
        


# nums = [25, 36, 45, 63, 78, 90]

# for i in range(len(nums)-1, -1, -1):
#     print(nums[i])


# nums = [25, 36, 45, 63, 78, 90]

# is_sorted = False

# for i in range(1, len(nums)):

#     if not nums[i] > nums[i-1]:
#         is_sorted = False

#     else:
#         is_sorted = True

# print(is_sorted)



# nums = [25, 36, 45, 63, 78, 90]


# def Second_largest(nums):

#     highest = float("-inf")
#     second_highest = float("-inf")

#     for i in range(len(nums)):

#         if nums[i] > highest:
#             second_highest = highest
#             highest = nums[i]
#         elif second_highest < nums[i] and nums[i] < highest:
#             second_highest = nums[i]
    
#     return second_highest

# print(Second_largest(nums))



# nums = [25, 36, 45, 63, 63, 78, 90]

# element_count = {}

# for i in range(len(nums)):

#     if nums[i] in element_count:
#         element_count[nums[i]] += 1

#     else:
#         element_count[nums[i]] = 1
# max_count = 1
# element = None

# for key, vlaue in element_count.items():
#     if value > max_count:
#         max_count = value
#         element = key

# print(f"{element} = {max_count}")



# nums = [25, 36, 45, 63, 63, 78, 90]

# max_subarray = float("-inf")

# for i in range(len(nums)):
#     current_sum = 0
#     for j in range(i,len(nums)):
#         current_sum += nums[j]
#         if current_sum > max_subarray:
#             max_subarray = current_sum
# print(max_subarray)


# nums = []

# target = 108
# is_found = False
# n = len(nums)

# for i in range(n):
#     current_sum = 0
#     for j in range(n-1):
#         if nums[i] + nums[j + 1] == target:
#             print(f"pair sum is ({i},{j}) = {target}")
#             is_found = True
#             break
#     if is_found:
#         break
# if not is_found:
#     print("No pair sum match to target")




# nums = [25, 36, 45, 63, 63, 78, 90]
# curr_length = 1
# max_length = 1

# for i in range(1, len(nums)):
#     if nums[i] >= nums[i-1]:
#         curr_length += 1
    
#         if curr_length > max_length:
#             max_length = curr_length
#     else:
#         curr_length = 1


# print(max_length)


# nums = [63, 36, 63, 63, 63, 78, 90]
# n = len(nums)
# count = 1
# max_element = 0

# for i in range(n):
#     count = 1
#     for j in range(n-1):
#         if nums[i] == nums[j + 1]:
#             count += 1
#         if count > n//2:
#             max_element = nums[i]
#             break
#     break
# print(max_element)



# nums1 = [25, 36, 45, 53, 78, 90]
# nums2 = [16, 28, 32, 44, 56, 78]
# i = 0
# j = 0
# merged = []

# for _ in range(len(nums1) + len(nums2)):
#     if i < len(nums1) and j < len(nums2):
#         if nums1[i] < nums2[j]:
#             merged.append(nums1[i])
#             i += 1
#         else:
#             merged.append(nums2[j])
#             j  += 1

#     elif i < len(nums1):
#         merged.append(nums1[i])
#         i += 1

#     elif j < len(nums2):
#         merged.append(nums2[j])
#         j += 1

# print(merged)



# nums = [1, 2, 3, 5]
# n = 5
# expected_total = n * (n+1)//2
# actual_sum = 0

# for i in range(len(nums)):
#     actual_sum += nums[i]

# missing_num = expected_total - actual_sum

# print(missing_num)



# def is_palindrome():
#     nums = [1, 2, 3, 2, 1]
#     n = len(nums) - 1

#     for i in range(len(nums)//2):
#         if nums[i] != nums[n - i]:
#             return False
#         else:
#             return True
        
# print(is_palindrome())








    






        
































