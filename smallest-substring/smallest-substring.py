"""
"""
def get_shortest_unique_substring(arr, str):
  letter_dict = set(str)
  # check if all letters are in there
  for item in arr:
    if item not in letter_dict:
      return ""
  new_string = str
  length = len(arr)
  left = 0
  right = len(str) 
  
  current = str
  # first get the left val
  while helper(current[left+1:right], arr) == True:
    left += 1
  # now get the right val
  while helper(current[left:right-1], arr) == True:
    right -= 1
  
  return current[left:right]
      

  
def helper(str, arr):
    """ return true if all letters in string"""
    letter_dict = set(str)
    # check if all letters are in there
    for item in arr:
      if item not in letter_dict:
        return False
    return True

arr = ['A','B','C']
str = "ADOBECODEBANCDDD"
print(get_shortest_unique_substring(arr, str))
  