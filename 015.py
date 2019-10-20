

# 2 x 2 grid,  has 3 choice points at 0,1,2
# At 0, there are 2 choices, at 1 there are 2 choices for both the options of 1 i.e. 0,1 and 1,0
# At level 2, there are no options 0,2 can only move in one way, 1,2 can also move in one way etc
# Therefore the options are a multiple of 2 x array size

# Let's try this
if __name__ == '__main__':
    n = 0
    for i in range(0,21):
        at_this_level = ((i+1) *2)
        n = n + at_this_level
    print(n)
