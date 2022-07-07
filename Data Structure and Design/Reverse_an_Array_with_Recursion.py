#First Solution
def reverse(array):
  # Base case1
  if len(array) == 0: # If we encounter an empty array, simply return an empty array
    return []
  
  # Base case2
  elif len(array) == 1 : # Inverting an array of size 1 returns the same array
   return array

  # Recursive case
  return [array[len(array) - 1]] + reverse(array[:len(array) - 1])
  # The first part is storing the last element to be appended later
  # The second part is calling another instance of the same function with the last element removed

# Driver Code
array = [1, 2, 3, 4]
print(reverse(array))
#Second Solution
