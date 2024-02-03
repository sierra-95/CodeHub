def update(*args):
    # Initialize variables with None
    a, b, c, d, e = None, None, None, None, None

    # Assign values from args to variables
    #you say greater or equal to so that
    #no matter the len() , the previous value is always assigned
    #eg len()=3
    #a,b and c will be assigned
    #summary: using b
    #ALWAYS ASSIGN arg[1] to b WHETHER ARGS>2 OR EQUAL THAN 2. BUT IF ARGS
    #IS LESS, DONT ASSIGN b
    if len(args) >= 1:
        a = args[0]
    if len(args) >= 2:
        b = args[1]
    if len(args) >= 3:
        c = args[2]
    if len(args) >= 4:
        d = args[3]
    if len(args) >= 5:
        e = args[4]

    # Print all variables
    print(a, b, c, d, e)

# Test cases
update(4)               # Stores 4, leaves b, c, d, e as None
update(4, 5)            # Stores 4 and 5, leaves c, d, e as None
update(4, 5, 6, 7, 8)   # Stores all 5 values
