"""


"""
def decrypt(word):
  x = []
  if word == '':
    return ''
  for i in range(len(word)):
    x.append(ord(word[i]))

  letter_list = []
  ## loop through list of ord values and update them
  for i in range(len(x)):
    print(i)
    if i == 0:
      value = x[i] -1 
      letter_list.append(value)
    else:

      value = x[i] - x[i-1]
      print(value)
      if value > 96:
        letter_list.append(value)
      else:
        new_val = -((96 - value) % 26) + 122
        letter_list.append(new_val)
    
    ## create string to store the new letters
    final_str = ''
    for item in letter_list:
      final_str += chr(item)
    
  print(final_str)     
  return final_str
print(decrypt('dnotq'))

  
  