"""csv file loader"""
import os
import sys
import csv


def get_list_from_csv(file_name, skip_header=True):
    """
    gets csv filename to read from /ressource/ folder

    returns:
      -list(dict)
    """
    result = []
    skipped = False
    _path = (os.path.dirname(os.path.abspath(sys.argv[0])) + "/ressources/").replace("\\", "/")
    with open(file=_path + file_name + ".csv", mode="r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            if skip_header and not skipped:
                skipped = True
                continue

            line = line[0].split(";")

            if line[0] == "":
                continue

            result.append({"name": line[0],
                           "index": int(line[0].replace("Action-", "")),
                           "cost": float(line[1]),
                           "profit": float(line[2].replace("%", "")) / 100})

    return result
