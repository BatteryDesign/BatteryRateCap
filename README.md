[comment]: <> (Build Badge)
[![Build Status](https://travis-ci.com/3DBatteryDesign/3DLi-ionbattery.svg?token=TqLpfP3Qz3sXPyzzMFhK&branch=main)](https://travis-ci.com/3DBatteryDesign/3DLi-ionbattery)

# Design Rule Discovery for 3D Li-ionbattery
Three-dimensional (3D) batteries enable high power and energy by modifying the
conventionally 1D planar architecture of battery electrodes into complicated 3D
architectures. Many 3D battery architectures have been fabricated, but their
geometry and spatial arrangement have not been fully optimized due to the lack
of design rules. This project aims to assist the discovery new 3D battery design rules
among existing 3D battery cases with data science approaches. <br/>

### 3DLi-ionbattery Data Analysis and Visualization Python Package
The final products of our project include a Python pacakge for visualizing and 
analysing 3D battery data. The package is specifically tailored to the data structure 
of our 3D battery dataset. The pacakge contains (A) a data conversion component,
(B) a curve-fitting component, (C) a visulization component, and (D) a hypothesis testing component.

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

### Research Objectives
**1. Estimate Parameters for Rate Performance**: One experimental measure for the
the high-rate (power) perfromance of batteries (often composed of Sodium-ion or
Lithium-ion) is the observation of the capacity Q for varying charge or discharge
rate RT. The battery capacity tends to be inversely proportional to the discharge
rate (the latter is raised to a characteristic, parametric coefficient, n).
Using the outlines of the model described by *R. Tian & S. Park et. al.*
for a 1D battery, we extend the model for the case of a 3D battery to extract
the following parameters: the characterictic time scale associated with charging
and discharging the battery, the low rate specific capacity, normalized with
respect to a volume mass density for a 3D battery, and the coefficient of the
discharge rate, which gives a physical interpretation of the battery
behavior, e.g., a value of one-half and one is associated with a diffusion
limited and resisitant limited behavior of the battery electrode, respectively.
[[1]](#1) 
In general, these parameters relate the rate performance to physical quantities
such as, the electrode thickness, porosity, and particle size of the conductive
component, here, Lithium-ion. We use a least square curve fit procedure to
extract the above parameters based on a capacity versus rate discharge dataset.<br/>
**2. 3D Battery Design Rule 1 -- Rate-limiting coefficient n**:The parameter
n found from fitting rate-capacity data determines how drastic a battery expereincce 
capacity fade over increasing charge/discharge rates. In supercapacitor, n=1 signifies
the dominating resistance resulting in capacity fade is dues to in sufficeint conduction.
Likewise, n=1/2 represents a purely diffusion-limited cell. This is an empirical
metric derived from rate-capacity fitting to supercapacitors. In *R. Tian & S. Park et al*,
it is assumed that 1D Lithium-ion/Sodium-ion batteries follow the same metric. 
We analyze the usability of this metric for 3D batteries by visualizing the distribution
of n values fitted from our 3D battery data. Unlike the baseline paper where most n values
lie in the range of 0-2, our n values have a widely spreaded distribution with magnitude
as high as 8. The preliminary result shows that the n metric used for super capacitors
does not apply to 3D batteries. Further visualization on the n values versus 3D 
architecture types is required to determine the underlying factors for the variations in n.
Here we hypothesize that at least one additional rate-limiting mechanism, the kinetic
limitation, exists in 3D batteries and that there exists a different n metric for 3D
batteries. <br/>
**3. 3D Battery Design Rule 2 -- Tau-L relationship**: A quadratic realationship is 
found between the fitting parameter characterisitc time tau and the electrode 
thickness L in 1D batteries. We hypothesize that this relationship does not 
apply to 3D batteries. We will validate out hypothesis by plotting tau versus
L data from our 3D battery data. We will also visualize tau versus 3D electrode
charateristic length data among 3D architecture groups to analyze whether or not
a linear/quadratic relationship can be found.<br/>
**4. Mathematical versus Statistical model for 3D battery rate-limiting mechanism**:
Based on the tau-L realationship, our baseline paper discovered a mathematical 
model that relate tau to L and material paramteres including the diffusivities,
conductitivites, and the particle radius for 1D batteries. Here we will determine
whether a similar mathematical model can be found for 3D battereies with the same
approach. We will decided whether a general trend can be observed from data
visualization. If no significant pattern is easily detectable from our dataset,
we will determine whether it is a result of lack of data or that the pattern can 
only be found with statistical appraches.<br/>
### Research Outcomes
**1. Estimate Parameters for Rate Performance**:
Curve-fitting on our 3D battery data set shows that batteries with less than 4 points will return infinite standard deviation, which invalidate the fitting parameters. Filtering out the battery cases that have less than 4 data points, we have 11 cases that are successully fitted.<br/>
**2. 3D Battery Design Rule 1 -- Rate-limiting coefficient n**:
Visualization shows that the metric used to define rate-limiting mechanism for 1D batteries does not apply to 3D batteries. However, we are seeing a clear pattern that the same trend still holds. Therefore, with an adjusted metrics, rate-limiting mechanisms can still be identified by n values in 3D batteries. <br/>
**3. 3D Battery Design Rule 2 -- Tau-L relationship**:
Visualization suggests that 3D batteries has a concave second-order Tau-L realationship. <br/>
**4. Mathematical versus Statistical model for 3D battery rate-limiting mechanism**: As the Tau-L realationship cannot be determined conclusively due to few data points available, this research objective cannot be further investigated. Following the component chart, we shift our project goal to identifying what type of data and how much more data is needed, as well as facilitating the data collection process. Therefore, Task 3 and 4 are updated to create data conversion scripts in order to obtain more rate-capacity data.<br/>
## Project Workflow Chart
![Component specifications](https://user-images.githubusercontent.com/67809165/116957565-00c06480-ac4d-11eb-875b-8f5cb6cf1309.png)

### Gantt Chart
| Week                                              |  1  |  2   |  3   |  4   |  5  |  6   |  7   |  8   |  9   |  10  |
|---------------------------------------------------|-----|------|------|------|-----|------|------|------|------|------|
| Date                                              | 4/5 | 4/12 | 4/19 | 4/26 | 5/3 | 5/10 | 5/17 | 5/24 | 5/31 | 6/7  |
|Task 1: Curve Fitting Script                       |  O  |   O  |   O  |      |     |      |      |      |      |      |
|Task 2: Data Visualization                         |     |   O  |   O  |   O  |  O  |      |      |      |      |      |
|Task 3: Plot conversion Script: Discharge curve    |     |      |      |      |     |   O  |   O  |  O   |      |      |
|Task 4: Plot conversion Script: Capacity-cycle     |     |      |      |      |     |   O  |   O  |  O   |      |      |
|Task 5: Hypothesis Testing Script                  |     |      |      |      |     |      |   O  |  O   |      |      |
|   Compile Final Presentation Poster               |     |      |      |      |     |      |      |  O   |   O  |      |
|   Final Presentation                              |     |      |      |      |     |      |      |      |      |   O  |
|   Current Team Progress                           |     |      |      |      |     |   O  |      |      |      |      |
|[Removed Task]: Data-driven models Review          |     |      |      |      |     |   X  |   X  |  X   |      |      |
|[Removed Task]: DataYoink Neural Network           |     |      |      |      |     |   X  |   X  |  X   |      |      |

## References
<a id="1">[1]</a>
Tian, R., Park, SH., King, P., Cunningham, G., Coelho, J., Nicolosi, V.,
Coleman, J. 
Quantifying the factors limiting rate performance in battery electrodes.
Nat Commun, 10, 1933 (2019).
https://doi-org.offcampus.lib.washington.edu/10.1038/s41467-019-09792-9



