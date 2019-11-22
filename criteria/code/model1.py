import exrex
import random
import numpy as np


### attributes
attributes = ['age', 'mmse', 'bmi']
min_val = {}
max_val = {}

min_val['age'] = '('+"|".join([str(i) for i in range(18, 60)])+')'
max_val['age'] = '('+"|".join([str(i) for i in range(60, 90)])+')'

min_val['mmse'] = '('+"|".join([str(i) for i in range(10, 17)])+')'
max_val['mmse'] = '('+"|".join([str(i) for i in range(24, 28)])+')'

min_val['bmi'] = ('('+"|".join([str(i) for i in np.arange(10, 18.5, 0.2)])+')').replace('.', '\.')
max_val['bmi'] = ('('+"|".join([str(i) for i in np.arange(30, 40, 0.2)])+')').replace('.', '\.')

### templates
template = {}
for attr in attributes:
	template[attr] = []

for attr in attributes:
	template[attr].append(attr + " is at least " + min_val[attr])
	template[attr].append(attr + " is less than " + max_val[attr])
	template[attr].append(attr + " is between " + min_val[attr] + " and " + max_val[attr])
	template[attr].append("minimum " + attr + " " + min_val[attr] + " " + " , maximum " + attr + " " + max_val[attr])

## patterns
patterns = []
for attr in attributes:
	p = np.random.choice(template[attr])
	patterns.append(exrex.getone(p))

# output
f = open('output.txt', 'w')
for p in patterns:
	f.write(p + "\n")
f.close()



























