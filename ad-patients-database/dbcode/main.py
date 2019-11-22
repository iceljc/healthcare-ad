import mysql.connector
import basics
import personal
import medTest
import medicine
import medHistory

def connectdb():
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="",
	  database="healthcare"
	)
	return mydb

def drop_tables(cursor):
	query = "DROP TABLE IF EXISTS demographics, personal, medtest, medicine, medhistory"
	cursor.execute(query)

	return

def create_basics_table(cursor):
	create_table = "CREATE TABLE IF NOT EXISTS demographics ( \
		id int NOT NULL AUTO_INCREMENT, \
		age VARCHAR(255), \
		yearOfEducation VARCHAR(255),\
		yearOfWork VARCHAR(255), \
		sex VARCHAR(255),\
		race VARCHAR(255), \
		hispanic VARCHAR(255), \
		diagnosis VARCHAR(255), \
		PRIMARY KEY (id) \
		)"
	cursor.execute(create_table)

	return

def create_personal_table(cursor):
	create_table = "CREATE TABLE IF NOT EXISTS personal ( \
		id int NOT NULL AUTO_INCREMENT, \
		patientId int NOT NULL, \
		speaking VARCHAR(255), \
		understand VARCHAR(255), \
		ingestOralMed VARCHAR(255), \
		resideInNurseFacility VARCHAR(255), \
		hasCareGiver VARCHAR(255), \
		hasInformant VARCHAR(255), \
		isOutpatient VARCHAR(255), \
		willingness VARCHAR(255), \
		agreeMed VARCHAR(255), \
		hasDisability VARCHAR(255), \
		medicalCondition VARCHAR(255), \
		presenceOfMetal VARCHAR(255), \
		isInOtherTrial VARCHAR(255), \
		comfortWithNet VARCHAR(255), \
		PRIMARY KEY (id) \
		)"

	cursor.execute(create_table)
	return

def create_medtest_table(cursor):

	create_table = "CREATE TABLE IF NOT EXISTS medtest ( \
		id int NOT NULL AUTO_INCREMENT, \
		patientId int NOT NULL, \
		MRI VARCHAR(255), \
		CT VARCHAR(255), \
		urineTest VARCHAR(255), \
		petImaging VARCHAR(255), \
		clinicalDementiaRating VARCHAR(255), \
		MMSE VARCHAR(255), \
		modHachinskiScore VARCHAR(255), \
		hamDepressRatingScaleScore VARCHAR(255), \
		frontalSystemsBehaviorScale VARCHAR(255), \
		BMI VARCHAR(255), \
		restingPulse VARCHAR(255), \
		systolicBloodPressure VARCHAR(255), \
		diastolicBloodPressure VARCHAR(255), \
		PRIMARY KEY (id) \
		)"

	cursor.execute(create_table)
	return


def create_medicine_table(cursor):

	create_table = "CREATE TABLE IF NOT EXISTS medicine ( \
		id int NOT NULL AUTO_INCREMENT, \
		medname VARCHAR(255), \
		PRIMARY KEY (id) \
		)"

	cursor.execute(create_table)
	return 

def create_medhistory_table(cursor):

	create_table = "CREATE TABLE IF NOT EXISTS medhistory ( \
		id int NOT NULL AUTO_INCREMENT, \
		patientId int NOT NULL, \
		useMedicine VARCHAR(255), \
		useDuration VARCHAR(255), \
		symptom VARCHAR(255), \
		symDuration VARCHAR(255), \
		symCondition VARCHAR(255), \
		coffee VARCHAR(255), \
		smoke VARCHAR(255), \
		alcoholAbuse VARCHAR(255), \
		alcoholDep VARCHAR(255), \
		drugAbuse VARCHAR(255), \
		drugDep VARCHAR(255), \
		PRIMARY KEY (id) \
		)"

	cursor.execute(create_table)
	return




def main():
	print("Connect to database ...")
	mydb = connectdb()
	mycursor = mydb.cursor()

	# drop existing tables
	drop_tables(mycursor)

	################
	numOfData = 10
	################

	print("Create demographics table ...")
	create_basics_table(mycursor)

	query = "SELECT id FROM demographics ORDER BY id DESC LIMIT 0, 1"
	mycursor.execute(query)
	row = mycursor.fetchone()
	if row is not None:
		maxid = row[0]
	else:
		maxid = 0

	print("Generate patients demographics data ...")
	patients_basics = basics.generateData(numOfData)
	basics_data = []
	for item in patients_basics:
		vals = list(item.values())[1:]
		basics_data.append(tuple(vals))


	print("Insert patients basic data ...")
	insert_query1 = "INSERT INTO demographics (age, yearOfEducation, yearOfWork, sex, race, hispanic, diagnosis) VALUES (%s, %s, %s, %s, %s, %s, %s)"

	

	###############
	print("Create demographics table ...")
	create_personal_table(mycursor)

	print("Generate patients personal data ...")
	personalInfo = personal.generateData(patients_basics, maxid)
	personal_data = []
	for item in personalInfo:
		vals = list(item.values())
		personal_data.append(tuple(vals))

	print("Insert patients personal data ...")
	insert_query2 = "INSERT INTO personal (\
			patientId, \
			speaking, \
			understand, \
			ingestOralMed, \
			resideInNurseFacility, \
			hasCareGiver, \
			hasInformant, \
			isOutpatient, \
			willingness, \
			agreeMed, \
			hasDisability, \
			medicalCondition, \
			presenceOfMetal, \
			isInOtherTrial, \
			comfortWithNet) \
			VALUES (%s, %s, %s, %s, %s, %s, %s, \
			%s, %s, %s, %s, %s, %s, %s, %s)"

	###############
	print("Create medical test table ...")
	create_medtest_table(mycursor)

	print("Generate medical test data ...")
	tests = medTest.generateData(patients_basics, maxid)
	medtest_data = []
	for item in tests:
		vals = list(item.values())
		medtest_data.append(tuple(vals))

	print("Insert medical test data ...")
	insert_query3 = "INSERT INTO medtest (\
			patientId, \
			MRI, \
			CT, \
			urineTest, \
			petImaging, \
			clinicalDementiaRating, \
			MMSE, \
			modHachinskiScore, \
			hamDepressRatingScaleScore, \
			frontalSystemsBehaviorScale, \
			BMI, \
			restingPulse, \
			systolicBloodPressure, \
			diastolicBloodPressure) \
			VALUES (%s, %s, %s, %s, %s, %s, \
			%s, %s, %s, %s, %s, %s, %s, %s)"

	###############
	print("Create medicine table ...")
	create_medicine_table(mycursor)

	medicines = medicine.generateData()
	medicine_data = []
	for item in medicines:
		medicine_data.append(tuple([item]))

	print("Insert medicine data ...")
	insert_query4 = "INSERT INTO medicine (\
			medname) \
	VALUES (%s)"

	###############
	print("Create medical history table ...")
	create_medhistory_table(mycursor)

	print("Generate medical history data ...")
	medical_history = medHistory.generateData(patients_basics, tests, maxid)
	medhistory_data = []
	for item in medical_history:
		vals = list(item.values())
		medhistory_data.append(tuple(vals))

	print("Insert medical history data ...")
	insert_query5 = "INSERT INTO medhistory (\
			patientId, \
			useMedicine, \
			useDuration, \
			symptom, \
			symDuration, \
			symCondition, \
			coffee, \
			smoke,  \
			alcoholAbuse, \
			alcoholDep, \
			drugAbuse, \
			drugDep) \
			VALUES (%s, %s, %s, %s, %s, %s, \
			%s, %s, %s, %s, %s, %s)"


	############ execution #############
	mycursor.executemany(insert_query1, basics_data)
	mydb.commit()
	mycursor.executemany(insert_query2, personal_data)
	mydb.commit()
	mycursor.executemany(insert_query3, medtest_data)
	mydb.commit()

	query = "SELECT id FROM medicine ORDER BY id DESC LIMIT 0, 1"
	mycursor.execute(query)
	row = mycursor.fetchone()
	if row is None:
		mycursor.executemany(insert_query4, medicine_data)
		mydb.commit()

	mycursor.executemany(insert_query5, medhistory_data)
	mydb.commit()


if __name__ == '__main__':
	main()








