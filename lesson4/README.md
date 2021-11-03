# lesson 4: 循环

## while循环

```python
i = 0
while i < 100:
    i = i + 1
```

```python
i = 0
while i < 100:
    i = i + 1
else:
    print("i >= 100")
```

### practice

1. 输出1-100（包含100）所有的整数
2. 斐波那契数列，又称黄金分割数列。指数列的第n项等于数列第n-1项与n-2项之和，即F(0)=0,F(1)=1,F(2)=1,F(3)=2,F(4)=3,F(5)=5,F(6)=8,F(7)=13。
   1. 输入整数n，输出斐波那契数列的0到第n项

## 列表（list）

列表是一个包含了多个变量的变量

### 初始化

1. `l = []`
2. `l = list()`

### 列表的基本操作

- 向列表末尾添加一个元素
  - `l.push(element)`
- 删除列表最后一个元素
  - `l.pop()`

### practice

3. 输入整数n，获得从0到n（不含n）的所有整数的列表
4. 输入整数a，整数b，获得从a到b所有整数的列表（假设b>a)
5. 输入整数a，整数b，整数c，获得从a开始，间隔c，直到b结束的所有整数的列表
   1. 示例：输入0，10，3。输出[0,3,6,9]

## for循环

```python
for element in iterable_variable:
    # your code here
    print(element) # an example
```


