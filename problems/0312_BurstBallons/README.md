关于这一题的详细解析参见：

- [https://www.cnblogs.com/grandyang/p/5006441.html](https://www.cnblogs.com/grandyang/p/5006441.html)



用到的是二维 dp，先考虑小区间 `[i, j]` 内的情况，再逐步扩大区间，考虑区间扩大后跟区间扩大前的 dp 关系。





Python 元素插入：

```python
"""
要达到的效果：
    在第0个位置插入一个元素5
"""
a = [1, 2, 3]
a.insert(0, 5)

print(a)

# result: [5, 1, 2, 3]
```

