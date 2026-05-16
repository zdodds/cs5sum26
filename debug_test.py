#
# python debugging example
#


print("Hello world. This is version 2 of this file...")

def f(x):
    """ a docstring for the function f """
    for i in range(100):
        print(i)
        if i == 42:
            print("The answer to the Ultimate Question of Life, The Universe, and Everything")  
            # drop into a debugger here
            import pdb; pdb.set_trace()

    return x + i + 42

# run the function
result = f(10)
print("Result:", result)
