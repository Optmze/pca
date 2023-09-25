# project_pca
pca is a single file script which implements Shewhart charts to aid with Process Control Analysis.<br>
**Process Control Tools** > **pca.py** (The implementation) <br>
**dataset** (sample datasets) <br>

## Implementation Details
These are the following components in pca.py:
### <ins> **Loading a dataset** </ins>
```
filename = "dataset\\lengths.csv" # always add \\ for file name
```
### <ins>**A. Sampling**</ins>
Sampling the given CSV Dataset to preferred **sample size** and **subgroup count**. It has two main methods of sampling:<br>
(i)<ins>Random Sampling:</ins>  Random samples of data of intended size from  a given dataset.<br>
```
filename = "dataset\\lengths.csv" # always add \\ for file name 
loadCSVObservation(file=filename)
sample_list = randomGenerator(5,20,"X")
m=1
for i in sample_list:
    print("Group {0}".format(m))
    print(i)
    m = m + 1
    print("--------")
```


(ii)<ins>Consecutive Sampling:</ins> Takes consecutive samples of the intended size.
```
filename = "dataset\\lengths.csv" # always add \\ for file name 
loadCSVObservation(file=filename)
sample_list = consecutiveGenerator(5,20,"X")
m=1
for i in sample_list:
    print("Group {0}".format(m))
    print(i)
    m = m + 1
    print("--------")
```

### <ins>**B. Charts for Variable Data:**<ins>
It is recommended that:
 - If subgroup = 1 : Use **X-MR chart**, also known as an **I-MR chart**
 - If subgroup size between 2 and 10 : Use **Xbar-Range Chart**
 - If subgroup size >= 11: Use Xbar - **Standard Deviation Chart**

#### **MR Chart**

#### **X Chart**

#### **Xbar Chart**
This graph helps us to view the mean change in a process over time. The control limits for the graph are:

We need to approximate the standard deviation, there are two ways we can do that:




#### **R Chart**

#### **S Chart**

### <ins>**C. Charts for Attribute Data:**<ins>

#### **p chart**

#### **np chart**

#### **c chart**

#### **u chart**
   
   
  

