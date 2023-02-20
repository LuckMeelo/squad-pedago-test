

def invoke_function_with_itself_as_argument(function):
    return function(function)

invoke_function_with_itself_as_argument(invoke_function_with_itself_as_argument)


foo = [1,2,3,4,5,6]
foo = [foo.pop() for x in foo]

try:
    while input():
        print(foo)
except:
    print("END")