#STATFLOW
#This component provides tools to perform Process Capability Analysis
#Code by Optmze (ayush.devmail@gmail.com)
#Future addition: To choose csv or mysql databases as datasets; choose options to show certain parts
import matplotlib.pyplot as py
import pandas as pd

#Load CSV Dataset
def loadCSVObservation(file):
    global observation # MAIN DATAFRAME
    try:
        observation = pd.read_csv(file)
        obsno = len(observation)
        print("STATFLOW >> {0} records from {1} loaded. ".format(obsno,file))
    except:
        print("STATFLOW >> Error loading {0} (did you provide the correct path?)".format(file))



def ConstantSampling():
    global cno_subgroups 
    global csample_size


def VariableSampling():
    global vno_subgroups
    


# DRIVER/TEST CODE
file = 'dataset/iston.csv'
loadCSVObservation(file)  
