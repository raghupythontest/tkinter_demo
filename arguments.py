def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

def calculate(n,**kwargs):
    # kwargs is dictionary
    print(kwargs)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)



print(add(1, 2, 3, 4, 5, 6, 7, 8))
print(add(4, 5))
print(add(5))

print("key words args :")
calculate(2,add=3,multiply=5)
