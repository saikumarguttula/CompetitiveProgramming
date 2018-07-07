
string1 = raw_input("") 
string2 = raw_input("") 

def Anagram(s,t):
    if(len(s)!=len(t)):
        return False

    for i in t:
        count =0
        if i  not in s:
            return False

            
    return True
s1 =string1.replace(" ","").lower()
t1= string2.replace(" ","").lower()
print(Anagram(s1,t1))
