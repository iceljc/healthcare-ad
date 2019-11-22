import numpy as np
import random


def getDistribution():

	items = ["speaking", "understand", "ingestOralMed", "resideInNurseFacility", \
				"hasCareGiver", "hasInformant", "isOutpatient", "willingness", "agreeMed", \
				"hasDisability", "medicalCondition", "presenceOfMetal", "isInOtherTrial", "comfortWithNet"]

	# attributes in each item
	attributes = {}
	attributes["speaking"] = ["Bad", "Moderate", "Good"]
	attributes["understand"] = ["Bad", "Moderate", "Good"]
	attributes["ingestOralMed"] = ["No", "Yes"]
	attributes["resideInNurseFacility"] = ["No", "Yes"]
	attributes["hasCareGiver"] = ["No", "Yes but NA", "Yes and available"]
	attributes["hasInformant"] = ["No", "Yes but NA", "Yes and available"]
	attributes["isOutpatient"] = ["No", "Yes"]
	attributes["willingness"] = ["No", "Yes"]
	attributes["agreeMed"] = ["No", "Yes"]
	attributes["hasDisability"] = ["No", "Moderate", "Severe"]
	attributes["medicalCondition"] = ["Bad", "Moderate", "Good"]
	attributes["presenceOfMetal"] = ["No", "Yes"]
	attributes["isInOtherTrial"] = ["No", "Yes"]
	attributes["comfortWithNet"] = ["No", "Yes"]

	# attribute distributions
	prob_attributes = {}
	prob_attributes["speaking"] = [0.1, 0.3, 0.6]
	prob_attributes["understand"] = [0.1, 0.3, 0.6]
	prob_attributes["ingestOralMed"] = [0.1, 0.9]
	prob_attributes["resideInNurseFacility"] = [0.7, 0.3]
	prob_attributes["hasCareGiver"] = [0.6, 0.1, 0.3]
	prob_attributes["hasInformant"] = [0.6, 0.1, 0.3]
	prob_attributes["isOutpatient"] = [0.6, 0.4]
	prob_attributes["willingness"] = [0.1, 0.9]
	prob_attributes["agreeMed"] = [0.1, 0.9]
	prob_attributes["hasDisability"] = [0.6, 0.3, 0.1]
	prob_attributes["medicalCondition"] = [0.1, 0.3, 0.6]
	prob_attributes["presenceOfMetal"] = [0.9, 0.1]
	prob_attributes["isInOtherTrial"] = [0.95, 0.05]
	prob_attributes["comfortWithNet"] = [0.1, 0.9]


	return items, attributes, prob_attributes

def generateData(patients_basics, startId):

	items, attributes, prob_attributes = getDistribution()
	columnNames = items.copy()
	columnNames.insert(0, "patientID")
	columnNames.insert(0, "ID")
	personalInfo = []

	# iterate over the data of patients basics
	idx = startId
	for basic in patients_basics:
		personal = {}
		idx += 1
		personal["patientID"] = str(idx)
		if basic["diagnosis"] == 'Normal':
			personal["speaking"] = "Good"
			personal["understand"] = "Good"
			personal["ingestOralMed"] = "Yes"
			personal["resideInNurseFacility"] = "No"
			personal["hasCareGiver"] = "No"
			personal["hasInformant"] = "No"
			personal["isOutpatient"] = "No"
			personal["willingness"] = "No"
			personal["agreeMed"] = "No"
			personal["hasDisability"] = "No"
			personal["medicalCondition"] = "Good"
			personal["presenceOfMetal"] = "No"
			personal["isInOtherTrial"] = "No"
			personal["comfortWithNet"] = "Yes"
		else:
			for item in items:
				elements = attributes[item]
				probs = prob_attributes[item]
				choice = random.choices(elements, probs)
				personal[item] = choice[0]
		personalInfo.append(personal)

	return personalInfo



# if __name__ == '__main__':
# 	patients_basics = []
# 	print(generateData(patients_basics))








