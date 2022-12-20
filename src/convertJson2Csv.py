import csv
import json
import pandas as pd

def main():
    record = "out/aurabb-a-USD-vault.json"
    f = open(record)
    data = json.load(f)
    output = [['address', 'balance']]
    maxBatch = 0

    for i, item in enumerate(data["balancesList"]):
        storage = [item["address"], item["totalBalance"]]
        output.append(storage)

    with open("out/aurabb-a-USD-vault.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(output)

if __name__ == "__main__":
    main()