from collections import Counter



#Check Permutation: Given two strings check if one is a permutation of the other.
def isPermutation(string1,string2):
	if len(string1)!=len(string2):
		return False
	#char_set = Counter()
	#for i in string1:
	#	char_set[i] += 1
	#for c in string2:
	#	if char_set[c]==0:
	#		return False
	#	char_set[c] -= 1
	#return True
	char_set = [0]*len(string1)
	for a,b in enumerate(string1):
		char_set[a] +=1
	for a,b in enumerate(string2):
		if char_set[a]==0:
			return False
		char_set[a] -= 1
	return True
print(isPermutation("hi","ih"))