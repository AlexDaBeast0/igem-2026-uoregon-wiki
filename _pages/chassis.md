---
layout: page
permalink: chassis

title: Chassis
subtitle: This is the chassis module page.
banner: https://static.igem.wiki/teams/6041/wiki/placeholders/petunias.avif
---
We designed an experimental pipeline to evaluate the activity of NARK and NARU across a range of carbon and nitrate concentrations. Varying sugar concentrations was intended to model differences in the availability of carbon sources within groundwater and wastewater, while simultaneously evaluating the effects of differing nitrate concentrations.

This approach was motivated by the project's intended application in groundwater and wastewater environments, where readily available carbon sources may be limited or highly variable. Because carbon availability can directly influence bacterial growth and metabolic activity, it is important to characterize the limitations of the bacterial host under carbon-limited conditions. Evaluating NARK and NARU across these nutrient gradients will help determine whether the system can maintain nitrate-reduction activity when carbon availability is low. These results will provide important information for assessing the feasibility and performance of the system in long-term environmental applications.

# Design

T7 BL21(DE3) *Escherichia coli* cells were selected as the host strain during the experimental design phase to enable inducible expression of recombinant genes of interest under control of the T7 expression system. BL21(DE3) was selected because it provides the T7 RNA polymerase required for expression from T7 promoters and is a well-established host for recombinant protein production. Additionally, *E. coli* naturally possesses the *nar* gene family, which encodes components involved in nitrate reduction and provides a relevant endogenous system for investigating nitrate metabolism.

The experimental design consisted of two complementary experiments designed to evaluate the effects of nitrogen and carbon availability on nitrate reduction. In the first experiment, carbon availability was held constant while nitrogen availability was systematically varied. A control condition was established using a growth medium without supplemental nitrate, representing the baseline condition. Experimental groups were then supplemented with sodium nitrate at stepwise concentrations, increasing in 1 mM increments. Glucose concentration and other growth conditions were maintained consistently across all treatment groups to minimize the effects of variables other than nitrate availability. This experimental design allowed changes in nitrate utilization and nitrite production to be evaluated as a function of increasing nitrate concentration.

A second experiment was conducted in parallel using the inverse experimental design. In this experiment, nitrogen availability was held constant while the concentration of the primary carbon source, glucose, was systematically decreased. Glucose concentrations ranged from 2% to 0.01%, allowing the effect of carbon limitation on nitrate reduction to be evaluated while maintaining a consistent nitrogen environment. Comparing the two experimental conditions provides a means of determining whether nitrate reduction is primarily influenced by nitrogen availability, carbon availability, or the interaction between these two nutrients.

Following incubation, samples from each experimental condition were analyzed using a Griess assay to quantify nitrite production. The Griess reaction detects nitrite through the formation of a colored azo compound, with the resulting signal being proportional to the concentration of nitrite in the sample. Because nitrate must first be reduced to nitrite for this signal to be generated, increased nitrite levels relative to the nitrate-free control provide evidence of nitrate reduction by the cells. Comparison of nitrite concentrations across the nitrate and glucose gradients can therefore be used to assess how substrate availability affects nitrate-reducing activity.

Appropriate biological replicates and technical replicates should be included for each condition to account for biological variability and assay-to-assay variation. Growth measurements, such as optical density (OD600), should also be collected alongside the Griess assay when possible. Normalizing nitrite production to cell density would help distinguish changes in nitrate-reduction activity from differences caused simply by differences in bacterial growth.
