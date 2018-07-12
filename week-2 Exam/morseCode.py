
output =[]

def morseCode(w):
	st = ''
	w=w.upper()
	for i in w:
		st=st+dictionary.get(i)


	return st

dictionary ={'A':".-",'B':"-...",'C':"-.-.",'D':"-..",'E':".",'F':"..-.",'G':"--.",'H':"....",'I':"..",'J':".---",'K':"-.-",'L':".-..",'M':"--",'N':"-.",'O':"---",
'P':".--.",'Q':"--.-",'R':".-.",'S':"...",'T': "-",'U':"..-",'V':"...-",'W':".--",'X':"-..-",'Y':"-.--",'Z':"--.."}
     

inputList =  ["a", "z", "g", "m"]

for w in inputList:
	s= morseCode(w)
	output.append(s)
	uniqueArray = []
	for i in output:
		if i not in uniqueArray:
			uniqueArray.append(i)

print(len(uniqueArray))
