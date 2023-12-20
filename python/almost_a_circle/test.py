def update(*args,**kwargs):
    # Initialize variables with None
    a, b, c, d, e = None, None, None, None, None

    # Assign values from args to variables
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
    #print(a, b, c, d, e)
    list=[]
    name=[]
    for key,value in kwargs.items():
        list.append(value)
        name.append(key)
    print(list)
    print(name)       
    
    print(a,b,c,d,e)    
             

# Test cases
update(a=10,b=15)               # Stores 4, leaves b, c, d, e as None
#update(4, 5)            # Stores 4 and 5, leaves c, d, e as None
#update(4, 5, 6, 7, 8)   # Stores all 5 values
