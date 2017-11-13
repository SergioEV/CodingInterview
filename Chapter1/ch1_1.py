#Implement an algorithm to determine if a string has all unique characters. What if you
#cannot use additional data structures?

def isUnique(string):
	if len(string)>128:
		return False
	char_set = [False for x in range(128)]#setup a char set with all the unique characters
	for char in string:#iterate through the string
		val = ord(char)#return the unicode value
		if char_set[val]:#if already in list return false
			return False
		char_set[val]=True#first time encountering it you will set the value to true
	return True
print(isUnique("hi"))
print(isUnique("asdfghjkl"))
