class check_anagram:
    def __init__(self,s1,s2):
        self.s1=s1
        self.s2=s2
    def check(self): 
        # the sorted strings are checked  
        if(sorted(self.s1)== sorted(self.s2)): 
            print("The strings are anagrams.")  
        else: 
            print("The strings aren't anagrams.")          
if __name__=='__main__':
    # driver code   
    s1 =input("Enter the first string")
    s2 =input("Enter the first string")
    c_anangram=check_anagram(s1,s2)
    c_anangram.check()
