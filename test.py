f = open('d:/testpy.txt','w')
f.write("AB\n")
f.write("ZD\n")
f.write("GH\n")
f.close()
f = open('d:/testpy.txt')
for line in f:
	print(line,end='')
f.close()
f = open('d:/testpy.txt')
y=[]
lst=[]
for line in f:
	lst += list(line.strip())
f.close()
lst.sort()
f = open('d:/test_out.txt', 'w')
for line in lst:
	f.write("{0}".format(line))
print(lst)