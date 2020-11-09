"""

GOAL: compute min energy required for flight

x, y
z: height

- each row represents diff point in space that it goes thru

- gains 1kWH when it goes down
- loses 1KWH when it goes up

- iterate through each row and rack the change in z
0: N/A
1: 10 -> 0: lost 10 miles altidue. gain 10KWH
2. 0 -> go up 6 miles, lose 6 KWH
3. 6 -> 15. go up 9, lose 9
4. go down 7, gain 7

- calculate the cumulative KWH that we have
- compute the min we need to start with, so we never go below 0

- find lowest cum. KWH and get -n and return that

TEST CASES: 
1)
>>> min_drone_energy([ [0, 2, 10], [3,   5,  0], [9,  20,  6], [10, 12, 15], [10, 10,  8] ])
5



"""


def min_drone_energy(route):
  """Return the min energy required."""

  cum_energy = 0
  min_energy = 0
  alt_change = 0
  
  # loop through the list and calculate the change in altitude and correspond change in KWH
  for i in range(1, len(route)):
    current_alt = route[i][2]
    alt_change = current_alt - route[i-1][2]
    cum_energy += -alt_change
    if cum_energy < min_energy:
      min_energy = cum_energy
      
    
  return -min_energy


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")
