import numpy as np
import random
import re
import medicine

def getDistribution():
	medicines = medicine.generateData()
	num_med = len(medicines)

	items = ["useMedicine", "useDuration", "symptom", "symDuration", "symCondition", \
			"coffee", "smoke", "alcoholAbuse", "alcoholDep", "drugAbuse", "drugDep"]

	# attributes in each item
	attributes = {}
	attributes["useMedicine"] = [str(i) for i in range(1, num_med)]
	attributes["useDuration"] = ["1m", "2m", "6m", "1y", "2y", "3y"] # less than
	attributes["symptom"] = ["head trauma", "peptic ulcer", "arrhythmia", "cancer", \
							"malignant melanoma", "stroke", "epilepsy", \
							"blindness", "deafness", "hepatic", "renal", \
							"seizures", "mental disorder", "schizophrenia", "memory difficulty", \
							"asthma", "diabetes", "hypertension", "coagulopathy", \
							"gastrointestinal", "cerebrovascular", "pulmonary", "autoimmune", \
							"cardiovascular", "other"]
	attributes["symDuration"] = ["1m", "2m", "6m", "1y", "2y", "3y"] # less than
	attributes["symCondition"] = ["mild", "moderate", "severe"]
	attributes["coffee"] = ["0-5", "6-10"] # cups per day
	attributes["smoke"] = ["0-10", "11-20", "21-30"]
	attributes["alcoholAbuse"] = ["No", "Yes"]
	attributes["alcoholDep"] = ["No", "Yes"]
	attributes["drugAbuse"] = ["No", "Yes"]
	attributes["drugDep"] = ["No", "Yes"]

	# attribute distributions
	prob_attributes = {}
	prob_attributes["useMedicine"] = [1.0 / (num_med-1)] * (num_med-1)
	prob_attributes["useDuration"] = [0.2, 0.1, 0.2, 0.1, 0.2, 0.2]
	prob_attributes["symptom"] = [1.0 / len(attributes["symptom"])] * len(attributes["symptom"])
	prob_attributes["symDuration"] = [0.1, 0.2, 0.2, 0.1, 0.2, 0.2]
	prob_attributes["symCondition"] = [0.6, 0.3, 0.1]
	prob_attributes["coffee"] = [0.7, 0.3]
	prob_attributes["smoke"] = [0.7, 0.2, 0.1]
	prob_attributes["alcoholAbuse"] = [0.9, 0.1]
	prob_attributes["alcoholDep"] = [0.9, 0.1]
	prob_attributes["drugAbuse"] = [0.9, 0.1]
	prob_attributes["drugDep"] = [0.9, 0.1]


	return items, attributes, prob_attributes


def generateData(patients_basics, medical_test, startId):

	items, attributes, prob_attributes = getDistribution()
	columnNames = items.copy()
	columnNames.insert(0, "patientID")
	columnNames.insert(0, "ID")
	items_to_number = ["coffee", "smoke"]
	histories = []

	# iterate over the data of patients basics
	idx = startId
	for i in range(len(patients_basics)):
		
		idx += 1
		if patients_basics[i]["diagnosis"] == 'Normal':
			history = {}
			history["patientID"] = str(idx)
			history["useMedicine"] = "38"
			history["useDuration"] = "0"
			history["symptom"] = "none"
			history["symDuration"] = "0"
			history["condition"] = "mild"
			history["coffee"] = str(random.choices(range(0, 10))[0])
			history["smoke"] = str(random.choices(range(0, 30))[0])
			history["alcoholAbuse"] = "No"
			history["alcoholDep"] = "No"
			history["drugAbuse"] = "No"
			history["drugDep"] = "No"
			histories.append(history)
		else:
			possible_num = 3
			num = random.choices(range(1, possible_num+1))[0] # number of symptoms and medicines
			
			attr = ["useMedicine", "useDuration", "symptom", "symDuration"]
			selected = {}
			for it in items:
				selected[it] = []

			# collect selected id for useMedicine and symptom
			for item in attr:
				while len(selected[item]) < num:
					elements = attributes[item]
					choice = random.choices(attributes[item], prob_attributes[item])[0]
					if choice not in selected[item]:
						selected[item].append(choice)

			# collect selected id for the rest of attributes
			for item in items:
				if item not in attr:
					elements = attributes[item]
					probs = prob_attributes[item]
					choice = random.choices(elements, probs)[0]
					index = attributes[item].index(choice)
					if item in items_to_number:
						lower, upper = re.split(r'-', attributes[item][index])
						selected[item].append(str(random.choices(range(int(lower), int(upper)))[0]))
					else:
						selected[item].append(choice)

			for j in range(num):
				history = {}
				history["patientID"] = str(idx)
				for item in items:
					if item in attr:
						history[item] = selected[item][j]
					else:
						history[item] = selected[item][0]

				histories.append(history)
		

	return histories





















