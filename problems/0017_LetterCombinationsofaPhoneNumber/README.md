```python
a = 'sdfgs'
print(len(a)) # 可以直接用len方法求一个字符串的长度
# result: 5



# 把一个字符串转成列表
b = list(a)
print(b)
# result: ['s', 'd', 'f', 'g', 's']


# 对一个字符串去重
aaa = 'aaddccs'
print(set(aaa))
# 不需要先转成list再用set，直接用set就可以对一个字符串进行去重。
# result：{'d', 'c', 'a', 's'}
# 但是得到的结果是一个set，set是不可遍历的，通常需要再将其转成list：
res = list(set(aaa))
print(f'res = {res}')
# result: res = ['d', 'a', 'c', 's']
# 这里要注意，转成list之后，原set中元素之间的顺序将会被打乱。
```