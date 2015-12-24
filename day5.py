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
			if(index>=2):
				if(string[index]==string[index-1]==string[index-2]):
					return None
			else:
				return True
		
	return None

def hasBurger(string):
	index = 0
	for index, char in enumerate(string):
		if(index>=2):
			if(string[index]==string[index-2]):
				return True
	return None

def is_really_nice(s):
    first = False
    for i in range(len(s) - 3):
        sub = s[i: i + 2]
        if sub in s[i + 2:]:
            first = True
            print("{} is really nice and repeats with {}".format(s, sub))
            break
    if not first:
        return False
    second = False
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            second = True
            break
    return second

nice = 0
string = ""
with open('input5', encoding='utf-8') as input:
    for line in input:
    	string = str(line)
    	#if (hasVows(string) and hasRow(string) and noStrings(string)): #PART 1
    	if (is_really_nice(string)): 
    		nice += 1

print(nice)