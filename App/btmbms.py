import pandas as pd
import os

file_names = ["Status", "Locations", "Batteries"]
file_columns = [
	["Battery", "SOC", "Date", "Time", "Notes"],
	["Battery", "Location", "Start", "End"],
	["Label", "Acquisition year", "Acquisition month", "Chemistry", "Cycle schedule"]
]


def initialise():
	"""initialise is code to generate the relevant files"""

	try:
		os.makedirs("..//Data")
	except Exception as e:
		print("Folder already made")

	for i in range(0, len(file_names)):
		x = open("..//Data//" + file_names[i] + ".csv", "w")
		temp_columns = file_columns[i]
		x.write(",".join(temp_columns))
		x.close()
	
	print("Initialisation complete")


def import_from_status(file_name):
	"""import_from_status is code to pull content from a Status.csv file"""

	df = pd.read_csv(file_name)
	print(df.columns)

	# building Status.csv
	df.to_csv("..//Data//" + file_names[0] + ".csv", sep=",", index=False)
	# END building Status.csv

	# building Batteries.csv
	df = df.sort_values('Battery')
	unique_batteries = df[file_columns[0][0]].unique()
	print(unique_batteries)

	x = open("..//Data//" + file_names[2] + ".csv", "w")
	temp_columns = file_columns[2]
	x.write(",".join(temp_columns))

	for j in range(0, len(unique_batteries)):

		if j == 0:
			x.write("\n" + unique_batteries[j] + "\n")
		else:
			x.write(unique_batteries[j] + "\n")

	x.close()
	# END building Batteries.csv


def get_latest_statuses(file_name):
	"""get_latest_statuses is code to pull latest status of batteries"""

	df = pd.read_csv(file_name)
	print(df.columns)

	latest_df = df.sort_values('Date').groupby('Battery').tail(1)
	print(latest_df)

	latest_df.to_csv("..//Data//Status_last.csv", sep=",", index=False)

	return latest_df


if __name__ == '__main__':
	initialise()

	# import_from_status("..//Data//Status_example.csv")
