[comment]: <> (Build Badge)
[![Build Status](https://app.travis-ci.com/BatteryDesign/BatteryRateCap.svg?branch=main)](https://app.travis-ci.com/github/BatteryDesign/BatteryRateCap)


# *BatteryRateCap*: A Python Package for Analyzing and Visualizing Battery Rate Capability
This pacakge is intended to faciliate battery 
rate capability analysis based on an empirical model approach developed by 
[Tian et al.](https://doi.org/10.1038/s41467-019-09792-9). 
A common phenomenon in intercalation batteries is decreasing battery capacity (mAh, mAh/g, or 
mAh/cm<sup>2</sup>)
to increasing charge and discharge current rate (A, A/cm<sup>2</sup>, or 1/hour). 
Rate capability is a battery's ability to maintain its maxnimum 
theoretical capacity when charged and discharged at high current rates. 
According to Tian et al., a battery's capacity (*Q*) versus current rate (*R*) data, also called the 
capacity-rate data,can be analyzed 
using the following empirical model:<br/>

Q = Q<sub>max</sub> ( 1 - (R $\tau$	)<sup>n</sup> (1-e<sup>-(R $\tau$	
)<sup>-n</sup></sup>)) <br/>

By fitting the capcaity-rate data to the empirical model, we can obtain
three fitting parameters that quantify the performace of a battery:
- The characterictic time ( $\tau$ ) is associated with the time required to fully charge or discharge a 
battery. A smaller $\tau$ means higher rate capability.
- The low rate specific capacity (*Q<sub>max</sub>*) measures a battery's maximum theoretical capacity, which 
normalizes
$\tau$ and *n* such that batteries made with different materials can be compared on the same scale.
- The exponent *n* gives a physical interpretation of the rate-limiting transport mechanism in 
a battery.
For more insight about the fitting parameters, please visit [Tian et 
al.(2019)](https://doi.org/10.1038/s41467-019-09792-9) and [Hung et 
al.(2022)](https://doi.org/10.1021/acsenergylett.2c02208).
 
![alt 
text](https://github.com/BatteryDesign/BatteryRateCap/blob/main/doc/Component_chart.jpg)

*BatteryRateCap* is composed of four components, each supports a function 
to allow or enhance the rate capability analysis approach developed by Tian et al.
The interdependency bewteen components are shown in the diagram above, where a brief desciprtion of each component can be found below:<br/>
- (A) a data conversion component to convert voltage-dicharge data and/or capacity-cycle data to capacity-rate 
data
- (B) a curve-fitting component to fit experimental capacity-rate data to Tian et al's empirical model.
- (C) a visulization component to plot the fitting parameters obtained from component (B) against other physical 
quantities such as the battery electrode thickness and porosity. 
- (D) a hypothesis testing component to compare different battery cases based on their rate capability 
charateristics and to detect outliers in a linear relationship. <br/>



## Example Use Cases for Battery Researchers
### Use case 1. Data Conversion
The data conversion module converts charge/discharge data (voltage versus capacity) and capacity-cycle  into rate-capacity data.
   
### Use case 2. Data Fitting
The curve-fitting module fits capacity-rate data and attains fitting parameters, including charatersitic time, *n* value, and capacity *Q* as described in the introduction.

### Use case 3: Data visulization
The  data visualization module plots fitting parameters versus battery geometry/material parameters. 

### Use case 4: Hypothesis testing
The hypothesis testing module determines whether a statistically-signicificant linear relationship exisits between 3D battery desgin parameters and performance.

 
## How to Install
*BatteryRateCap* can be installed by cloning the entire repoitory or via pip:</br>
```
pip install batteryratecap
```

## Software Dependency
- Python >=3.6
- See environment.yml for all Python package dependencies


## Community Guidelines
If you encounter any issue using *BatRateCap* or would like to request an additional feature, please report using a [Github 
issue](https://github.com/BatteryDesign/BatteryRateCap/issues). If you would like to directly contribute to this project, please email the 
reporsitory maintainer at .


