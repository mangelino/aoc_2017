
from aoc24 import blocks

def calc_sum(s):
	a = [[int(c) for c in b.split('/')] for b in s.split('-')]
	return sum([sum(c) for c in a])


def attach(b, s, used, p, l):
	l.append(p)
	for i in range(len(b)):
		u = set(used)
		if i in u:
			continue
		e = b[i].split('/')
		if e[0] == s:
			u.add(i)
			attach(b, e[1], u, p+'-'+b[i],l)
		elif e[1] == s:
			u.add(i)
			attach(b, e[0], u, p+'-'+b[i],l)


	return
			
test=[
'0/2',
'2/2',
'2/3',
'3/4',
'3/5',
'0/1',
'10/1',
'9/10'
]			

def solve(b):
	k=0
	l=[]
	for i in range(len(b)):
		used = set()
		e = b[i].split('/')
		if e[0] == '0':
			used.add(i)
			attach(b, e[1], set(used), ''+b[i],l)
		elif e[1] == '0':
			used.add(i)
			attach(b, e[0], set(used), ''+b[i],l)
	return l

l = solve(blocks)
#print l
#print [(calc_sum(r), r) for r in l]
o = 0
br =''
for e in l:
	if calc_sum(e) > o:
		o = calc_sum(e)
		br = e

print o, br
#print max([calc_sum(r) for r in l])

