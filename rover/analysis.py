# Importing required external libraries:
import os
import numpy as np
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# Importing required internal libraries:
from extensions import *


# Reading after verifying if any manually uploaded dataset exists:
if find_local_file(("*new_dataset*"), "data/datasets/") == []:
    print(u"[INFO] No dataset detected...")
    print(u"[INFO] Default Iris dataset being loaded...")
    df = sns.load_dataset("iris")
# Else proceeding with uploaded dataset:
else:
    datapath = "data/datasets/new_dataset.csv"
    df = pd.read_csv(datapath)


# Reading Dataset [Only CSV extension considered for now]:
def dataset_preview():
    """
    DESCRIPTION: Generates preview (top-10 records) of input/default dataset.
    """
    return df.head(50)
