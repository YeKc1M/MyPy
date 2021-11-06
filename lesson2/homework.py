
def homework1():
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a ** b)
    print(a % b)
    print(a // b)

def homework2():
    y = float(input())
    a = float(input())
    b = float(input())
    print((y - b) / a)

def homework3():
    a = input()
    b = int(input())
    print(a * b)

def homework4():
    a = input()
    length = len(a)
    if length % 2 == 0:
        half = int(length / 2)
        print(a[half - 1:half + 1])
    else:
        print(a[int(length/2)])

def homework5():
    a = input()
    b = input()
    lengtha = len(a)
    lengthb = len(b)
    result = ""
    if lengtha % 2 == 0:
        result = result + a[int(lengtha/2 - 1): int(lengtha/2) + 1]
    else:
        result = result + a[int(lengtha/2)]
    if lengthb % 2 == 0:
        result = result + b[int(lengthb/2 - 1): int(lengthb/2) + 1]
    else:
        result = result + b[int(lengthb/2)]
    print(result)

if __name__ == '__main__':
    # homework1()
    # homework2()
    # homework3()
    # homework4()
    homework5()