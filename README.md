# pca
pca is a single file script which implements Shewhart charts to aid with Process Control Analysis. <br>

<b>For more detailed notes that I took while trying to implement the same can be found here:</b>
https://docs.google.com/document/d/1pkbh8Tx12znxN-BH2zfXEK3SEfHIz5LWCbud4BF4VIE/edit?usp=sharing

***Process Control Notes by Optmze(<ayush.devmail@gmail.com>)***

## **Statistical Process Control and Variability:**

The general approach is descriptive rather than analytical, the aim is not to model the distribution of data for a given process but instead control the process using decision rules to look out for significant changes between observed data and standards of the process.

For example a let us take piston cycle times<br>
![1](https://github.com/Optmze/pca/assets/95652520/b85c39d5-b08b-479f-b3d7-4d676d363d4b)


If we have say data for 50 cycle times with the same operating conditions
Here: Cycle time varies between 0.22 and 0.69 seconds even though the operating conditions are the same.
Avg cycle time = 0.392 seconds
S.D = 0.114 seconds<br>

![2](https://github.com/Optmze/pca/assets/95652520/bbf3b152-324d-44ce-a293-6f42d43d0d67) ![3](https://github.com/Optmze/pca/assets/95652520/7cdf8059-f8cf-4c80-9cde-d48159131518) 


**A production process has many sources or causes of variation**, factors that are permanent (natural part of process) are called **common causes** of variation. We can only reduce any negative effects of these chronic/common causes of variability by modifying the process.

**Special causes/assignable causes/sporadic spikes** rise from external and temporary sources, which are not a common cause. Example: for our piston here it could be an increase in temperature. To detect occurrence of special causes we need a “control mechanism”

Here: Say we have 20 subgroups with 5 cycle times each, we compute subgroup average and standard deviation and generate charts:

The chart of averages is called an X-bar chart and the chart of standard deviations is called an S-Chart. We can see the center values: average of cycle time averages = 0.045s and the average of the sd is 0.0048s. Here the observed variability is due to common causes. But say we introduce a forced changed like increasing the temperature at rate of 20% per group, now the charts show:<br>
 ![4](https://github.com/Optmze/pca/assets/95652520/3a1f3f17-b1a1-456d-83ed-8cb9c283a97e) ![5](https://github.com/Optmze/pca/assets/95652520/a7286f96-c339-4f6e-8178-0184c6ff8c98)
 <br>




(UCL = upper control limit, LCL = lower control limit and CL is control limit)

We can see that in the x bar chart up to the 7th sample (scaling is a bit different in both chart) is identical but in the 8th sample it’s a little above average and then the next one is a huge increase and that trend includes, to have more than 10 points run is unlikely to occur by chance which means common causes are no longer the only causes of variation. (here we know it’s because temperature as increased).(The S chart shows a downward trend with several points falling below the average of 0.004 beginning at the 8th sample)

Also note how there’s a shift after the 8th sample we see the new average cycle time to be around 0.052s. Process operators can analyze Xbar and S charts to stop and adjust the process in case spikes like these appear(timing is important).

**NOTE:** A run chart doesn’t have UCL and LCL, by adding those it becomes a control chart. Control charts have wide applicability


## **Driving a process with Control Charts:**

To determine when to take action in order to adjust a process affected by a special cause and when to leave it alone and not misinterpret variations from common causes.

Types: **Control chart for variable data**, **Control Charts for attribute data**

Attribute data needs definition of the problem:

- If binary classification (eg pass or fail, conforms vs non-conform) = track proportion of units that don’t conform (**p - chart**)
- If size of observation fixed, no of non-conforming units can be tracked (**np-chart**)
- When observation has no of nonconformities you can have **c-chart**(no of nonconformities) or **u-chart** (rate of nonconformities = no of nonconformities per unit of observation / opportunities for errors)

For variable data two classes: one that can be repeatedly sampled and second measurements that are derived one at a time(monthly sales)(use control charts here we using moving range charts)

- We saw in the charts above 3 lines = Central Line (at the total avg), LCL and UCL. The UCL and LCL indicate the range of variability we expect to observe around the center line.
- For a 3-sigma chart: control limits are at 3 SDs of x-bar away from central line: ![7](https://github.com/Optmze/pca/assets/95652520/b156cc2c-3a79-485a-8bf0-55cfbe4663ac)


(On average only 1/370 are expected to fall out of these limits, a rare event) -> **So when a point falls beyond the control limits we can question the stability of the process.**

- Very low chance that it’s a false alarm, also stable random variation does not exhibit patterns of upward/downward trends or consecutive runs of points above or below the center line. In general the patterns to look out for are:

![8](https://github.com/Optmze/pca/assets/95652520/69efb686-bcdc-4481-a60c-f4fa1f54624a)

Example of the above four:<br>![9](https://github.com/Optmze/pca/assets/95652520/214b548a-a35b-4dff-b0b6-f802b58b2bb0)![10](https://github.com/Optmze/pca/assets/95652520/90aa1c31-b0d7-4dc6-81a2-98ef8f598c81)



## **WHICH CHART TO USE WHEN?**

![11](https://github.com/Optmze/pca/assets/95652520/af71b755-58b6-4b6b-8486-07beebe1a9b3)


- When counting non-conformities of a certain event or phenomenon = use c(assumes a fixed likelihood) or u(varying likelihoods)charts, provides more info but it cannot be combined without the different types of conformities.
- For large subgroups (>1000), number of incidences/incidents per unit/percent defectives considered as individual measurement, X-chart for subgroups of size 1 can be used.
- If measurements are grouped in samples you can use X-bar charts(sample averages) + R charts(sample range: max-min) or S Charts(sample standard deviation). For samples larger than 10 use S charts over R charts. If sample size varies only use S-charts.
- WE USE CONTROL CHARTS TO DETECT OCCURRENCE OF SPECIAL, SPORADIC CAUSES WHILE MINIMIZING THE RISK OF OF A FALSE ALARM -> to do so we need to assess the effect of chronic, common causes and setup control limits that reflect the variability. (**process capability study** = study of process variability before using control charts)
- Attribute process capability studies to determine a process capability in terms of fraction of defective output, we use data collected over several time numbers.
- **RULE OF THUMB** = 3 time periods with 20-25 samples of size 50-100 units each; for each sample a control chart is drawn which will show the special cases, we remove those cases and a new control chart is generated which indicates the process capability (center line is the measure for that)
- Note: when sample sizes are large (>1000), control charts become ineffective as very narrow control limits, so we use X-charts instead.
- Variable data is info represented and recorded as measurements (quantitative), and has numerical values. Whereas attribute data is basically more qualitative(boiled down to a yes/no question), is a certain standard being met (example will a bridge break if a car passes through it)
- For Variable process capability studies, process capability is determined via distribution of measurement characteristics. We need relatively less data here, the samples are called rational subgroups; It is aimed at measuring variability due to common causes only. Control limits are determined from measures of location and variability in each subgroup; any deviation from a stable pattern relative to it indicates a special cause.

For example here: Say rational subgroup has 5 consecutive cycle times, the avg and sd is calculated for them; the 3 sigma control limits are calculated:

A time plot(time is on the x axis) of 20 consecutive averages(20\*5=100), it shows the pattern for

![12](https://github.com/Optmze/pca/assets/95652520/c0b53d21-783f-4840-8348-18496ddf6233)


- The probability that an rv is larger than 0.99 is 0.1; 16% of the future cycle times will be above the USL (0.050s), 24% will be lower than 0.003s. With the analysis we can see the piston is incapable of complying with the specifications.
- **Process capability indices**

## **Capability Indices**
Two indices are used to assess process capability :

- **Cp** = indicator of the potential of process to meet 2 sided spec with few defects as possible; Full potential when process is centered at midpoint of specification limits

![13](https://github.com/Optmze/pca/assets/95652520/65be9e9c-e845-4127-b7b4-82ff123af2b2)


**Numerator = how wide the specs are**<br>
**Denominator = width of process** = range that accounts for 99.73% of observation with variability due to common causes only;

Used to see if a process is capable, they are not concerned with control of a process; (The larger the better, remember it can never be zero; but remember just because Cp>1 it doesn’t mean good quality as process has to be centered within the specification limits) (If Cp is <1 the variation will never fit and process will never be capable)

When Cp=1, we expect 0.27% of observation to fall outside the spec limits; The target for modern industry is to reach Cp=2( which basically says there will be no defective products)(possible shift in location of process mean by 1.5 sds)

- **Cpk**:

![14](https://github.com/Optmze/pca/assets/95652520/9881ad88-0b9d-465d-a066-fde8f3e57509)


Process mean is not centered midway between the spec limits; Cpk is different from Cp Basically:<br>
Non-centered processes have potential capability measured by Cp and their actual capability measured by Cpk; validity of Cp and Cpk indices is questionable in cases the measurements are skewed instead of normally distributed(proper form can be treated with bootstrapping).

Common practice to estimate Cp or Cpk:

![15](https://github.com/Optmze/pca/assets/95652520/0818afde-8176-444d-8d0f-a22e6ebc7d95)<br>
![16](https://github.com/Optmze/pca/assets/95652520/3ba6852b-3892-4f3b-bcf4-e5268e6bb7e0)



(X’ is sample mean)


## **THE SHEWHART CONTROL CHARTS** <br>
The detection procedure:<br>
“Every h unit of time, a sample of size n is drawn from the process.”
Θ = parameter of the distribution of observed random sample(x1…xn) <br>
![29](https://github.com/Optmze/pca/assets/95652520/a09fcb35-9ae9-4a67-9cd6-77171465725b) =
 Appropriate estimate of n<br>
![30](https://github.com/Optmze/pca/assets/95652520/46763e01-7b81-4767-8b2d-f1ef9766619a)


As long as the below condition is true, we can say the process is in statistical control:
![31](https://github.com/Optmze/pca/assets/95652520/1439a400-7793-4886-8d1d-637a2e587d72)<br>
![32](https://github.com/Optmze/pca/assets/95652520/6de4be20-e422-46dd-93fa-c6ce320ef76e)

Note: Samples are independent and xbar\_n is distributed as N(theta\_0,var/n) as long as process is under control; alpha = probability of observing xbar\_n outside CL (alpha = 0.0027); We expect about 5% to lie outside WL (alpha = 0.05).

Note: Samples are usually taken of small sizes and more frequently to reduce the possibility of a shift would happen during sampling ( but if too frequent there is higher chance of detecting a shift early)

## **CONTROL CHARTS FOR ATTRIBUTES**<br>
![33](https://github.com/Optmze/pca/assets/95652520/d3623188-cb60-442f-a489-172afa86209f) ![34](https://github.com/Optmze/pca/assets/95652520/a20abc97-b252-4f85-9427-c2fcc3676ab1) <br>
![35](https://github.com/Optmze/pca/assets/95652520/d15f8503-2fa3-4bc4-a09e-8d1f1287afbc)

Similar way for all the other charts:

## **CONTROL CHARTS FOR VARIABLES** <br>
![36](https://github.com/Optmze/pca/assets/95652520/30363e02-6d16-4d7f-a46a-ce1832d249ca)


## **X-BAR CHARTS**<br>
We observe the process for k sampling period and compute the estimate of the process mean and sd. Process sd can be estimated using the average sample deviation or the average sample range:<br>
![37](https://github.com/Optmze/pca/assets/95652520/7cd57498-6895-4ecd-adaf-be1b35a41904)

Factors c(n) and d(n) guarantee unbiased estimate of sigma:
![38](https://github.com/Optmze/pca/assets/95652520/8df09612-1d97-47b9-a539-829ea8c80641)![38](https://github.com/Optmze/pca/assets/95652520/b35adedd-98ee-4b3b-9134-7156c3e7eefd)
![39](https://github.com/Optmze/pca/assets/95652520/4d976f4e-14ea-4901-b83e-9c1e7d6eef28) <br>
![40](https://github.com/Optmze/pca/assets/95652520/4af2b281-5625-45f6-b73c-b7a578c6282d) <br>

The control limits can be found out as: (3/c(n)\*sqrt(n)) = A value (thus UCL = X’’ + A1S’ )<br>

## **S and R charts** <br>
R charts are easier to produce so we use those, but it is not very efficient and its efficiency declines as sample size increases; should not be used for sample size greater than 5.

For S chart: the control limits: (here sigma\_s is estimate of standard deviation S, also shown below):<br>
![41](https://github.com/Optmze/pca/assets/95652520/cf2a7e4a-32a0-47b3-bb3b-1b6a83367a4a) <br>
![42](https://github.com/Optmze/pca/assets/95652520/87490ffa-5a03-48fe-b482-fe6e59139085) <br>
For the unbiased estimate again divide by c(n):<br>
![43](https://github.com/Optmze/pca/assets/95652520/8996887c-0f88-464b-a6c5-6ada722f4e8d) <br>
**Note:** The center line is S’

The R chart can be constructed using similar technique ; center line = R’ Control limits are:<br>
![44](https://github.com/Optmze/pca/assets/95652520/42f4d006-35ca-4fe0-b245-59eadb8d05c0)



## **Z-SCORE**

Higher Z score means more sds are within specification limits and the process avg is away from the outlying limits
![53](https://github.com/Optmze/pca/assets/95652520/8f2a2979-5ad3-4e75-a6e3-95831b10e626)
![54](https://github.com/Optmze/pca/assets/95652520/62943f94-c2af-4cc1-8d5b-acb30aaf0f0a)



## **Tools for Process Control and Process Improvement**
Flow Charts, Check Sheets(data collection), Run Charts, Histogram,Pareto Charts,Scatter Plots,Cause and Effect Diagrams 


## References:
> 1.Google Images for certain graph images <br>
> 2.Industrial Statistics: A Computer-Based Approach with Python by Ron S.Kennet, Shelemyahu Zacks and Peter Gedeck



