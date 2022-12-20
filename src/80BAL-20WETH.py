import csv
import pandas as pd

def captureDepositList():
    file = 'import/80BAL-20WETH.csv'
    input = pd.read_csv(file)
    deposit = input[input.Method == 'Deposit']
    depositList = list(set(deposit.From))
    with open('import/80BAL-20WETH-depositList.csv', 'w') as f:
        write = csv.writer(f, delimiter='\n')
        write.writerow(depositList)

def main():
    captureDepositList()

if __name__ == "__main__":
    main()