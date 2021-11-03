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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # practice1()
    practice2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


