[comment]: <> (Build Badge)
[![Build Status](https://travis-ci.com/3DBatteryDesign/3DLi-ionbattery.svg?token=TqLpfP3Qz3sXPyzzMFhK&branch=main)](https://travis-ci.com/3DBatteryDesign/3DLi-ionbattery)

# *BatteryRateCap*: A Python Package for Analyzing and Visualizing Battery Rate Capability
This pacakge is intended to faciliate analysis on battery 
rate capability based on an empirical model appraoch developed by 
[Tian et al.](https://doi.org/10.1038/s41467-019-09792-9). 
A common phenomenon in intercalation batteries is decreasing battery capacity (mAh, mAh/g, or 
mAh/cm<sup>2</sup>)
to increasing charge and discharge current rate (A, A/cm<sup>2</sup>, or 1/hour). 
Rate capability is a battery's ability to maintain its maxnimum 
theoretical capacity when charged and discharged at high current rates. 
According to Tian et al., a battery's capacity versus rate data, also called the capacity-rate data,can be analyzed 
using the following empirical model:<br/>

$$
Q = Q<sub>max</sub> \left(1-(R \tau )<sup>n</sup> \left(1-e<sup>-\left(R \tau 
)\right<sup>-n</sup></sup>)\right)\right
$$ <br\>

By fitting the capcaity-rate data from experiments to the above empirical model, we can obtain
three fitting parameters that quantify the performace of a battery:
- The characterictic time ( $\tau$ ) is associated with the charge
and discharge time. A smaller $\tau$ means higher rate capability.
- The low rate specific capacity (*Q<sub>max</sub>*) measures a battery's maximum theoretical capacity, which 
normalizes
$\tau$ and *n* such that batteries made with different materials can be compared on the same scale.
- The exponent *n* gives a physical interpretation of the rate-limiting transport mechanism in 
a battery.


*BatteryRateCap* is composed of four components, each supports different functions to allow the rate capability analysis approach developed by Tian et al.: <br/>
A. a data conversion component to convert voltage-dicharge data and/or capacity-cycle data to capacity-rate data
B. a curve-fitting component to fit Tian et al.'s model to the experimental capacity-rate data
C. a visulization component to plot the fitting parameters obtained from component (B) against other physical quantities such as the battery electrode thickness and porosity 
D. a hypothesis testing component to compare different battery cases based on their rate capability charateristics. <br/>

The interdependency bewteen components are shown in the diagram below:
![alt 
text](https://github.com/BatteryDesign/BatteryRateCap/blob/main/doc/Component_chart.jpg)


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

### How to Install
*BatteryRateCap* can be installed by cloning the repo or via pip:<\br>
```
pip install batteryratecap
```

### Software Dependency
- Python 3
- See environment.yml for all Python package dependencies

### Community Guidelines
If you encounter any issue using *BatRateCap* or would like to request an additional feature, please report using a [Github issue]().


