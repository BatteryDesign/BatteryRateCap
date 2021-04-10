# 3DLi-ionbattery
Three-dimensional (3D) batteries enable high power and energy by modifying the
conventionally 1D planar architecture of battery electrodes into complicated 3D
architectures. Many 3D battery architectures have been fabricated, but their
geometry and spatial arrangement have not been fully optimized due to the lack
of design rules. This project aims to discover new 3D battery design rules
among existing 3D battery cases with data science approaches. This project aims
to discover new 3D battery design rules among existing 3D battery cases with
data science approaches.

### Use Cases and Componennt Specifications
** Estimate Parameters for Rate Performance**: One experimental measure for the
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
extract the above parameters based on a capacity versus rate discharge dataset.

## References
<a id="1">[1]</a>
Tian, R., Park, SH., King, P., Cunningham, G., Coelho, J., Nicolosi, V.,
Coleman, J. 
Quantifying the factors limiting rate performance in battery electrodes.
Nat Commun, 10, 1933 (2019).
https://doi-org.offcampus.lib.washington.edu/10.1038/s41467-019-09792-9
