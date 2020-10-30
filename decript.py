# f = open("C:\\Users\\ag16000\\Desktop\\decript\\emails.txt", "r")
# a=f.readlines()
# for i in a:
# with file("C:\\Users\\ag16000\\Desktop\\decript\\emails.txt", "r") as f:
# 	for line in f:
# 		line = line.strip()
#     	if len(line) > 0:
#     		print(chr(ord(i)-5))

filepath = 'C:\\Users\\ag16000\\Desktop\\decript\\emails.txt'
def encripted():
	with open(filepath) as fp:
	   line = fp.readline()
	   cnt = 1
	   while line:
	       print("Line {}: {}".format(cnt, line.strip()))
	       line = fp.readline()
	       cnt += 1

def decripted():
 	with open(filepath) as fp:
	   line = fp.readline()
	   cnt = 1
	   while line:	
	       # print("Line {}: {}".format(cnt, line.strip()))
	       for i in line:
	       	b=chr(ord(i)-5)
	       	print(b,end='')
	        line = fp.readlines()
	       cnt += 1
	   print('\n')

print("-----------------------------")
print("the encripted message is :")
encripted()

print("-----------------------------")
print("the decripted messge is :")
decripted()
print("-----------------------------")