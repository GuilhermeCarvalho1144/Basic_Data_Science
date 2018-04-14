#==============================================================================
# THIS CODE IS A BASIC TEMPLETE TO MERGE DATAFRAMES AND APPEND A NEW COLUMN IN PANDAS
# AUTHOR : GUILHERME CARVALHO PEREIRA
# SOURCE: DEEP LEARNING PREREQUISITES: THE NUMPY STACK IN PYTHON...UDEMY COURSE
#==============================================================================
##START
##LIBRARIES
import numpy as np
import pandas as pd
#==============================================================================
#VARIABLES
##ENTER THE FILEs NAMEs
file_name1 = 'table1.csv'       
file_name2 = 'table2.csv'
#LOADING THE FILE...CONFIGURE THE READ FUNCTION SUIT YOUR DATA
df1 = pd.read_csv(file_name1)
df2 = pd.read_csv(file_name2)
#MERGING THE TABLES
new_df = pd.merge(df1,df2,on = 'user_id')
#APPEND A ROW
new_df['Age verification'] = new_df.apply(lambda row: row['age'] >= 21, axis=1)
#PREVIEWING
print new_df