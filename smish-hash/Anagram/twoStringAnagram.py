# WAP to find out if two strings are anagrams
# example keep and peek
# having same letters in rearranged manner

str1 = input("String 1:")
str2 = input("String 2:")
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
