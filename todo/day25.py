


def stateA(p,s):
	if p in s:
		return p-1, 'E'
	else:
		s.add(p)
		return p+1, 'B'

def stateB(p,s):
	if p in s:
		return p+1, 'F'
	else:
		s.add(p)
		return p+1, 'C'

def stateC(p,s):
	if p in s:
		s.remove(p)
		return p+1, 'B'
	else:
		s.add(p)
		return p-1, 'D'

def stateD(p,s):
	if p in s:
		s.remove(p)
		return p-1, 'C'
	else:
		s.add(p)
		return p+1, 'E'

def stateE(p,s):
	if p in s:
		s.remove(p)
		return p+1, 'D'
	else:
		s.add(p)
		return p-1, 'A'

def stateF(p,s):
	if p in s:
		return p+1, 'C'
	else:
		s.add(p)
		return p+1, 'A'

states = {
'A': stateA,
'B': stateB,
'C': stateC,
'D': stateD,
'E': stateE,
'F': stateF
}

def solve(n):
	tape = set()
	c = 0
	s = 'A'
	for i in range(n):
		c,s = states[s](c,tape)
	print len(tape)

solve(12459852)
		
