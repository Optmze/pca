
#Process Capability Analysis Tool
#Code by: Optmze (ayush.devmail@gmail.com)


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import math


# Load CSV
# Usage:  Loads given CSV file as the dataframe "observation"
# Input:  file (string)
# Output: records load message / error messages

def loadCSVObservation(file):
    global observation # MAIN DATAFRAME
    try:
        observation = pd.read_csv(file)
        obsno = len(observation)
        print("STATFLOW >> {0} records from {1} loaded. ".format(obsno,file))
    except:
        print("STATFLOW >> Error loading {0} (did you provide the correct path?)".format(file))


# SAMPLE GENERATION
# Two kinds: Random Sample Generator and Consecutive Sample Generator (for time series)


#Random Sample Generator
# Usage:  Generates random samples from given dataset
# Input:  sample_size,subgroups,label
# Output: list of random samples

def randomGenerator(sample_size,subgroups,label):
    samples = []
    df_left = observation[label].copy() #copy the required dataframe
    droplist = []
    for i in range(0,subgroups):
        df_chose = df_left.sample(n = sample_size)
        for a,row in df_chose.items(): #iterrows for df, items for series
            droplist.append(a)
        samples.append(df_chose)
        df_left = df_left.drop(index=droplist,axis=0)
        droplist.clear()
    return samples


# Consecutive Sample Generator
# Usage:  Gives consecutive samples from given dataset
# Input:  sample_size,subgroups,label
# Output: list of generated samples

def consecutiveGenerator(sample_size,subgroups,label):
    global df_left
    samples = []
    df_left = observation[label].copy()
    for i in range(0,subgroups):
        df_chose = df_left.iloc[i*sample_size:i*sample_size+sample_size]
        samples.append(df_chose)
        #print(df_chose)
    return samples


# CONSTANT RETRIEVAL 
# Retrieves constants c(n) and d(n) for unbiased estimates 


#C(n)
# Usage: Estimation of sigma
# Input: Size of sample
# Output: Constant value

def c(n):
    return (math.gamma(n/2) / math.gamma((n-1)/2))*(math.sqrt(2/(n-1)))



# D(n)
# Usage: Estimation of Range; has values for n=2 to n=10 
# Input: Sample Size
# Output: Constant value

def D(n):
    D3 = [0,0,0,0,0.076,0.136,0.184,0.223]
    D4 = [3.267,2.574,2.82,2.114,2.004,1.924,1.864,1.816,1.777]
    if (n==1):
        return 0
    elif(n>10):
        print("Error values beyond n=10 are not supported!")
        return 0
    else:
        return D3[n-2],D4[n-2]


#VARIABLE CHART GENERATION (Xbar,R,S,X,mR,Histogram)
# If subgroup = 1: X-MR Chart
# If subgroup between 2 and 10 : X'-R Chart
# If subgroup size >= 11 : X'-S Chart



# Xbar Chart Generator
# Usage: Generate xbar chart; monitor mean change over time
# Input: sample_list
# Output: Xbar chart output

def genXbar(sample_list,sample_size):
    n = len(sample_list)
    xbar = []
    sd_sum = 0
    xbar_sum = 0
    for i in sample_list:
        mn = i.mean()
        xbar.append(mn)
        xbar_sum = xbar_sum + mn
  
    for j in sample_list:
        sd = j.std()
        print(sd)
        sd_sum = sd_sum + sd

    xbar_bar = xbar_sum / n
    sigma_bar = sd_sum / n

    # Prints X'' and S'
    print("xbar:{0}".format(xbar_bar))
    print("sigma_bar:{0}".format(sigma_bar))
    print("c(n):{0}".format(c(sample_size)))

    # Factor c(n)
    a = 3 / (c(sample_size)*math.sqrt(sample_size))
     
    # Control Limits
    UCL = xbar_bar + (a*sigma_bar)
    LCL = xbar_bar - (a*sigma_bar)
    center = xbar_bar
    print("UCL: {0}".format(UCL))
    print("Center: {0}".format(center))
    print("LCL: {0}".format(LCL))

    # Plot
    xbar_df = pd.DataFrame(xbar,columns=['xbar'])
    xbar_df.plot(kind='line',xlim=(0,len(xbar)),y='xbar',style='.-')
    plt.title('XBAR Chart')
    plt.axhline(UCL,linestyle="--",color="red",label="USL")
    plt.axhline(LCL,linestyle="--",color="blue",label="LSL")
    plt.axhline(center,linestyle="--",color="green",label="target")
    #print(xbar_df)
    plt.show()
    plt.close()


# R Chart Generator
# Usage: Generates range chart (sample size n=2 to n=10)
# Input: sample_list and sample_size
# Output: R chart output
 
def genR(sample_list,sample_size):
    ranges = []
    range_sum = 0
    for i in sample_list:
        rng = max(i) - min(i)
        ranges.append(rng)
        range_sum = range_sum + rng

    range_bar = range_sum / len(ranges)
    D0,D1 = D(sample_size) 
    print("D0:{0}".format(D0))
    print("D1:{0}".format(D1))

    UCL = D1 * range_bar
    center = range_bar
    LCL = D0 * range_bar



    print("center:{0}".format(center))
    ranges_df = pd.DataFrame(ranges,columns=['ranges'])
    ranges_df.plot(kind='line',xlim=(0,len(ranges)),y='ranges',style='.-')
    plt.title('R Chart')
    plt.axhline(UCL,linestyle="--",color="red",label="USL")
    plt.axhline(LCL,linestyle="--",color="blue",label="LSL")
    plt.axhline(center,linestyle="--",color="green",label="target")
    plt.show()



# I-mR Chart Generator (Moving Range Chart)
# Usage: Generates moving range chart;
# mR monitors the absolute difference b/w each measurement to prev measurement
# I monitors shifts in the process
# Input: label,subgroups
# Output: I and MR chart for given data

def genMR(label,subgroups):
    mr = 0
    mrlist = []
    for i in range(0,len(df_left)-1):
       diff = abs(df_left[i] - df_left[i+1])
       mr = mr + diff
       mrlist.append(diff)
    mr_bar = mr / (subgroups - 1)
    print(mr_bar)
    # Here n = 2 (as avg of two consecutive points); D3=0 and D4=3.27
    D3 = 0
    D4 = 3.27
    mr_UCL = mr_bar * D4
    mr_center = mr_bar
    mr_LCL = mr_bar * D3
    
    # MR-Plot
    mr_df = pd.DataFrame(mrlist,columns=['mr'])
    mr_df.plot(kind='line',xlim=(0,len(mrlist)),y='mr',style='.-')
    plt.title('MR CHART')
    plt.axhline(mr_UCL,linestyle="--",color="red",label="USL")
    plt.axhline(mr_LCL,linestyle="--",color="blue",label="LSL")
    plt.axhline(mr_center,linestyle="--",color="green",label="target")
    plt.show()

    # X Chart 
    xbar = df_left.mean()
    df_x = observation[label].copy()
    E2 = 2.66
    x_UCL = xbar + (E2*mr_bar)
    x_center = xbar
    x_LCL = xbar - (E2*mr_bar)
    df_x.plot(kind='line',xlim=(0,len(df_x)),style='.-')
    plt.axhline(x_UCL,linestyle="--",color="red",label="USL")
    plt.title("X chart")
    plt.axhline(x_LCL,linestyle="--",color="blue",label="LSL")
    plt.axhline(x_center,linestyle="--",color="green",label="target")
    plt.show()



# Histogram Generation and Estimation
# Usage: Generates histogram and an estimate (within and overall)
# Input: usl (Upper Specification Limit), lsl (Lower Specification Limit), tgt (Target)
# Output: Output histogram chart

def histogram(usl,lsl,tgt):
    df_left.plot(kind='hist',xlim=(min(df_left),max(df_left)),density=True,color='green')
    sns.kdeplot(observation,label='Density')
    plt.axvline(usl,linestyle="--",color = "red",label="USL")
    plt.axvline(lsl,linestyle="--",color="blue",label="LSL")
    plt.axvline(tgt,linestyle="--",color ="yellow",label="target")
    plt.show()



#mS Chart Distribution
# Usage: S-chart; usually for larger subgroup sizes
# Input: sample_list (the list of samples), sample_size(the size of each sample)
# Output: S-chart for given data

def genS(sample_list,sample_size):
    sd = []
    sd_sum = 0
    for i in sample_list:
        s = i.std()
        sd_sum = sd_sum + s
        sd.append(s)
    sd_bar = sd_sum / len(sd)
    print(sd_bar)
    LCL = sd_bar - ((3*sd_bar) / (c(sample_size)*math.sqrt(2*(sample_size-1))))
    center = sd_bar
    UCL = sd_bar + ((3*sd_bar) / (c(sample_size)*math.sqrt(2*(sample_size-1))))
    if(LCL < 0 ):
        LCL = 0

    # S-Plot
    mr_df = pd.DataFrame(sd,columns=['mr'])
    mr_df.plot(kind='line',xlim=(0,len(sd)),y='mr',style='.-')
    plt.title('S CHART')
    plt.axhline(UCL,linestyle="--",color="red",label="USL")
    plt.axhline(LCL,linestyle="--",color="blue",label="LSL")
    plt.axhline(center,linestyle="--",color="green",label="target")
    plt.show()
    


# ATTRIBUTE CHART GENERATION (p,np,c,u)



# P Chart
# Usage: Build the p chart; if n =100 and say 22 defective items (np) so p = np/n = 0.22
# Input: p (proportion label),np (label), sample (size label) [csv must have p,np,sample]
# Output: p-chart for given data

def genP(p,np,sample_size):
    df_p = observation[p].copy()
    df_np = observation[np].copy()
    k = len(df_p)
    n = sample_size * k
    np = 0
    
    for j in df_np:
        np = np + j
    p_bar = np / n # center
    n_bar = n / k 

    # Control Limits
    UCL = p_bar + (3*math.sqrt((p_bar*(1-p_bar))/n_bar))
    LCL = p_bar - (3*math.sqrt((p_bar*(1-p_bar))/n_bar))
    center = p_bar
    print("p: {0}".format(p_bar))
    print("UCL: {0}".format(UCL))
    print("LCL: {0}".format(LCL))

    #p-plot
    df_p.plot(kind='line',xlim=(0,len(df_p)),y='p',style='.-')
    plt.title("p Chart")
    plt.axhline(UCL,linestyle="--",color="red",label="USL")
    plt.axhline(LCL,linestyle="--",color="blue",label="LSL")
    plt.axhline(center,linestyle="--",color="green",label="target")
    plt.show()


# NP Chart
# Usage: np chart, subgroup size(n) is constant; k = no of subgroups
# Input: np (label for np), n (total subroup size 50)
# Output: np chart of given data

def genNP(np,n):
    np_df = observation[np].copy()
    k = len(np_df)
    np = 0
    for i in np_df:
        np = np + i
    np_bar = np / k
    
    # control limits 
    UCL = np_bar + (3*math.sqrt(np_bar*(1-(np_bar/n))))
    center = np_bar
    LCL = np_bar - (3*math.sqrt(np_bar*(1-(np_bar/n))))
    print(UCL)
    print(center)
    print(LCL)
    #p-plot
    np_df.plot(kind='line',xlim=(0,len(np_df)),y='p',style='.-')
    plt.title("np Chart")
    plt.axhline(UCL,linestyle="--",color="red",label="USL")
    plt.axhline(LCL,linestyle="--",color="blue",label="LSL")
    plt.axhline(center,linestyle="--",color="green",label="target")
    plt.show()

# u,c charts use poisson to model the results
# conditions:
# discrete counts, well-defined time/space occurence, counts should be rare in comparison to opportunityy, independent counts


# C Chart
# Usage: generate c chart; if area of opportunity(inspection unit) does not change from subgroup to subgroup
# Input: c(no of defects in each subgroup); k = total no of subgroups
# Output: c - chart of given data

def gencc(c,k):
    df_c = observation[c].copy() # no of defects in each subgroup
    c_sum = 0
    for i in df_c:
        c_sum = c_sum + i
    c_bar = c_sum / k
    
    cvals = observation[c].values.tolist()
    #control chart
    UCL = c_bar + (3*math.sqrt(c_bar))
    LCL = c_bar - (3*math.sqrt(c_bar))

    plt.plot(cvals,".-")
    plt.axhline(UCL,linestyle="--",color="red",label="USL")
    plt.axhline(LCL,linestyle="--",color="blue",label="LSL")
    plt.title("C Chart")
    plt.show()



# U Chart
# Usage: Generate u chart; if area of opportunity changes ( c = no of infections; n = no of units); in some caes it's k ; u = c/k where k is subgroup size
# Input: c = no of defects in each unit; n = no of units (since variable size)
# Output: u chart of given data
# note: the subgroup size is not constant it varies

def genU(c,n):
    sample = observation.copy()
    sample['u'] = sample[c].div(sample[n]) # u chart values
    c_df = sample[c].copy()
    n_df = sample[n].copy()
    c_sum = 0
    n_sum = 0
    for i in c_df:
        c_sum = c_sum + i
    for i in n_df:
        n_sum = n_sum + i
    ubar = c_sum / n_sum # means avg of ubar happening per n 

    # Control Limits
    UCL = []
    LCL = []
    for i in n_df:
        ul = ubar + 3*math.sqrt((ubar/i))
        ll = ubar - 3*math.sqrt((ubar/i)) # below 0 values of LCL shouldn't matter
        UCL.append(ul)
        LCL.append(ll)
    uvals = sample["u"].values.tolist()
    print(uvals)
    print(UCL)
    print(LCL)

    plt.plot(UCL,".-")
    plt.plot(LCL,".-")
    plt.plot(uvals,".-")
    plt.title("U Chart")
    plt.show()


# Capability Indices Calculation
def calcCI(LSL,USL,sample_list,sample_size):
    n = len(sample_list)
    # Calculation xbar_bar
    xbar = []
    sd_sum = 0
    xbar_sum = 0
    for i in sample_list:
        mn = i.mean()
        xbar.append(mn)
        xbar_sum = xbar_sum + mn

    for j in sample_list:
        sd = j.std()
        sd_sum = sd_sum + sd

    xbar_bar = xbar_sum / n
    sigma_bar = sd_sum / n
    
    # Sigma estimate using sigma_bar and c(n)
    sigma_estimate = sigma_bar / c(sample_size)
    print("Sigma Estimate: {0}".format(sigma_estimate))

    # Calculation: Cp and Cpk
    Cp = (USL-LSL)/(6*sigma_estimate)
    val1 = ((USL-xbar_bar)/(3*sigma_estimate))
    val2 = ((xbar_bar-LSL)/(3*sigma_estimate))
    #Cpk = min(((USL-xbar_bar)/(3*sigma_estimate)),((xbar_bar-LSL)/(3*sigma_estimate)))

    # Calculation: Pp and Ppk, use pooled sd
    Pp = (USL-LSL)/(6*observation.std().values)
    val3 = ((USL-xbar_bar)/(3*observation.std().values))
    val4 = ((xbar_bar-LSL)/(3*observation.std().values))
    

    print("Cp: {0}".format(Cp))
    print("Cpk: {0}".format(min(val1,val2)))
    print("Pp: {0}".format(Pp))
    print("Ppk: {0}".format(min(val3,val4)))




#DRIVER CODE 
#Driver code to showcase how the functions work

filename = "dataset\\lengths.csv" # always add \\ for file name 
loadCSVObservation(file=filename)
sample_list = consecutiveGenerator(5,20,"X")
m=1
#for i in sample_list:
#    print("Group {0}".format(m))
#    print(i)
#    m = m + 1
#   print("--------")
genXbar(sample_list,5)
#runX("FC")
#print(c(8))
#genR(sample_list,5)
#print(d(10))
histogram(1.9,2,2.1)
#genMR("X",20)
#genS(sample_list,5)
#histogram(2.1,1.85,2)
#genP("p","np",100)
#genNP("np",50)
#genU("no_infection","no_units")
#gencc("c",20)
calcCI(1.6,2.3,sample_list,5)




