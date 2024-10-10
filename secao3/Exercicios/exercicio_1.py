''' LINK_: https://www.codewars.com/kata/595aa94353e43a8746000120
An ordered sequence of numbers from 1 to N is given. One number might have deleted from it, then the remaining numbers were mixed. Find the number that was deleted.

Example:

The starting array sequence is [1,2,3,4,5,6,7,8,9]
The mixed array with one deleted number is [3,2,4,6,7,8,1,9]
Your function should return the int 5.
If no number was deleted from the starting array, your function should return the int 0.

Note: N may be 1 or less (in the latter case, the first array will be []).
'''

def lostone(arr, mixed_arr):
    if len(arr) == 0:
        return 0
    else:  
        for i in arr: 
            if i in mixed_arr:
                continue
            return i
        if len(arr) == arr[-1]:
            return 0
    
        
print(lostone([], [3,2,4,6,7,5,8,1,9]))


#melhor solcao: 

# def find_deleted_number(arr, mixed_arr):
#     lost = 0
#     for i in arr:
#         if i not in mixed_arr:
#             lost = i
            
#     return lost

# def find_deleted_number(arr, mixed_arr):
#     return sum(arr)-sum(mixed_arr)