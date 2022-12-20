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

    q75,q25 = np.percentile(record1.loc[:,'value'],[75,25])
    intr_qr = q75-q25
    max = q75+(1.5*intr_qr)
    record1.loc[record1['value'] > max] = np.nan
    record1 = record1.dropna(axis = 0)
    record1['category'] = '80BAL-20WETH'

    q75,q25 = np.percentile(record2.loc[:,'value'],[75,25])
    intr_qr = q75-q25
    max = q75+(1.5*intr_qr)
    record2.loc[record2['value'] > max] = np.nan
    record2 = record2.dropna(axis = 0)
    record2['category'] = 'aurabb-a-USD'

    q75,q25 = np.percentile(record3.loc[:,'value'],[75,25])
    intr_qr = q75-q25
    max = q75+(1.5*intr_qr)
    record3.loc[record3['value'] > max] = np.nan
    record3 = record3.dropna(axis = 0)
    record3['category'] = 'auraB-stETH-STABLE'

    fig = px.box(record3, y="value", points="all", title='auraB-stETH-STABLE(Outliers Removal)')

    fig.show()

if __name__ == "__main__":
    main()