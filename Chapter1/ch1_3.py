#urlify: given a string and the true length of string, write a function that replaces the
#" " with "%20"
my_dictionary={" ": "%20"}
def urlify(string,truelength):
	i=0
	outputstring=""
	for x in string:
		if(i<truelength):
			outputstring += my_dictionary.get(x,x)
			i+=1
	return outputstring

print(urlify("how will this work?  ", 20))
