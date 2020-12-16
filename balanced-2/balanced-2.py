#
# abc[def]123/ -> balanced
# [ab[cdef]ggg -> not balanced
# 
# balanced: for every [ there's ] that follows it 
"""

Return True if balanced, False if not balanced

abc][de -> False
abc[]cde] -> False
abcd -> ** special case -> True (for now)

saw_brackets = False
- when we get to '[' or ']', set saw_brackets = True


counter variable. 
- every time we see '[', increment counter
- when we see ']'
    - if counter = 0:, return False # a closer w/o opener
    - else, decrement counter

- if saw_brackets = False
    - return 'No Brackets'
- after we loop through the whole string, return True if counter = 0, else return False ## counter > 0, we have openers w/o closers

"""
def is_balanced(string):
    """Determine if brackets are balanced in string."""
    counter = 0
    saw_brackets = False
    if string is None:
        return 'Invalid'
    # loop through string and assess '[' and ']'
    for i in range(len(string)):
        # increment counter if char is opener
        if string[i] == '[':
            saw_brackets = True
            counter += 1 
        # if char is closer, determine if valid
        # if valid, decrement counter
        elif string[i] == ']':
            saw_brackets = True
            if counter == 0:
                return False
            else:
                counter -= 1
    ## assess if any unmatched openers
    if saw_brackets == False:
        return 'Invalid'
    if counter > 0:
        return False
    else:
        return True

#
# [ => ], < => >, ..., a => A, b => B, 
# stack to store most recent opening char
# dictionary to store opener/closer pairs
# pairs = { '<': '>'}
"""
- stack = []
- make a set to store dictionary keys (openers)
- make a set to store dictionary values (closers)
- iterate through string
- if char is in openers:
    - append char to stack
- if char is a closer
    - if stack is empty, return False
    - else, if pairs[stack[-1]] == char, stack.pop() ## it is a match
    - otherwise, return False
"""
def is_balanced_v2(string, config: dict):
    stack = [] 
    openers = set(config.keys())
    closers = set(config.values())
    
    for i in range(len(string)):
        if string[i] in openers:
            stack.append(string[i])
        elif string[i] in closers:
            # assess if stack is empty
            if stack == []:
                return False
            # pop if they are matching
            elif config[stack[-1]] == string[i]:
                stack.pop()
            else:
                return False
    # assess if stack is empty
    if stack == []:
        return True
    else:
        return False
                
    

config = {'[': ']', '<': '>', '(': ')', 'a': 'A'}

tests = [
    ('abc[]cde]',  False),
    ('abc[]cde', True),
    ('abc][de', False),
    ('abc', True),
    ('[ab[cdef]ggg', False),
    ('abc[[d[e]]]f', True),
    ('', True),
    ('<hi(bye)>', True),
    ('<hi(bye>', False),
    ('abA', True),
    ('(a)A', False)
    
]
for i, t in enumerate(tests):
    inp, exp_res = t
    res = is_balanced_v2(inp, config)
    success = "SUCCESS" if exp_res == res else "FAILURE"
    print(f"{i + 1}. '{inp}' -> {res} ({success})")
    
