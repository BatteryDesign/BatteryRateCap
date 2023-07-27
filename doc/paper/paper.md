---
title: '*BatteryRateCap*: A Python Package for Comparative Battery Rate Capability Analysis'
tags:
  - Python
  - insertion electrode battery
  - rate-limiting
  - rate capability
authors:
  - name: Chih-Hsuan Hung
    orcid: 0000-0001-8930-1608
    affiliation: 1
  - name: C. Praise Anyanwu
    orcid: 0000-0003-0212-3488
    affiliation: 2
  - name: Kevin Martinez-Chavez
    orcid: 0009-0000-6874-4098
    affiliation: 3
  - name: Matthew J. Canin
    orcid: 0009-0001-7857-4413
    affiliation: 4
  - name: G. Kevin Lee
    orcid: 0009-0000-6874-4098
    affiliation: 4
  - name: Daniel T. Schwartz
    orcid: 0000-0003-1173-5611
    affiliation: 4 
  - name: David A. C. Beck
    orcid: 0000-0002-5371-7035
    affiliation: 4 
  - name: Corie L. Cobb
    orcid: 0000-0003-3381-2120
    affiliation: 1 
affiliations:
  - name: Department of Mechanical Engineering, University of Washington
    index: 1
  - name: Department of Chemistry, University of Washington
    index: 2
  - name: Department of Bioengineering, University of Washington
    index: 3
  - name: Department of Chemical Engineering, University of Washington
    index: 4
date: 27 July 2023
bibliography: paper.bib
---
# Summary

We present a Python package, *BatteryRateCap*, for comparative analysis
of insertion electrode batteries across different published datasets.
Due to the myriad of battery chemistries and testing procedures that
exist today, comparing battery performance across different cell and
electrode designs is challenging. To facilitate reuse and integration of
published data into new research studies, we need more standardized
reporting of datasets, as recently highlighted by battery experts
[@sun_experimental_2021; @stephan_standardized_2021; @mistry_minimal_2021],
and more consistent data analysis procedures along with the
corresponding software infrastructure. *BatteryRateCap* is an
open-source toolbox aimed at streamlining comparative analysis of
different battery datasets while facilitating a more efficient data
collection process for future reuse. Our goal is to help promote more
rigorous and consistent comparative data analysis in the battery
community through our toolbox.

*BatteryRateCap* analyzes battery rate capability, which focuses on how
capacity (the amount of energy in a battery) responds to changing
discharge and charge rates (the amount of current applied to a battery).
Leveraging the empirical capacity-rate model developed by Tian et
al.[@tian_quantifying_2019], *BatteryRateCap* is an open-source, 
four-component package that
facilitates a systematic workflow for rate capability analysis. First,
the feature extraction component uses least-square curve-fitting to
tailor battery capacity-rate datasets to Tian et al.\'s semi-empirical
model [@tian_quantifying_2019] in order to extract critical fitting
parameters. These fitting parameters help normalize battery rate capability
across different chemistries and reveal potential rate-limiting factors
[@tian_quantifying_2019]. Next, the
visualization and the correlation test components aid in discovering
patterns between the extracted fitting parameters and the battery's
design parameters such as electrode thickness, porosity, particle size,
and other material-dependent properties. Finally, a data conversion
component converts battery cycling and voltage discharge data to
capacity-rate datasets. This data conversion component allows the user
to collect datasets (having different formats or units) from various
sources to increase a user's available datasets and improve data
analysis reliability.

# Statement of Need

Batteries are complex devices that are multi-scale and multi-physics in
nature. Therefore, batteries are designed, characterized, and reported
in various standards and formats based on the focus of each research
study. When comparing different batteries, the materials, electrode
composition, test conditions, and other design features must be
carefully considered. The process to search, collect, and clean up
datasets requires significant manual labor and effort. As a result,
reusing battery datasets across multiple publications to conduct a
comparative data analysis can be challenging. To facilitate rapid data
reuse and integration, the battery community has proposed standardized
reporting with several checklist structures 
[@sun_experimental_2021; @stephan_standardized_2021; @mistry_minimal_2021].
Carrying through the
resolve to foster data-intensive research in the battery community,
*BatteryRateCap* is designed to lead the user through a sequential
battery rate capability analysis, and *BatteryRateCap* aids in every
step from data collection, to feature extraction, and to exploratory
data analysis. The ingenuity of *BatteryRateCap* is the capability to
organize and characterize various published battery datasets for ease of
comparative analysis.

# Description

*BatteryRateCap* has a feature extraction component that characterizes
the battery's capacity-rate datasets based on the model proposed by Tian
et al. [@tian_quantifying_2019], as shown in Equation 1:

$$Q = Q_{\max} \lbrack 1 - (R\tau)^{n}\left( {1 - e}^{{- (R\tau)}^{- n}} \right)\rbrack\tag*{(3)}$$

where *Q* is the measured capacity for an applied current rate, *R*, in
an experiment. The coefficients of the model in Equation (1), i.e.
$Q_{\max},$ $\tau$, and $n$, parameterize the fitting of the model to
the capacity-rate datasets. These fitting parameters, the low-rate
specific capacity $Q_{\max},$ the characteristic time associated with
charge/discharge $\tau$, and the parameter associated with rate-limiting
mechanism $n$, serve as important performance features that characterize
the capacity-rate behavior of batteries [@tian_quantifying_2019;@hung_are_2023]. *BatteryRateCap*
extracts these fitting parameters by least-square curve fitting of
Equation 1 to the capacity-rate datasets, using the trust region
reflective algorithm from SciPy package [@virtanen_scipy_2020]. \autoref{fig:1} 
demonstrates
fitting examples of two capacity-rate datasets using *BatteryRateCap*. In
\autoref{fig:1}, the blue markers are the input capacity-rate data, and the red
curve represents the best-fit curve. The optimized fitting parameters
with the associated standard errors (SEs) are shown on the plot and
tabulated in a separate Excel .csv file. In cases where there are not
enough data points from the input to find a best-fit curve, a warning
message is shown on the figure instead (see right panel in \autoref{fig:1}).

![Examples of a successful (left) and unsuccessful (right)
curve fitting results in *BatteryRateCap*.\label{fig:1}](fitcaprate_example_cropped.png)

The sparsity of datasets is a major contributor to the difficulty of
comparative analysis of batteries. To assist in the collection of
capacity-rate datasets, *BatteryRateCap* has a data conversion component
that converts two other types of battery datasets -- cycling and
voltage-capacity datasets -- to capacity-rate datasets. This component
is built under the premise that battery datasets are often
multi-dimensional and contain embedded information that can be harvested
and reused on different research subjects. As shown in \autoref{fig:2}, a
cycling dataset demonstrates a battery's capacity values corresponding
to changing current rates, where each data point represents the capacity
value measured in one charge or discharge cycle at a fixed current rate.
Typically, the battery is cycled at a fixed current rate repeatedly
before moving on to the next current rate, resulting in the signature
'staircase' pattern. *BatteryRateCap* identifies each stairstep with a
different color (see \autoref{fig:2}) and calculates the average capacity of
each stairstep. Then, the cycling dataset is converted to a
capacity-rate dataset by pairing the corresponding current rate to each
stairstep identified.

![Battery cycling data grouped for conversion to
capacity-rate data in *BatteryRateCap*\label{fig:2}](data_converter_paneled.png)

A similar feature that converts voltage-capacity data to capacity-rate
data is available, and a detailed demonstration can be found on the
Github repository. Additionally, to allow more integrated postprocessing
of the extracted fitting parameters, *BatteryRateCap* has visualization
and correlation testing components for basic exploratory data analysis.
Demonstrations of these two components are also available in the
repository. In summary, *BatteryRateCap* provides an open-source
infrastructure and standardized workflow for battery researchers to
conduct comparative rate capability analysis following Tian et al's
capacity-rate model approach [@tian_quantifying_2019]. In addition, *BatteryRateCap* can be
used to collect capacity-rate data reported in voltage capacity and
cycling plots. This allows access to the previously embedded and often
overlooked capacity-rate datasets. We hope this package helps accelerate
more data-intensive work in the community and lays the groundwork for
future electrochemical analysis research.

# Acknowledgements

This project was supported by the Data Intensive Research Enabling
Clean Technology (DIRECT) National Science Foundation (NSF) National
Research Traineeship (DGE-1633216), the State of Washington through the
University of Washington (UW) Clean Energy Institute and the UW eScience
Institute, in part upon the work of S.A. and G.A.W. supported by the NSF
Graduate Research Fellowship under Grants No. DGE-1762114 and
DGE-1256082, respectively, and via funding from the Washington Research
Foundation.

This work was funded by a Defense Advanced Research Projects Agency
(DARPA) Young Faculty Award under grant number D19AP00038. The views,
opinions, and findings expressed in this work are those of the authors
and should not be interpreted as representing the official views or
policies of the Department of Defense or the U.S. Government and no
official endorsement should be inferred. This is approved for public
release and distribution is unlimited.

# References
