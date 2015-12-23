#----PART 1--------------------------------------------------------------------------------
def hasVows(string):
	vows = 0
	for char in string:
		if (char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
			vows += 1

	if (vows>=3):
		return True
	else:
		return None

def hasRow(string):
	previous = ''
	for char in string:
		if (char==previous):
			return True
		previous=char
	return None

def noStrings(string):
	return "ab" not in string and "cd" not in string and "pq" not in string and "xy" not in string
#--------------------------------------------------------------------------------------------------
# PART 2

def hasPair(string):
	index = 0
	for index, char in enumerate(string):
		if(string.count(string[index:index+2])>=2):
			return True
		
	return None

nice = 0
string = ""
with open('input5', encoding='utf-8') as input:
    for line in input:
    	string = str(line)
    	#if (hasVows(string) and hasRow(string) and noStrings(string)): #PART 1
    	if (hasPair(string)): 
    		nice += 1

print(nice)