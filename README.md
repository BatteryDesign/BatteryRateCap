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
The *data_converter* module converts charge/discharge data (voltage versus capacity) and capacity-cycle data 
into rate-capacity data. Complete procedures and example codes on how to use the *data_converter* module are 
detailed in Demo/Demo_data_converter.ipynb. Below is an excerpt of the *data_converter* demo notebook, showing 
the output of how *data_converter* categorizes capacity data by their C-rate in a capacity-cycle dataset. 
The conversion from voltage-capacity to capacity-rate data does not involve any visuals, so no figures are shown here.<br/>
![alt text](https://github.com/BatteryDesign/BatteryRateCap/blob/main/demo/data_converter_grouped.png)   
### Use case 2. Data Fitting
The *fitcaprate* module fits capacity-rate data and attains fitting parameters, including charatersitic time, 
*n* value, and capacity *Q* as described in the introduction. Complete procedures and example codes on how to 
use the *fitcaprate* module can be found in Demo/Demo_fitcaprate.ipynb. Below is an excerpt of the *fitcaprate* 
demo notebook, showing the results of fitted curves (red dashed curves) found by *fitcaprate* for a set of 
battery capcity-rate data (blue dots).<br/>
![alt text](https://github.com/BatteryDesign/BatteryRateCap/blob/main/demo/fitcaprate_example.png)
### Use case 3: Data visulization
The *visualization* module creates a panel plot that lays out 2D scatter plots of fitting parameters versus 
available battery design parameters realated to geometry and materials. Complete procedures and example 
codes on how to use the *visualization* module are detailed in Demo/Demo_visualization.ipynb. Below is an 
excerpt of the *visualization* demo notebook, showing the output panel plot.<br/>
![alt text](https://github.com/BatteryDesign/BatteryRateCap/blob/main/demo/visualization_example.png)
### Use case 4: Hypothesis testing
The *correlationtest* module determines whether a statistically-signicificant linear relationship exisits 
between found battery fitting parameters, which indicate the battery performance, and their desgin parameters
related to geometry and materials. Complete procedures and example codes on how to use the *correlationtest* 
module are detailed in Demo/Demo_correlationtest. Below is an excerpt of the *correlationtest* demo notebook, 
showing how the module plots the best-fit linear regression line (in blue) between two target parameters 
and highlights potential outliers (in red) to the linear relationship.
![alt text](https://github.com/BatteryDesign/BatteryRateCap/blob/main/demo/correlation_test_example.png)

 
## How to Install
*BatteryRateCap* can be installed by cloning the entire repoitory or via pip:</br>
```
pip install BatteryRateCap
```

## Software Dependency
- Python >=3.6
- See environment.yml for all Python package dependencies


## Community Guidelines
If you encounter any issue using *BatteryRateCap* or would like to request an additional feature, please report using a [Github 
issue](https://github.com/BatteryDesign/BatteryRateCap/issues). If you would like to directly contribute to this project, please email the 
reporsitory maintainers Doris Hung (dhung@uw.edu) and Praise Anyanwu (anyanc@uw.edu).


