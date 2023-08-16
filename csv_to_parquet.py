import os
from glob import iglob
import pandas as pd


ROOT_DIR="./../**/*"

for f in iglob(ROOT_DIR,recursive=True):
    if f.endswith(".csv") and os.path.isfile(f):

        try:
            df=pd.read_csv(f)

            # save to .parquet
            parquet_filename = os.path.splitext(f)[0] + ".parquet"
            df.to_parquet(parquet_filename)

            # delete the csv file from disk
            os.remove(f)

        except Exception as e:
            
            print(e)
            continue


        