import numpy as np

print(np)
# <module 'numpy' from '/Users/yeh/Library/Python/3.7/lib/python/site-packages/numpy/__init__.py'>
print(np.__version__)
# 1.20.2

a = np.arange(15)
print(a)
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

a = np.arange(15).reshape(3,5)
print(a)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
# [10 11 12 13 14]]


# Q1 [簡答題] 請問下列兩種將 Array 轉換成 List 的方式有何不同？
print("list(a): ", list(a))
# [array([0, 1, 2, 3, 4]), array([5, 6, 7, 8, 9]), array([10, 11, 12, 13, 14])]

print("tolist(): ", a.tolist())
# [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]


# Q2 請試著在程式中印出以下三個 NdArray 的屬性並且解釋結果？
# （屬性：ndim、shape、size、dtype、itemsize、length、type）
a = np.random.randint(10, size=6)
print(a)    # 陣列
print(a.ndim)   # 有多少維度(屬性)
print(a.shape)  # 各個維度大小
print(a.size)   # 有幾個元素
print(a.dtype)  # 陣列內元素的資料型態
print(a.itemsize)   # 每個元素佔用空間
print(len(a))   # 長度
print(type(a))  # class類型
print(a.data)   # 所存在記憶體位置

b = np.random.randint(10, size=(3,4))
print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(b.dtype)
print(b.itemsize)
print(len(b))
print(type(b))
print(b.data)

c = np.random.randint(10, size=(2,3,2))
print(c)
print(c.ndim)
print(c.shape)
print(c.size)
print(c.dtype)
print(c.itemsize)
print(len(c))
print(type(c))
print(c.data)

# Q3 如何利用 list(...) 實現 a.tolist() 的效果？試著用程式實作。
def tolist(iterable):
    iterable.tolist()

print(a.tolist())
print(b.tolist())
print(c.tolist())


# 延申題
list = np.arange(20)
print(list)
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

list = np.arange(0, 20, 2)
print(list)
# [ 0  2  4  6  8 10 12 14 16 18]

list = np.arange(0, 20, 3)
print(list)
# [ 0  3  6  9 12 15 18]
