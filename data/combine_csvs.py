all_csv = [
    'amazon.csv',
    'australia.csv',
    'indonesia.csv'
]

import csv, os


# Compile CSVs into single CSV
with open("fire_archives.csv", "w") as csv_file:
    fileWriter = csv.writer(csv_file)
    for place in all_csv:
        file_to_load = os.path.join(place)
        with open(file_to_load, "r") as fire_data:
            fileReader = csv.reader(fire_data, delimiter = ",")
            # Skip Headers
            next(fileReader)
            for row in fileReader:
                fileWriter.writerow(row)