# 布尔变量

值为true（真）/false（假）的变量

```python
trueValue = True
falseValue = False
```

## 布尔变量的运算

and, or, not

## 条件判断

- 等于==
- 大于>
- 小于<
- 大于等于>=
- 小于等于<=
- 不等于!=

### if

```python
a = input("请输入a：")
if a == 0:
    print("a等于0")
```

### if...else...

```python
a = input("请输入a：")
if a >0:
    print("a大于0")
else:
    print("a不大于0")
```

### if...elif...else

```python
a = input("请输入a：")
if a >0:
    print("a大于0")
elif a < 0:
    print("a小于0")
else:
    print("a等于0")
```

### practice

1. 阅读代码
```python
a = input("请输入a：")
b = input("请输入b：")
if a > 0 and b > 0:
    print(a * b)
    print(a)
```

```python
a = input("请输入a：")
b = input("请输入b：")
if a > 0 and b > 0:
    print(a * b)
print(a)
```

2. 编程：控制台输入a、b，如果a乘b大于0，输出“a和b同号”，否则输出“a和b异号”

# 列表

存放了一组变量的变量

# for循环

