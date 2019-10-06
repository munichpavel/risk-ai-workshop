import os
from pathlib import Path

datadir = Path(os.environ['DATA_DIR'])


class filenames:
    '''
    Not-exactly-12-factor-app-conform, but still better than hardcoding, solution to 
    accessing local files in a portable way

    Usage example:

    >> from risk_learning.config import filenames
    >> pd.read_csv(filenames.telecom_churn)
    '''
    telcom_churn=datadir.joinpath('WA_Fn-UseC_-Telco-Customer-Churn.csv')
    fake_churn=datadir.joinpath('churn.csv')
    fake_churn_simple=datadir.joinpath('churn_simple.csv')
    
    churn_bn=datadir.joinpath('churn_bn.pickle')