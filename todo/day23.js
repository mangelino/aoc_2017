



prog = ['set b 84',
'set c b',
'jnz a 2',
'jnz 1 5',
'mul b 1',
'sub b -1000',
'set c b',
'sub c -170',
'set f 1',
'set d 2',
'set e 2',
'set g d',
'mul g e',
'sub g b',
'jnz g 2',
'set f 0',
'sub e -1',
'set g e',
'sub g b',
'jnz g -8',
'sub d -1',
'set g d',
'sub g b',
'jnz g -13',
'jnz f 2',
'sub h -1',
'set g b',
'sub g c',
'jnz g 2',
'jnz 1 3',
'sub b -17',
'jnz 1 -23']

prog1 = ['set b 84',
'set c b',
'jnz a 2',
'jnz 1 5',
'mul b 100',
'sub b -100000',
'set c b',
'sub c -17000',
'set f 1',
'set d 2',
'set e 2',
'sub d -1',
'set g d',
'sub g b',
'jnz g -4',
'jnz f 2',
'sub h -1',
'set g b',
'sub g c',
'jnz g 2',
'jnz 1 3',
'sub b -17',
'jnz 1 -15'
]

reg = {
'a':1,
'b':0,
'c':0,
'd':0,
'e':0,
'f':0,
'g':0,
'h':0
}

var gr = function(r) {
    if (r>='a' && r<='h') {
		return reg[r]
    } else {
		return parseInt(r)	
	}
}

var sr = function(r, v) {
	reg[r] = v
}
pc = 0

cpu = {
'set': (a,b) => { sr(a,gr(b)) },
'mul': (a,b) => { sr(a, gr(a)*gr(b)) },
'sub': (a,b) => { sr(a, gr(a)-gr(b)) },
'jnz': (a,b) => { if (gr(a) != 0) {
					pc += gr(b)-1
					}
				}
}
var pr = function() {
	out = ''
	for (k in reg) {
		out+=k+':'+reg[k]+' '	
}
	return out
}
var solve = function(p) {
	i = 0
	while (pc>=0 && pc<p.length) {
		instr = p[pc].split(' ')
		cpu[instr[0]](instr[1],instr[2])
		pc += 1
		if (reg['f'] == 1) {
			console.log(pr()+' ['+pc+']')		
		}
		i+=1
	}
	console.log('reg h='+reg['h'])
}

solve(prog)
