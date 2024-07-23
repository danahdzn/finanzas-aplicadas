# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 13:25:07 2023

@author: Meva
"""

# import libraries and functions
import numpy as np
import pandas as pd

# compare 2 dataframes and give a note based on how good the comparison is
def compare_dataframes(df_teacher, df_student):
    print('---')
    print(' Comparing dataframes df_teacher vs df_student')
    print('---')
    correct_entries = 0
    if not df_teacher.shape == df_student.shape:
        print('df_teacher.shape =/= df_student.shape : ' +\
              str(df_teacher.shape) + ' =/= ' + str(df_student.shape))
        return 0.0
    columns = df_teacher.columns
    for col_name in columns:
        for n in range(df_teacher.shape[0]):
            x = df_teacher.loc[n,col_name]
            y = df_student.loc[n,col_name]
            comp = compare_entries(x, y)
            correct_entries += comp
            if comp == 0:
                print('df_teacher.loc[' + str(n) + ', ' + col_name + '] = ' + str(x) +\
                      ' | df_student.loc[' + str(n) + ', ' + col_name + '] = ' + str(y) +\
                      ' | compare_entries = ' + str(comp))
    note = 10. * float(correct_entries) / (df_teacher.shape[0] * df_teacher.shape[1])
    print('Note = ' + str(note))
    return note
   
     
# compare 2 entries based on their type
def compare_entries(x, y):
    check = int(0)
    if isinstance(x, str):
        y = str(y)
        if x == y:
            check = int(1)
    elif isinstance(x, np.bool_):
        y = bool(y)
        if x == y:
            check = int(1)    
    elif isinstance(x, int) or isinstance(x, np.int32) or isinstance(x, np.int64):
        x = int(x)
        y = int(y)
        if x == y:
            check = int(1)
    elif isinstance(x, float):
        str_format = '.3f'
        x = format(x, str_format)
        y = format(y, str_format)
        if x == y:
            check = int(1)
    elif x is None and x == y:
         check = int(1)
    elif str(x) == 'nan' and str(y) == 'nan': 
         check = int(1)
    return check

   
