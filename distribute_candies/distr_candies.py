"""
#1
Input: c= 7, p = 4
output: [1, 2, 3, 1]

#2 
Input: c = 10, p = 3
1 2 3 (6)
4
[5, 2, 3]

#3 
Input: c = 12, p = 3
1 2 3 (6)
4 2 0
[5, 4, 3]

- when there are leftovers
- when there are not leftovers
    - exact amount can be given back
    - return less than the exact amount
    
    
- track total candies distrbuted
- distribute candies to the correct person (c_dist)
- we know who to distribute it to by mod
- index will be the candies % people

- we want to continue dispersing candies until we have dispersed all of them
- we will want to disperse the MIN of the current dispersion, or the amount remaining
- each time you do it, update remaining candies
- make an array to store everyone
while there are remaining candies,
assign it to the person (current_disp % people) to get the index
then increment current dispersion. and assin to that person
then we will decrease remaining by the current dispersion

"""


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        candies_left = candies
        c_array = []
        for i in range(num_people):
            c_array.append(0)
        
        current_disp = 0
        while candies_left:
            idx = current_disp % num_people
            current_disp = min(current_disp+1, candies_left)
            c_array[idx] += current_disp
            candies_left -= current_disp
            print(candies_left)
            
        
        
        
        return c_array
        
        
        