'''
#Problem Statement

Write a function to find all pairs of an integer array whose sum is equal to a given number. 
Do not consider commutative pairs.

Example

pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
Output : ['2+5', '4+3', '3+4', '-2+9']


Note:

4+3 comes from second and third elements from the main list.

3+4 comes from third and seventh elements from the main list.

'''

#Solution : 1


def pair_sum(myList, sum):
    pairs = []
    n = len(myList)
    
    # Loop through all pairs
    for i in range(n):
        for j in range(i + 1, n):
            if myList[i] + myList[j] == sum:
                pairs.append(f"{myList[i]}+{myList[j]}")
    
    return pairs

# Example usage:
result = pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7)
print(result)  # Output: ['2+5', '4+3', '3+4', '-2+9']

#======================================================

#Leetcode Solution 


#Define the function pairSum that takes the input array arr and the target sum target_sum as arguments.
def pair_sum(arr, target_sum):


#Initialize an empty list called result to store the pairs that add up to the target sum.
    result = []

#Start a loop iterating through the indices of the input array with the loop variable i.
    for i in range(len(arr)):

#Inside the outer loop, start another loop iterating through the indices of the input array.
#Starting from i+1 to avoid comparing an element with itself or repeating pairs. The loop variable is j.
        for j in range(i+1, len(arr)):

#Check if the sum of the elements at index i and index j of the input array equals the target sum.
            if arr[i] + arr[j] == target_sum:

#If the sum of the elements at index i and index j equals the target sum, 
#append a formatted string containing the pair to the result list.
                result.append(f"{arr[i]}+{arr[j]}")

#After iterating through all pairs in the array, 
#return the result list containing the pairs that add up to the target sum.                
    return result

#Define the input array for testing purposes.
arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]

#Define the target sum for testing purposes.
target_sum = 7

#Call the pairSum function with the input array and target sum, and print the resulting list of pairs.
print(pair_sum(arr, target_sum))  # Output: ['2+5', '4+3', '3+4', '-2+9']

'''
Time and Space Complexity:

The time complexity of the pair_sum function is O(n^2), where n is the length of the input array arr. 
This is because the function uses nested loops, and for each element in the array, 
it checks every other element in the array for possible pairs.

The space complexity of the pair_sum function is O(n), where n is the length of the input array arr. 
The additional space used in this function is the result list, 
which stores the pairs that add up to the target sum. 
In the worst case, the number of pairs that sum up to the target value is proportional
to the size of the input array.

'''

