from random import Random
import time
import re
reg = re.compile(r'%([^%]+)%')
data = []
misc = {}
r = Random()
r.seed(time.time())

with open('excuse.txt','r') as f:
	state = ''
	for line in f.readlines():
		if state == '':
			if line[0] == '%':
				tag = line[1:-1]
				if tag in misc:
					pass
				else:
					misc.update({tag:[]})
				state = tag
				continue
			data.append(line[:-1])
		else:
			misc.get(state).append(line[:-1])

def replace(a):
	tag = a.group(1)
	if tag in misc:
		d = misc.get(tag)
		return d[r.randrange(len(d))]
	return '%'+ tag +'%'


def gen(eid=None):
	if eid:
		r.seed(eid)
	ans = data[r.randrange(len(data))]
	ans = reg.sub(replace,ans)
	return ans

if __name__ == '__main__':
	print(gen())
