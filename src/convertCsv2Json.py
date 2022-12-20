import json
import pandas as pd

def main():
    record = "import/allOther-depositList.csv"
    data = pd.read_csv(record, header=None, on_bad_lines='skip')
    result = {"record": []}
    for i, row in data.iterrows():
        result["record"].append({"address": row[0]})

    json.dump(result,open(f"{record.split('.')[0]}.json",'w',encoding='utf-8'), ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()