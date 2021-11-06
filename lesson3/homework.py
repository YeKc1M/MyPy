

def homework1():
    a = int(input())
    if a > 0 :
        print("a为正数")
    else:
        print("a不为正数")

def homework2():
    a = float(input())
    b = float(input())
    if a > b:
        print("大于")
    else:
        print("不大于")

def homework3():
    if input() == input():
        print("等于")
    else:
        print("不等于")

def homework4():
    y = float(input())
    a = float(input())
    b = float(input())
    x = float(input())
    if x == (y - b)/a:
        print("正解")
    else:
        print("错解")

if __name__ == "__main__":
    # homework1()
    # homework2()
    # homework3()
    homework4()

