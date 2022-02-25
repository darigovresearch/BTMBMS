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


if __name__ == '__main__':
	initialise()
