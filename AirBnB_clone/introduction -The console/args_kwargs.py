def test_var_args(f_arg, *args):
    print ("first normal arg:", f_arg)
    #you use *arg when you dont know how many arguments the user will pass
    #used for non-keyworded variables
    for arg in args:
        print ("another arg through *args :", arg)

test_var_args('yasoob','python','eggs','test')
###########################################################
print("\n")
def greet_me(**kwargs):
    #used for named variables eg dictionaries etc
    if kwargs is not None:
        for key, value in kwargs.items():
            print ("%s == %s" %(key,value))
greet_me(name="yasoob")
###########################################################
#Kwargs vs Dictionaries
def my_func(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)

my_func(fruite="apple",quantity=3,color="red")
###########################################################
#when storing values in dictionary we use this format:
class MyClass:
    def __init__(self):
        self.__x = None
        self.__y = None
        self.__width = None
        self.__height = None
        self.id = None

    def create_dict(self, **kwargs):
        for key, value in kwargs.items():
            if key == "x":
                self.__x = value
            elif key == "y":
                self.__y = value
            elif key == "width":
                self.__width = value
            elif key == "height":
                self.__height = value
            elif key == "id":
                self.id = value
obj = MyClass()
obj.create_dict(x=1, y=2, width=3, height=4, id=5)


