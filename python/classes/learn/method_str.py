class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year
    
    def __str__(self):
        return f"Name: {self.name}, Build Year: {self.build_year}"

# Creating a Robot object
marvin = Robot("Marvin", 1979)

# Using the str() function and print() on the object
print(str(marvin))  ## Output: Name: Marvin, Build Year: 1979
print(marvin)       # Output: Name: Marvin, Build Year: 1979
