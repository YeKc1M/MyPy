# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def practice1():
    i = 1
    while i <= 100:
        print(i)
        i += 1

def practice2():
    n = int(input())
    last = 0
    current = 0
    i = 0
    while i <= n:
        if i == 0:
            current = 0
        elif i == 1:
            last = 0
            current = 1
        else:
            currentHolder = last + current
            last = current
            current = currentHolder
        print(current)
        i += 1

def practice3():
    n = int(input())
    i = 0
    l = list()
    while i < n:
        l.append(i)
        i += 1
    print(l)

def practice4():
    start = int(input())
    end = int(input())
    l = list()
    while start < end:
        l.append(start)
        start += 1
    print(l)

def practice5():
    start = int(input())
    end = int(input())
    step = int(input())
    l = list()
    while start < end:
        l.append(start)
        start += step
    print(l)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # practice1()
    # practice2()
    # practice3()
    # practice4()
    practice5()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


