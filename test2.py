import re
r = re.compile('\d.*')
f = open('d:/employee.txt').read()
lst = f.split('\n')
a = 0
ans = []
for x in lst:
	l = r.findall(x)
	ans.append(int(l[0]))
ans = sorted(ans)
ans = list(reversed(ans))
print(ans)
print("Sum :",sum(ans))