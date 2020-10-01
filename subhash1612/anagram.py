'''
   This program checks if two strings are anagrams of each other.
   An anagram is a word or phrase formed by rearranging the letters of a different word or phrase
'''

def check(str1,str2): #Function to check if they are anagrams
    if(len(str1) != len(str2)): #Comparing the lengths of the two strings
        print("The strings are not anagrams")
    else:
        str1 = str1.lower()
        str2 = str2.lower()
        str1 = sorted(str1) #Sort each string alphabetically
        str2 = sorted(str2)
        if(str1 == str2): #If they are equal then they are anagrams
            print("The strings are anagrams")
        else:
            print("The strings are not anagrams")


def main(): #Driver function
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    check(str1,str2)

main()
