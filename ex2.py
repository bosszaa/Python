import os
import re
file = open('d:/student.txt').read().split("\n")
sdict = dict(item.split('=') for item in file)
sdir = ''
for i in sdict.items():
	sdir = r'd:/{}'.format(i[0])
	if not os.path.exists(sdir):
		os.makedirs(sdir)
	file_conf = open(r'{}/work.conf'.format(sdir), 'w')
	file_conf.write('id={}\ngroup={}'.format(i[0], i[1]))
	file_conf.close()


