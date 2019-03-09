import numpy as np

# s = "Chào ngày mới nhé"
# u = s.encode('utf-8')
# d = u.decode('utf-8')
#
# sr = np.array(list(s))
# ur = np.array(list(u))
#
# sr = np.char.encode(sr, 'utf-8')
#
#
# str = str(sr[2])
# print(str)
# print(type(str))
#
# c = bytes(str, encoding='utf-8')
# print(type(c))
# c = c.decode('utf-8')
# print(c)
#
# sr = np.char.decode(sr)
# print(sr)
# print(sr.dtype)

f = open('label.txt', 'r')
str = f.read()
arr = np.array(list(str))
print(arr.shape)