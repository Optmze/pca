import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Loads CSV Dataset
def loadCSVObservation(file):
    global observation # MAIN DATAFRAME
    try:
        observation = pd.read_csv(file)
        obsno = len(observation)
        print("STATFLOW >> {0} records from {1} loaded. ".format(obsno,file))
    except:
        print("STATFLOW >> Error loading {0} (did you provide the correct path?)".format(file))

#------------------------------------RANDOM-SAMPLE-DATA-GENERATOR--------------------------------------------------
#file = 'dataset/failure.csv'
#loadCSVObservation(file)

#samples = [] #dataframe list
#sample_size = 10 # 5 cycle times
#subgroups = 18 # 10 samples
#df_left = observation['FC'].copy() #copy the required dataframe
#droplist = []

#for i in range(0,subgroups):
#    df_chose = df_left.sample(n = 10)
#    for a,row in df_chose.items(): #iterrows for df, items for series
#        droplist.append(a)
#    #print("----SAMPLE {0} ----".format(i+1))
#    #print(df_chose)
#    samples.append(df_chose)
#    df_left = df_left.drop(index=droplist,axis=0)
#    droplist.clear()
#----------------------------------------------------------------------------------------------------------------------

# Consecutive Sample Generator
#file = 'dataset/failure.csv'
#loadCSVObservation(file)
observation = pd.read_csv("dataset\cf.csv")

samples = []
sample_size = 10
subgroups = 18
df_left = observation['FC'].copy()
droplist = []

for i in range(0,subgroups):
    df_chose = df_left.iloc[i*10:i*10+10]
    samples.append(df_chose)
    print(df_chose)

# VARIABLE DATA CHARTS 
# If subgroup size = 1: X-MR or I-MR Chart (basically individual)
# Subgroup size between 2 and 10 : Xbar-R Chart
# Subgroup Size 11 or more: Xbar - S chart
#----------------------------------------------------XBAR-CHARTS-----------------------------------------------------
#Specification Limits, given by user
USL = 2.3
target = 1.5
LSL = 0.1



#https://www.moresteam.com/toolbox/statistical-process-control-spc.cfm

#Histogram and Curve Fitting
df_left.plot(kind='hist',xlim=(min(df_left),max(df_left)),density=True)
sns.kdeplot(df_left,label="Density")
plt.axvline(USL,linestyle="--",color = "red",label="USL")
plt.axvline(LSL,linestyle="--",color="blue",label="LSL")
plt.axvline(target,linestyle="--",color ="green",label="target")

#Xbar-Chart
xbar = []
for j in samples:
     xbar.append(j.mean())
 
xbar_df = pd.DataFrame(xbar,columns=['xbar'])
xbar_df.plot(kind='line',xlim=(0,len(xbar)),y='xbar',style='.-')
plt.title('XBAR')
plt.axhline(USL,linestyle="--",color="red",label="USL")
plt.axhline(LSL,linestyle="--",color="blue",label="LSL")
plt.axhline(target,linestyle="--",color="green",label="target")
plt.show()
plt.close()
print(xbar_df)
    
    
#R-Chart
USL_range = 10
LSL_range = 0
ranges = []
for j in samples:
    ranges.append(max(j)-min(j))
range_df = pd.DataFrame(ranges,columns=['ranges'])
range_df.plot(kind='line',xlim=(0,len(xbar)),y='ranges',style='.-')
plt.title('Ranges')
plt.axhline(USL_range,linestyle="--",color="red",label="USL")
plt.axhline(LSL_range,linestyle="--",color="blue",label="LSL")
plt.show()
plt.close()
print(range_df)

# Calculate Cp and Cpk
Cp = (USL-LSL)/(6*np.std(df_left))    
Cpk = min((USL-df_left.mean())/(3*df_left.std()),(df_left.mean()-LSL)/(3*df_left.std()))
print("Cp:{0}".format(Cp))
print("Cpk:{0}".format(Cpk))

# ATTRIBUTE DATA CHART

#PROCESS-COMPONENT-ANALYSIS


