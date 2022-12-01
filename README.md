[comment]: <> (Build Badge)
[![Build Status](https://travis-ci.com/3DBatteryDesign/3DLi-ionbattery.svg?token=TqLpfP3Qz3sXPyzzMFhK&branch=main)](https://travis-ci.com/3DBatteryDesign/3DLi-ionbattery)

# *BatteryRateCap*: A Python Package for Analyzing and Visualizing Battery Rate Capability
This pacakge is intended to faciliate qualitative analysis on battery 
rate capability based on an empirical model appraoch developed by 
[Tian et al.](https://doi.org/10.1038/s41467-019-09792-9). 
Rate capability is a battery's ability to maintain its maxnimum 
theoretical capacity (mAh, mAh/g, or mAh/cm^2) 
when charged and discharged at high current rates (A, A/cm^2, or 1/hour). 
According to Tian et al., a battery's capacity-rate data can be modeled 
using the following empirical model:

The empirical model quantifies the rate capability three fitting parameters:
- The characterictic time (*$tau$*) associated with the charge
and discharge time
- The low rate specific capacity (*$Q_max$*) normalized with
respect to a volume mass density
- The exponent *n*, which gives a physical interpretation of the rate-limiting transport mechanism in 
a battery.


*BatteryRateCap* is composed of four components: <br/>
A. a data conversion component to convert voltage-dicharge data and/or capacity-cycle data to capacity-rate data
B. a curve-fitting component to fit Tian et al.'s model to the experimental capacity-rate data
C. a visulization component to plot the fitting parameters obtained from component (B) against other physical quantities such as the battery electrode thickness and porosity 
D. a hypothesis testing component to compare different battery cases based on their rate capability charateristics. <br/>

The interdependency bewteen components are shown in the diagram below:
![alt text](https://github.com/3DBatteryDesign/3DLi-ionbattery/blob/0d35484f2e800dfc9533d3d9f63d8ed553d17337/doc/Python%20Package%20Component.png)


### Use Cases
1. Use case 1: Data Fitting
   - Our curve-fitting module is for any researchers who would like to fit their capacity-rate data and attain fitting parameters including charatersitic time, n value, and capacity Q as described in the *Research Objectives* section. 
   - Target users: Battery researchers who have rate-capacity data
2. Use case 2: Data visulization
   - Our data visualization module is for any researchers that wish to visualize their batteries data with plots of fitting parameters versus battery geometry/material parameters. 
   - Target users: Battery researcher who have multiple sets of battery data that include charateristic time, n value, capacity, and other geometry/material parameters. 
3. Use case 3: Data conversion
   - Our data conversion module can be used to convert voltage-discharge curves and capacity-cycle plots into rate-capacity data.
   - Target users: Battery researchers who have voltage-discharge/capacty-cycle data
4. Use case 4: Hypothesis testing
   - Our hypothesis testing module can be used to determine whether a statistically-signicificant linear relationship exisits between 3D battery desgin parameters and performance.
   - Target users: Battery researchers who have battery desgin parameter and performance data.

### Workflow for using *BatteryRateCap*
![Component specifications](https://user-images.githubusercontent.com/67809165/116957565-00c06480-ac4d-11eb-875b-8f5cb6cf1309.png)

### How to Install

### Software Dependency
- Python 3
- See environment.yml for all Python package dependencies

### Community Guidelines
If you encounter any issue using *BatRateCap* or would like to request an additional feature, please report using a [Github issue]().


