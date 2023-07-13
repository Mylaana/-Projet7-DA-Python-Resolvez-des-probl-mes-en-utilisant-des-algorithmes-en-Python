"""csv file loader"""
import os
import sys
import csv


def get_list_from_csv(file_name, list_length: int, skip_header=True):
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
                           "cost": int(line[1]),
                           "rate": float(line[2].replace("%", "")) / 100,
                           "list_value_at_cost": [0 for i in range(list_length)],
                           "list_combo_at_cost": [[0] for i in range(list_length)]})

    return result
