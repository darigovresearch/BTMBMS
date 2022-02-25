import pandas as pd


file_names = ["Status", "Locations", "Batteries"]
file_columns = [
	["Battery", "SOC", "Date", "Time", "Notes"],
	["Battery", "Location", "Start", "End"],
	["Label"]
]


def initialise():
	"""initialise is code to generate the relevant files"""

	for i in range(0, len(file_names)):
		x = open("Data//"+ file_names[i] + ".csv", "w")
		temp_columns = file_columns[i]
		x.write(",".join(temp_columns))
		x.close()
	
	print("Initialisation complete")


def import_from_status(file_name):
	"""import_from_status is code to pull content from a Status.csv file"""

	df = pd.read_csv(file_name)
	print(df.columns)
	unique_batteries = df[file_columns[0][0]].unique()
	print(unique_batteries)

	x = open("Data//"+ file_names[2] + ".csv", "w")
	temp_columns = file_columns[2]
	x.write(",".join(temp_columns))

	for j in range(0, len(unique_batteries)):

		if j == 0:
			x.write("\n" + unique_batteries[j] + "\n")
		else:
			x.write(unique_batteries[j] + "\n")


	x.close()


if __name__ == '__main__':
	initialise()

	# import_from_status("Data//Status_example.csv")