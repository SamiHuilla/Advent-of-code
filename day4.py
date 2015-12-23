import hashlib
input = "yzbqklnj"
answer = 1
hashput = ""
hex = ""

flag = True

while(flag):
	m = hashlib.md5()
	hashput = input+str(answer)
	m.update(hashput.encode())
	hex = m.hexdigest()
	if(hex[0]=='0'and hex[1]=='0'and hex[2]=='0'and hex[3]=='0'and hex[4]=='0' and hex[5]=='0'):
		break
	else:
		answer+=1

print(answer)
print(hashput)
print(hex)