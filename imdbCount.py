import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import glob
import gzip
import shutil
import urllib.request
in_suffix = '.tsv.gz'
url = 'https://datasets.imdbws.com/name.basics.tsv.gz'
urllib.request.urlretrieve(url, 'name.basics.tsv.gz')

def unzip_files(files):
    for file in files:
        in_file_name = file + in_suffix
        out_file_name = file.replace('.', '_') + '.tsv'
        print("Unzipping " + in_file_name + " to " + out_file_name + ".")
        with gzip.open(in_file_name, 'rb') as f_in:
            with open(out_file_name, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

files = ['name.basics']
print("")
print("Starting...")
unzip_files(files)        

tsv_files = glob.glob("*.tsv")
for file in tsv_files:
    print(file)
    pickle.dump(pd.read_table(file,sep="\t",low_memory=False, na_values=["\\N","nan"]),
                open(file[:-4]+".sav","wb"))
print('Processing records...');
data=pd.read_csv('name_basics.tsv',sep='\t')
rslt_df = data[(data['deathYear'].str.isdigit()==0) & (data['primaryProfession'].str.startswith('producer'))] 
count = str(len(rslt_df))  
print('\nTotal people that are not dead and have the first of their professions as producer :' + count  )
