# project_pca
pca is a single file script which implements Shewhart charts to aid with Process Control Analysis.<br>
**Process Control Tools** > **pca.py** (The implementation) <br>
**dataset** (sample datasets) <br>

## Implementation Details
These are the following components in pca.py:

### <ins>**A. Sampling**</ins>
Sampling the given CSV Dataset to preferred **sample size** and **subgroup count**. It has two main methods of sampling:<br>
(i)<ins>Random Sampling:</ins>  Random samples of data of intended size from  a given dataset.<br>
(ii)<ins>Consecutive Sampling:</ins> Takes consecutive samples of the intended size.

### <ins>**B. Charts for Variable Data:**<ins>
It is recommended that:
 - If subgroup = 1 : Use **X-MR chart**, also known as an **I-MR chart**
 - If subgroup size between 2 and 10 : Use **Xbar-Range Chart**
 - If subgroup size >= 11: Use Xbar - **Standard Deviation Chart**

#### **X-MR Chart**

#### **Xbar-R Chart**

#### **Xbar-S Chart**

### <ins>**C. Charts for Attribute Data:**<ins>

#### **p chart**

#### **np chart**

#### **c chart**

#### **u chart**
   
   
  

