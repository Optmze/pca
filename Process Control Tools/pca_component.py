#STATFLOW
#This component provides tools to perform Process Capability Analysis
#Code by Optmze (ayush.devmail@gmail.com)
#Future addition: To choose csv or mysql databases as datasets; choose options to show certain parts

#-------------------------------------------IMPORTS----------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#----------------------------------------LOAD-DATA-SET-------------------------------------------------------------
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

#---------------------------------------------CONSECUTIVE-SAMPLE-DATA-GENERATOR--------------------------------------
file = 'dataset/failure.csv'
loadCSVObservation(file)
samples = []
sample_size = 10
subgroups = 18
df_left = observation['FC'].copy()
droplist = []

for i in range(0,subgroups):
    df_chose = df_left.iloc[i*10:i*10+10]
    samples.append(df_chose)
    print(df_chose)
#----------------------------------------------------XBAR-CHARTS-----------------------------------------------------
#user-inputed driven
USL = 2.3
target = 1.5
LSL = 0.1

#fractional defect based/formula based
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

    
#PROCESS-COMPONENT-ANALYSIS
#Attribute Data Analysis

#Variable Data Analysis




