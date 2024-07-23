#setting sys.path for importing modules
import os
import sys

if __name__ == "__main__":
         abspath= __file__
         parent_module= "/".join(abspath.split("/")[:-2])
         sys.path.insert(0, parent_module)

import pandas as pd
from scipy.stats import iqr
import numpy as np

def load(expmatfile, expmatsep = "\t", indexcolname="target_id"):
    #expmat_df = pd.read_csv(expmatfile, sep = expmatsep).set_index(indexcolname)
    expmat_df = pd.read_csv(expmatfile, sep = expmatsep, index_col=0)
    return expmat_df

def load_transposed(expmatfile, expmatsep = "\t", indexcolname="accession"):
    """"For expression matrix that is outputed by ken's pipeline where cols = genes and each row correspond to on sample"""
    #expmat_df = pd.read_csv( expmatfile, sep=expmatsep).set_index(indexcolname)
    expmat_df = pd.read_csv(expmatfile, sep = expmatsep, index_col=0)
    expmat_df = expmat_df[~expmat_df.index.duplicated(keep='first')].transpose() #get rid of duplicated sample rows then transpose
    return expmat_df

def subset(expmat_df, samples_to_keep):
     samples_to_drop = set(list(expmat_df.columns)) - set(samples_to_keep)
     samples_to_drop = list(samples_to_drop)
     expmat_df.drop(labels = samples_to_drop, inplace=True, axis = 'columns')
     return expmat_df

def write(expmat_df, path, expmatsep = "\t"):
     expmat_df.to_csv(path , sep = expmatsep)