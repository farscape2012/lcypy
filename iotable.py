import csv

def lcy_csv_read(data, file="output.csv", mode="wb"):
    with open(file, mode) as f:
        writer = csv.writer(f)
        writer.writerows(data)
