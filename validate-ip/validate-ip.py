"""

Edge cases:
Input: '200.50.252' -> False
Input: '23.23.23.23.23' -> False
Input: '12.12.12.x' -> False
Input: '400.2.2.2' -> False
Input: '0.0.0.00' _> False

Approaches:
- splitting the string by '.' and then iterating through the array
  - validate that length of list == 4
  - check each item use and convert to int. in the array to make sure it is an int between 0-255
  2a
  int(2a)

- iterating through string
  - temp string to hold value until we reach a period, then assess if 0-255
try int(item)
else:
return False

"""
#print(str(int('00')))->0 !="00" 0<=x<=255
def validateIP(ip):
  # convert address into list
  ip_list = ip.split('.')
  #validate length
  if len(ip_list) != 4:
    return False
  # iterate and validate each substring
  for substring in ip_list:
    try:
      x = int(substring)
      if 0<=x<=255 and str(x) == substring:
        continue
      else: 
        return False
    except:
      return False
  return True
print(validateIP('192.168.0.1')) ## true
print(validateIP('192.168.123.456')) # false
print(validateIP('0.0.0.00')) #false
print(validateIP('0.0.0.23x')) #false
print(validateIP('0.0.0.23')) #true