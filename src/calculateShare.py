import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots

def main():
    file1 = 'out/80BAL-20WETH-deposit.csv'
    file2 = 'out/aurabb-a-USD-vault.csv'
    file3 = 'out/auraB-stETH-STABLE-vault.csv'
    poolVal1 =  105063969
    totalToken1 = 7361487.83
    poolVal2 = 119331844
    totalToken2 = 118008001.05
    poolVal3 = 213322763
    totalToken3 = 143140.18
    record1 = pd.read_csv(file1)
    record1['value'] = record1['balance']*poolVal1/totalToken1
    record2 = pd.read_csv(file2)
    record2['value'] = record2['balance']*poolVal2/totalToken2
    record3 = pd.read_csv(file3)
    record3['value'] = record3['balance']*poolVal3/totalToken3

    thr1 = 6862.75
    thr2 = 33333.33
    thr3 = 48275.86

    totalUser1 = len(record1)
    totalUser2 = len(record2)
    totalUser3 = len(record3)

    print(totalUser1, totalUser2, totalUser3)

    record1.loc[record1['value'] > thr1] = np.nan
    record1 = record1.dropna(axis = 0)
    record2.loc[record2['value'] > thr2] = np.nan
    record2 = record2.dropna(axis = 0)
    record3.loc[record3['value'] > thr3] = np.nan
    record3 = record3.dropna(axis = 0)

    acqUser1 = len(record1)
    acqUser2 = len(record2)
    acqUser3 = len(record3)

    print(acqUser1, acqUser2, acqUser3)
    print(sum(record1['value']), sum(record2['value']), sum(record3['value']))

if __name__ == "__main__":
    main()