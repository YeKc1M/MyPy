# 变量

用来存储程序中可变化的值

变量的命名规则
* 由字母、数字、下划线（_）组成，必须含字母，不能以数字开头
* 不能是python关键字（input、int、print、main等）
* 不能包含空格

## practice:以下哪些命名是正确的
* ab2cd
* ab_123cd
* 34s
* 123456
* a1
* a#d

基本命名规范
* 变量命名应该能体现出变量包含数据的含义
```python
# 符合规范的变量命名方式
name = 'harry, potter'
age = 18
current_year = 2021
now_time = '2021/9/4'
eng_language = 'English'
```
```python
# 不符合规范的变量命名方式
a1 = 'harry potter'
a2 = 18
a3 = 2021
x = '2021/9/4'
_y = 'English'
```
* 驼峰和下划线命名
```python
# 驼峰法
current_year = 2021
now_time = '2021/9/4'
eng_language = 'English'
# 下划线
currentYear = 2021
nowTime = '2021/9/4'
engLanguage = 'English'
```

基本变量类型：数字、字符串、布尔

# 数字变量

整型（int）：存储数据格式为整数

浮点型（float）：存储数据格式为小数

数字运算符 + - * / ** % //

运算顺序：同数学运算顺序

## practice

1. 输入a，b，c，d四个变量，控制台打印出a加b的和乘以c再除以d的值
2. 输入a，b，c三个变量，控制台打印出a的b次方加c的值

# 字符串变量

用"或'引起来

```python
str = '这是一个字符串变量'
str = "这是另一个字符串变量的值"
str = '''123
456
789'''
```

## 字符串变量的运算

- 拼接字符串： +
```python
str1 = 'hello,'
str2 = 'world'
print(str1 + str2)
```
- 字符串截取： []
```python
str = 'python'
print(str[2])
print(str[1:3])
print(str[3:])
print(str[:-1])
```
- 大小写转换：lower()/upper()
```python
str = 'python'
print(str.upper())
```
- 字符串中插入变量：占位符
```python
a = 1
b = 3
print('%d+%d=%d'%(a,b,a+b))
```

### practice：尝试字符串的乘法

```python
str1 = 'abcd'
str2 = '12a'
print(str1 * 2)
print(str1 ** 2)
print(str1 * str2)
```

## 转义字符

- \'
- \"
- \\
- \000
- \n
- \t

## 数字变量与字符串变量

## (optional) is

自学内容
