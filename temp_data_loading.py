#==============================================================================
# THIS CODE IS A BASIC TEMPLETE TO LOADING A FILE IN PANDAS
# AUTHOR : GUILHERME CARVALHO PEREIRA
# SOURCE: DEEP LEARNING PREREQUISITES: THE NUMPY STACK IN PYTHON...UDEMY COURSE
#==============================================================================
##START
##LIBRARIES
import numpy as np
import pandas as pd
#==============================================================================
#VARIABLES
file_name = 'international-airline-passengers.csv'       ##ENTER THE FILE NAME
#LOADING THE FILE...CONFIGURE THE READ FUNCTION SUIT YOUR DATA
df = pd.read_csv(file_name, engine = 'python', skipfooter=3)
#RENAMING THE COLUMMS
df.rename(index = str, columns={"International airline passengers: monthly totals in thousands. Jan 49 ? Dec 60":"Passengers"}, inplace = True)
#PREVIEWING
print df.head(5)
     

