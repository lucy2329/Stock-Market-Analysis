import csv

for year in range(1995,2020):	

	with open(str(year)+'bonuses.txt', 'r') as in_file:

		stripped = (line.strip() for line in in_file)
		lines = (line.split(",") for line in stripped if line)
		with open('combinedbonuses.csv', 'a', newline='') as out_file:
			writer = csv.writer(out_file)
			writer.writerows(lines)