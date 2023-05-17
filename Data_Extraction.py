# -*- coding: utf-8 -*-
"""
Created on Tue May 16 10:57:35 2023

@author: Ashish Bahuguna
         epartment of Earthquake Engineering
         IIT Roorkee, Uttarakhand
         email: bahugunaashish92@gmail.com
                abahuguna1@eq.iitr.ac.in
         
"""

import pandas as pd
import numpy as np
import os

#get the list of files in the directory
def get_list_files (filepath):
    dir_list = os.listdir(filepath)
    #print(dir_list)
    return dir_list

# create the path of the each file
def create_path_list (dir_list,filepath):
    file_path_list = []
    i=0
    for fname in dir_list:
        _path =[]
        file_name =fname
       
        #print(file_name,i)
        _path = filepath + file_name
        #print(filepath)
        file_path_list = np.append (file_path_list,_path)
        
        #print(filepath)
        i=i+1
    #print(type (file_name))
   
    return file_path_list
    
#obtain the index of the max value of rlz0 from each file
def get_index(path):
    #pd.read_excel('tmp.xlsx', index_col=None, header=None) 
    df = pd.read_csv(path, skiprows=[0])
    #df = df.rename(columns={'': 'newName1', 'oldName2': 'newName2'})
    #print(df)
    #max_PGA=df[['rlz0']].idxmax() 
    column_name = list(df.columns)
    df = df.rename(columns={column_name[3]: 'rlz'})
    column_name = list(df.columns)
    re_column = column_name[3]
    idmax_PGA= df[re_column].idxmax()
    #print(max_PGA)
    return idmax_PGA, df




path1= 'E:/AshishBahuguna/New folder/output-852-disagg-csv/'
dir_list =  get_list_files (path1)
fname_path = create_path_list (dir_list,path1)

#print(fname_path)

res = pd.DataFrame()
# path = 'E:/AshishBahuguna/New folder/output-852-disagg-csv/Dist-0_287.csv'

for path in fname_path:
    idmax_PGA, df = get_index(path)
    row1=df.iloc[idmax_PGA]#.to_frame('')
    row1=pd.DataFrame(row1)
    row1=row1.T
    print('\n========', path,'====================')
# #print(row1)
    res = pd.concat([res,row1],ignore_index=True)
res["File Name"]= dir_list
print(res)

# path = 'E:/AshishBahuguna/New folder/output-852-disagg-csv/Dist-1_287.csv'
# idmax_PGA, df = get_index(path)
# row1=df.iloc[idmax_PGA]#.to_frame(' ')
# row1=pd.DataFrame(row1)
# row1=row1.T
# # print(row1)
# res = pd.concat([res,row1],)
# #print(res)


# se = pd.Series(mylist)
# df['new_col'] = se.values

