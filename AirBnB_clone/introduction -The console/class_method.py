#Class methods are bound to the class itself rather than to instances of the class.
class MyClass:
    class_variable = "Hello, world!"

    @classmethod
    #they receive the class itself as parameter and not "self"
    def class_method(cls):
        print(cls.class_variable)

MyClass.class_method()  # Output: Hello, world!
e