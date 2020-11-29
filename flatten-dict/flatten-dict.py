"""


"""

def flatten_dictionary(dictionary):
  return helper(dictionary)
  
def helper(dictionary):
  """ return value if not dict. otherwise, do recursion"""
  output_dict = {}
  for key in dictionary:
    #check if value is dictionary
    if type(dictionary[key]) is dict:
      result = helper(dictionary[key])  # inner_dict is flattened
      for inner_key, inner_value in result.items():
        if key == "":
          output_dict[key + inner_key] = inner_value
        elif inner_key == "":
          output_dict[key] = inner_value
          
        else:
          output_dict[key + "." + inner_key] = inner_value
          
    else:
      output_dict[key] = dictionary[key]
    
  return output_dict
  
  
test_dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

print(flatten_dictionary(test_dict))


#'Key2.c.e.': '1'
#'Key2.c.e': '1'  # correct
