import csv

with open('test.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('test.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('name', 'date', 'open', 'high', 'low', 'close', 'volume'))
        writer.writerows(lines)