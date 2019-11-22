import exrex
import random
import numpy as np



time_units = ["week(s| )", "month", "year(s| )"]
time_units = "(" + "|".join(time_units) + ")"

t = "[1-9]"

pp1 = "(within|at least|less than)"
pp2 = "(before|prior to)"
symptoms = ["head trauma", "peptic ulcer", "arrhythmia", "cancer", \
					"malignant melanoma", "stroke", "epilepsy", \
					"blindness", "deafness", "hepatic", "renal", \
					"seizures", "mental disorder", "schizophrenia", "memory difficulty", \
					"asthma", "diabetes", "hypertension", "coagulopathy", \
					"gastrointestinal", "cerebrovascular", "pulmonary", "autoimmune", \
					"cardiovascular"]

symptoms = "(" + "|".join(symptoms) + ")"

medications = ["galantamine", "rivastigmine", "donepezil", "tacrine", "analgesics", \
				"sinemet", "amantadine", "bromocriptine", "pergolide", \
				"selegiline", "estrogen", "vitaminE", "memantine", \
				"antidepressant", "ginkgo biloba", "insulin", "betablockers", \
				"narcotics", "methyldopa", "clonidine", "antiparkinsonian", \
				"bromocriptine", "neuroleptics", "benzodiazepines", "barbituates", \
				"anxiolytics", "sedative hypnotics", "corticosteroids", "anticonvulsants", \
				"phenytoin", "phenobarbital", "carbamazepine", "warfarin", "vitamin", \
				"anticoagulant", "cholinesterase inhibitor"]

medications = "(" + "|".join(medications) + ")"

events1 = ["use of " + medications, "history of " + symptoms]
events2 = ["screening", "first first dose of study medication"]
events3 = ["eduction", "work history"]

events1 = "(" + "|".join(events1) + ")"
events2 = "(" + "|".join(events2) + ")"
events3 = "(" + "|".join(events3) + ")"

output = []
templates = []

templates.append(events1 + " " + pp1 + " " + t + " " + time_units)
templates.append(events1 + " " + pp1 + " " + t + " " + time_units + " " + pp2 + " " + events2)
templates.append("(\d|\d{2})" + " years of " + events3)

patterns = []
for _ in range(3):
	p = np.random.choice(templates)
	patterns.append(exrex.getone(p))

# output
f = open('output2.txt', 'w')
for p in patterns:
	f.write(p + "\n")
f.close()









