str1 = input("word 1:")
str2 = input("word 2:")
a = []
b = []
a[:0] = str1
b[:0] = str2
a.sort()
b.sort()
if a==b:
    print("%s and %s are anagrams" %(str1, str2))
else:
    print("%s and %s are not anagrams" %(str1, str2))
