def my_decorator(some_function):

    def wrapper():

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper

@my_decorator(lambda x: x==True)
def just_some_function():
    print("Wheee!")

if __name__ == "__main__":
    just_some_function()