# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
# def biggie_size(nums):
#     newNums = []
#     for i in nums:
#         if i >= 0:
#             newNums.append("Big")
#         else:
#             newNums.append(i)

#     return newNums

# testNums = [-1, 3, 5, -5]
# print(biggie_size(testNums))


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
# def count_positives(nums):
#     count = 0
#     for num in nums:
#         if num > 0:
#             count += 1

#     nums[-1] = count

#     return nums


# testNums = [1, 6, -4, -2, -7, -2]
# print(count_positives(testNums))


# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
# def sum_total(nums):
#     sum = 0
#     for num in nums:
#         sum += num
#     return sum


# testNums = [1, 2, 3, 4]
# print(sum_total(testNums))


# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5
# def average(nums):
#     sum = 0
#     for num in nums:
#         sum += num
#     avg = sum / len(nums)
#     return avg


# testNums = [1, 2, 3, 4]
# print(average(testNums))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
# def length(nums):
#     return len(nums)


# testNums = [37, 2, 1, -9]
# print(length(testNums))


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
# def minimum(nums):
#     if len(nums) > 0:
#         minimum = nums[0]
#         for num in nums:
#             if num < minimum:
#                 minimum = num
#         return minimum
#     else:
#         return False


# testNums = [37, 2, 1, -9]
# print(minimum(testNums))


# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
# def maximum(nums):
#     if len(nums) > 0:
#         maxNum = nums[0]
#         for num in nums:
#             if num > maxNum:
#                 maxNum = num
#         return maxNum
#     else:
#         return False


# testNums = [37, 2, 1, -9]
# print(maximum(testNums))


# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
# def ultimate_analysis(nums):
#     sumTotal = 0
#     average = 0
#     minimum = nums[0]
#     maximum = nums[0]
#     for num in nums:
#         if num < minimum:
#             minimum = num
#         elif num > maximum:
#             maximum = num
#         sumTotal += num
#     average = sumTotal / len(nums)

#     return {'sumTotal': sumTotal, 'average': average, 'minimum': minimum, 'maximum': maximum, 'length': len(nums)}


# testNums = [37, 2, 1, -9]
# print(ultimate_analysis(testNums))


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
# def reverseList(nums):
#     return nums[::-1]


# testNums = [37, 2, 1, -9]
# print(reverseList(testNums))
