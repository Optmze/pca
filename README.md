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
![c2](https://github.com/Optmze/project_pca/assets/95652520/a65bb609-6c44-436d-82e0-d75f38d84135)

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
![Capture](https://github.com/Optmze/project_pca/assets/95652520/9d4e96bf-7cea-41ee-a9f7-be7ad2bf31ae)

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

![sd_approx](https://github.com/Optmze/project_pca/assets/95652520/abc20f48-ea32-4de9-9701-8a3f6c3765b7)
or
![sd2_approx](https://github.com/Optmze/project_pca/assets/95652520/d0d9492d-4e9c-4b5c-825a-458f0daec230)

![xbar](https://github.com/Optmze/project_pca/assets/95652520/9d2a4400-ad59-4aaf-ba52-059df66e80ae)

#### **R Chart**

#### **S Chart**

### <ins>**C. Charts for Attribute Data:**<ins>

#### **p chart**

#### **np chart**

#### **c chart**

#### **u chart**
   
   
  

