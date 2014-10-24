import csv
import sys

fieldname = ["Week", "Threadstarter", "Subthreadstarter", "Number of Posts", "Post Density", "Post Duration",
        "In-Degree", "Out-Degree", "Degree", "Authority", "Hub"]

field_dict = {}

for st in fieldname:
    field_dict[st] = []

with open(sys.argv[1], 'rb') as f:
    reader = csv.DictReader(f)
    lines = [x for x in reader]
    for fn in fieldname:
        field_dict[fn].append(max(float(item[fn]) for item in lines))
        field_dict[fn].append(min(float(item[fn]) for item in lines))

with open(sys.argv[1], 'rb') as f, open("normalized_" + sys.argv[1], 'wb') as normalizedcv:
    reader = csv.DictReader(f)
    cwriter = csv.DictWriter(normalizedcv, reader.fieldnames)
    cwriter.writeheader()
    for x in reader:
        for fn in fieldname:
            tmp = (float(x[fn]) - field_dict[fn][1])/(field_dict[fn][0] - field_dict[fn][1])
            x[fn] = str(tmp)
        cwriter.writerow(x)

