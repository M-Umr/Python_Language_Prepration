# a function get values in dictionary format so
# args represent tuple, non-key
# kwargs represent dictionary
def example_func(a, b, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

example_func(1, 2, 3, 4, c=5, d=6)
#result:
# a: 1
# b: 2
# args: (3,4)
# kwargs: {c:5, d:6}