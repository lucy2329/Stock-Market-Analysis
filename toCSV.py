import csv

with open('nonifty.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('complete.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('name', 'date', 'open', 'high', 'low', 'close', 'volume'))
        writer.writerows(lines)