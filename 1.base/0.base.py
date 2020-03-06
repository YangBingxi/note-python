# -*-encoding:utf-*-
# 0. the string

s = "hello"
s1 = " world"
print (s)
print s+s1
print s*3
print (s[0])
print (s[-1])
print (s[0:3])
print (len(s))
nums = "0,1,1,2,3,4,5,6,6,4,7,7,6,5,48"
nums_num = nums.split(",")
print nums_num

# 1. the list
a = [1,2.0,'hi',5+1.0]
print (a)
print (a[0])
print (len(a))
# a.append("add")
print (a)
# a.remove(4)
# print a

# 2. the set
s = {2,3,4}
s1 = {2,5,6}
print s
s.add('45')
print s
print s&s1
print s|s1
print s-s1
print s^s1


# 3. the dictionary
d = {'dog':5,'cat':6}
print d["dog"]
d["pig"]=7
print d.keys()
print d.values()


# 4. File IO
f = open('data.txt','w')
# f.write('hello\n')
f.close()

# 5. common data types
"""
类型 	例子
整数 	-100
浮点数 	3.1416
字符串 	'hello'
列表 	[1, 1.2, 'hello']
字典 	{'dogs': 5, 'pigs': 3}
Numpy数组 	array([1, 2, 3])
"""
# others
"""
类型 	例子
长整型 	1000000000000L
布尔型 	True, False
元组 	('ring', 1000)
集合 	{1, 2, 3}
Pandas类型 	DataFrame, Series
自定义 	Object Oriented Classes
"""
# you can use 'type' function to get the type of varibale
# like: 'type(a)'


