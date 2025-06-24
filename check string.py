#identify vowel,consonent,uppercase,lowercase,and space
class String:
    def __init__(self,s):
        self.s=s
    def vowel(self):
        v="aeiouAEIOU"
        k=0
        for char in self.s:
            if char in v:
                k=k+1
        print("vowels are:",k)
    def consonent(self):
        v="aeiouAEIOU"
        l=0
        for char in self.s:
            if char in v:
                l=l+1
        print("consonent:",l)
    def uppercase(self):
        p=0
        for char in self.s:
            if char.isupper():
                p=p+1
        print("uppercase are:",p)
    def lowercase(self):
        o=0
        for char in self.s:
            if char.islower():
                o=o+1
        print("lowercases are:",o)
    def spaces(self):
        m=0
        for char in self.s:
            if char==" ":
                m+=1
        print("spaces in your string are:",m)
s=str(input("Enter your string:"))        
p1=String(s)        
p1.vowel()
p1.consonent()
p1.uppercase()
p1.lowercase()
p1.spaces()
print("Thanku for believing on us")