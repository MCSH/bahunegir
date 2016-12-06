from random import Random
import time
data = []

with open('excuse.txt','r') as f:
	data = f.readlines()

def gen(eid=None):
	r = Random()
	if eid:
		r.seed(eid)
	else:
		r.seed(time.time())
	ans = data[r.randrange(len(data))]
	return ans
