#--------------------------- O(N)---------------------------#
# def two_sum(numbers, target):
#     hash_table = {}
#     for number in numbers:
#         print(hash_table)
#         hash_number = target - number
#         if hash_number in hash_table:
#             return [hash_number, number]
#         else:
#             hash_table[number] = True
#     return []

#----------------------------O(N log(N))--------------------#

def two_sum(numbers, target):
    numbers.sort()
    left_p = 0
    rigth_p = len(numbers) - 1

    while left_p < rigth_p:
        sum = numbers[left_p] + numbers[rigth_p]
        if sum == target:
            return [numbers[left_p], numbers[rigth_p]]
        elif sum > target:
            rigth_p -= 1
        elif sum < target:
            left_p += 1
    return []

#------------------------------------Test-------------------------------------#


target = 5
numbers = [4, 1, 2, -2, 11, 15, 1, -1, -6, -4]
numbers2 = [4, 1, 2, -2, 13, -1, -6, -4]

res = two_sum(numbers, target)

print(res)
