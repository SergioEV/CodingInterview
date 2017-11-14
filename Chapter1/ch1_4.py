#palindrome permutation: Given a string, write a function to check if its is a permutation 
#of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. 
#A permutation is a rearrangement of letters. The palindrome does not need to be limited
#to just dictionary words.
def isPalindromePermutation(string):
	mymap = [0 for x in range(26)]
	countodd = 0
	for c in string:
		if(ord(c)<=ord('z')):
			x=ord(c)-ord('a')
		else:
			x=ord(c)-ord('A')
		if x>=0 and x<=26:
			mymap[x] += 1
			if mymap[x]%2:
				countodd += 1
			else:
				countodd -= 1
	return countodd <=1

print(isPalindromePermutation("tacos cosat"))