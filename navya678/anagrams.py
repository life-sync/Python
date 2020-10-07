def isAnagram(s1,s2):
    s1,s2 = list(s1.lower()),list(s2.lower())
    s1.sort()
    s2.sort()
    return s1==s2

string1 = input("Enter String 1: ")
string2 = input("Enter String 2: ")
print(isAnagram(string1,string2))
     