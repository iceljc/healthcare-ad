import numpy as np
import pandas as pd
import random

def getDistribution():

	total_subjects = 41459.0
	total_normal = 14638.0
	total_notmci = 1739.0
	total_mci = 7213.0
	total_dementia = 17869.0

	diagnosis = ["Normal", "Impaired, not MCI", "MCI", "Dementia"]
	items = ["age", "yearOfEducation", "sex", "race", "hispanic"]
	attributes = {}
	attributes["age"] = ["<65", "65-84", ">=85"]
	attributes["yearOfEducation"] = ["<=12", "13-16", ">=17"]
	attributes["sex"] = ["Male", "Female"]
	attributes["race"] = ["White", "Black or African American", "American Indian or Alaska Native", "Native Hawaiian", 
		"Asian", "Multiracial", "Unknown"]
	attributes["hispanic"] = ["No", "Yes"]

	# compute conditional probability using Bayes formula
	# class distribution
	prob_diagnosis = np.array([total_normal, total_notmci, total_mci, total_dementia]) / total_subjects

	# attribute distributions
	prob_attributes = {}
	prob_attributes["age"] = np.array([6836, 26914, 7709]) / total_subjects
	prob_attributes["yearOfEducation"] = np.array([10919, 16824, 13381]) / total_subjects
	prob_attributes["sex"] = np.array([17750, 23709]) / total_subjects
	prob_attributes["race"] = np.array([32952, 5159, 253, 32, 1036, 1299, 728]) / total_subjects
	prob_attributes["hispanic"] = np.array([37925, 3353]) / total_subjects

	# likelihood: P( attribute | class )
	prob_class_attributes = {}
	prob_class_attributes["age"] = np.array([[0.19, 0.19, 0.13, 0.16], 
											[0.67, 0.68, 0.67, 0.62],
											[0.14, 0.14, 0.2, 0.22]])
	prob_class_attributes["yearOfEducation"] = np.array([[0.17, 0.28, 0.27, 0.33],
														[0.43, 0.40, 0.40, 0.39], 
														[0.39, 0.31, 0.32, 0.27]])
	prob_class_attributes["sex"] = np.array([[0.35, 0.41, 0.47, 0.48], 
											[0.65, 0.59, 0.53, 0.52]])
	prob_class_attributes["race"] = np.array([[0.78, 0.71, 0.76, 0.83],
											[0.14, 0.17, 0.15, 0.10], 
											[84/total_normal, 9/total_notmci, 59/total_mci, 101/total_dementia], 
											[9/total_normal, 3/total_notmci, 5/total_mci, 15/total_dementia], 
											[0.03, 0.03, 0.03, 0.02], 
											[0.03, 0.05, 0.04, 0.03], 
											[0.01, 0.04, 0.02, 0.02]])
	prob_class_attributes["hispanic"] = np.array([[0.93, 0.86, 0.90, 0.92], 
												[0.07, 0.13, 0.10, 0.08]])


	# posterior: P( class | attribute )
	prob_attributes_class = {}

	for attr in items:
		prob_attributes_class[attr] = []
		for i in range(len(attributes[attr])):
			tmp = []
			for j in range(len(diagnosis)):
				posterior = prob_class_attributes[attr][i][j] * prob_diagnosis[j] / prob_attributes[attr][i]
				tmp.append(posterior)
			prob_attributes_class[attr].append(tmp)
		prob_attributes_class[attr] = np.asarray(prob_attributes_class[attr])

	return items, attributes, diagnosis, prob_attributes, prob_diagnosis, prob_class_attributes, prob_attributes_class


def main():

	items, attributes, diagnosis, prob_attributes, prob_diagnosis, prob_class_attributes, posteriers = getDistribution()
	
	columnNames = items.copy()
	columnNames.insert(0, "ID")
	columnNames.append("diagnosis")
	items_to_number = ["age", "yearOfEducation"]
	df = pd.DataFrame(columns=columnNames)
	num = 100
	for i in range(1, num+1):
		patient = {}
		patient["ID"] = i
		log_likelihood = []
		for item in items:
			elements = attributes[item]
			weights = prob_attributes[item]
			choice = random.choices(elements, weights)
			patient[item] = choice[0]
			idx = attributes[item].index(choice[0])
			log_likelihood.append(np.log(prob_class_attributes[item][idx]) - np.log(prob_attributes[item][idx]))
			if item is "age":
				if idx < 1:
					patient[item] = str(random.choices(range(40, 65))[0])
				elif idx == 1:
					patient[item] = str(random.choices(range(65, 85))[0])
				else:
					patient[item] = str(random.choices(range(85, 95))[0])
			elif item is "yearOfEducation":
				if idx < 1:
					patient[item] = str(random.choices(range(5, 13))[0])
				elif idx == 1:
					patient[item] = str(random.choices(range(13, 17))[0])
				else:
					patient[item] = str(random.choices(range(17, 25))[0])


		probs = np.sum(log_likelihood, axis=0)
		logits = []
		for i in range(len(probs)):
			logits.append(probs[i] + np.log(prob_diagnosis[i]))
		patient["diagnosis"] = diagnosis[np.argmax(logits)]

		df = df.append(patient, ignore_index=True)
	
	df.to_csv("genData.csv", encoding='utf-8', index=False)
	# for item in items:
	# 	print("=====================")
	# 	print(df.groupby(item).size() / num)
	# 	print("=====================")

	# print(df.groupby("diagnosis").size() / num)




if __name__ == '__main__':
	main()









