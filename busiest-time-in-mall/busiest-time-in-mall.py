"""
OBJ: return busiest time period. if tie, return earliest

- keep running count of visitors in mall
- when people exit, subtract amount. when people enter, add that amount

- max_count: maximum count of people
  - reset this when current count > max_count

- max_tims = value

- if current count > max_count
    max_times = [current_time]
    
 return max_times[0]
 
 - need to track total change over time
 
 - update current count once we know next value isn't current alue
 - make dictionary to store total change for each time
 
 key: time, value: cum change for time 
 
iterate through dictionary:
  calculate cumulative time
  return max time at the end. reset max value and max time if current_count > max count
 
 
 

"""

def find_busiest_period(data):
  times_dict = {}
  for item in data:
    time = item[0]
    change = item[1]
    entered = item[2]
    # handle if already in dict
    if time not in times_dict:
      if entered == 0:
        times_dict[time] = -change
      else:
        times_dict[time] = change
    else:
      if entered == 0:
        times_dict[time] -= change
      else:
        times_dict[time] += change
  print(times_dict)
  # shows cum change over period
  # iterate through
  # tieme_dict[1487799425] = 10   
  max_time = 0
  max_count = 0
  cum_count = 0
  for item in data:
    time = item[0]
    current_count = times_dict[time]
    cum_count += current_count
    if cum_count > max_count:
      max_count = cum_count
      max_time = time


  return max_time
    
data = [ [1487799425, 14, 1], 
             [1487799425, 4,  0],
             [1487799425, 2,  0],
             [1487800378, 10, 1],
             [1487801478, 18, 0],
             [1487801478, 18, 1],
             [1487901013, 1,  0],
             [1487901211, 7,  1],
             [1487901211, 7,  0] ]
print(find_busiest_period(data))
      