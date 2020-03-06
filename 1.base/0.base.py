# 0. the string

s = "hello"
print (s)
print (s[0])
print (s[-1])
print (s[0:3])
print (len(s))

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
s = f.read('data.txt')
print s
# f.write('hello\n')
f.close()
