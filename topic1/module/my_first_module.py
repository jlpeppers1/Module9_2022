def hello(name):
    print("Hello, " + name)

def average(l = []):
    sum = 0
    count = len(l)
    for x in l:
        sum = sum + x
    return sum/count
