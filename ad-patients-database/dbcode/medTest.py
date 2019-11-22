import numpy as np
import random
import re

def getDistribution():

	items = ["MRI", "CT", "urineTest", "petImaging", "clinicalDementiaRating",\
			"MMSE", "modHachinskiScore", "hamDepressRatingScaleScore", "frontalSystemsBehaviorScale", \
			"BMI", "restingPulse", "systolicBloodPressure", "diastolicBloodPressure"]
	
	# attributes in each item
	attributes = {}
	attributes["MRI"] = ["consistent ad", "intervening neurological disease", \
						"cerebral microhemorrhages", "infection", "infarction", \
						"fluid attenuation inversion recovery", "focal lesion", \
						"other abnormality", "normal"]
	attributes["CT"] = ["consistent ad", "intervening neurological disease", \
						"infection", "infarction", \
						"focal lesion", "other abnormality", "normal"]
	attributes["urineTest"] = ["drug abuse", "normal"]
	attributes["petImaging"] = ["amyloid burden with ad", "normal"]
	attributes["clinicalDementiaRating"] = ["0", "0.5", "1", "2", "3"]
	attributes["MMSE"] = ["0-12", "13-20", "21-24", "25-30"]
	attributes["modHachinskiScore"] = ["0-4", "5-18"]
	attributes["hamDepressRatingScaleScore"] = ["0-9", "10-13", "14-17", "18-54"]
	attributes["frontalSystemsBehaviorScale"] = ["14-28", "29-52", "53-70"] # only for apathy - 14 items, 5-pt scale
	attributes["BMI"] = ["10-18.5", "19-25", "26-30", "31-40"]
	attributes["restingPulse"] = ["30-59", "60-80", "81-100"]
	attributes["systolicBloodPressure"] = ["100-119", "120-129", "130-139", "140-179", "180-210"]
	attributes["diastolicBloodPressure"] = ["60-80", "60-80", "80-89", "90-119", "120-180"]
	

	# attribute distributions
	prob_attributes = {}
	
	prob_attributes["MRI"] = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.1]
	prob_attributes["CT"] = [0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.1]
	prob_attributes["urineTest"] = [0.1, 0.9]
	prob_attributes["petImaging"] = [0.6, 0.4]
	prob_attributes["clinicalDementiaRating"] = [0.2, 0.3, 0.3, 0.1, 0.1]

	prob_attributes["MMSE"] = [0.1, 0.2, 0.4, 0.3]
	prob_attributes["modHachinskiScore"] = [0.3, 0.7]
	prob_attributes["hamDepressRatingScaleScore"] = [0.4, 0.4, 0.1, 0.1]
	prob_attributes["frontalSystemsBehaviorScale"] = [0.5, 0.4, 0.1]
	prob_attributes["BMI"] = [0.2, 0.4, 0.3, 0.1]
	prob_attributes["restingPulse"] = [0.3, 0.5, 0.2]
	prob_attributes["systolicBloodPressure"] = [0.2, 0.2, 0.2, 0.2, 0.2]
	prob_attributes["diastolicBloodPressure"] = [0.2, 0.2, 0.2, 0.2, 0.2]
	


	return items, attributes, prob_attributes


def generateData(patients_basics, startId):

	items, attributes, prob_attributes = getDistribution()
	columnNames = items.copy()
	columnNames.insert(0, "patientID")
	columnNames.insert(0, "ID")
	tests = []
	items_to_number = ["MMSE", "modHachinskiScore", "hamDepressRatingScaleScore", \
					"frontalSystemsBehaviorScale", "BMI", "restingPulse", "systolicBloodPressure"]

	# iterate over the data of patients basics
	idx = startId
	for basic in patients_basics:
		test = {}
		idx += 1
		test["patientID"] = str(idx)
		if basic["diagnosis"] == 'Normal':
			
			test["MRI"] = "normal"
			test["CT"] = "normal"
			test["urineTest"] = "normal"
			test["petImaging"] = "normal"
			test["clinicalDementiaRating"] = "0"
			test["MMSE"] = "30"
			test["modHachinskiScore"] = "0"
			test["hamDepressRatingScaleScore"] = "0"
			test["frontalSystemsBehaviorScale"] = "14"

			for it in ["BMI", "restingPulse", "systolicBloodPressure"]:
				choice = random.choices(attributes[it], prob_attributes[it])
				index = attributes[it].index(choice[0])
				lower, upper = re.split(r'-', attributes[it][index])
				if it is "BMI":
					test[it] = str(round(random.choices(np.arange(float(lower), float(upper), 0.2))[0], 1))
				else:
					test[it] = str(random.choices(range(int(lower), int(upper)))[0])
					if it is "systolicBloodPressure":
						lower, upper = re.split(r'-', attributes["diastolicBloodPressure"][index])
						test["diastolicBloodPressure"] = str(random.choices(range(int(lower), int(upper)))[0])
		else:
			for item in items:
				if item is "diastolicBloodPressure":
					continue
				elements = attributes[item]
				probs = prob_attributes[item]
				choice = random.choices(elements, probs)
				test[item] = choice[0]
				index = attributes[item].index(choice[0])
				if item in items_to_number:
					lower, upper = re.split(r'-', attributes[item][index])
					if item is "BMI":
						test[item] = str(round(random.choices(np.arange(float(lower), float(upper), 0.2))[0], 1))
					else:
						test[item] = str(random.choices(range(int(lower), int(upper)))[0])
						if item is "systolicBloodPressure":
							lower, upper = re.split(r'-', attributes["diastolicBloodPressure"][index])
							test["diastolicBloodPressure"] = str(random.choices(range(int(lower), int(upper)))[0])

		tests.append(test)

	return tests



















