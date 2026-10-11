---
layout: page
permalink: chassis

title: Chassis
subtitle: Evaluating and optimizing our bacterial chassis.
banner: https://static.igem.wiki/teams/6041/wiki/placeholders/petunias.avif
---


Two key factors of our chassis that we focused on optimizing were ability to take up nitrate and survive in the low temperatures required for implementation. For uptake, we decided to utilize the the NAR gene protein family for nitrogen import and reduction s as they already have a decent efficiency, and we wanted to avoid any unnecessary metabolic strain  {% cite cleggRolesPolytopicMembrane2002c --file chassis %} . As for the temperature requirement, we utilized directed evolution of our starting T7 BL21(DE3) *Escherichia coli* to lower its ideal growth temperature {% cite miyazakiDirectedEvolutionStudy2000 --file chassis %}.

# Uptake

 We designed an experimental pipeline to evaluate the activity of NARK and NARU across a range of carbon and nitrate concentrations. While this experimental pipeline does not directly test for transportation, it does test for nitrate reduction of the entire cell. which correlates to uptake.  Varying sugar concentrations were intended to model differences in the availability of carbon sources within groundwater and wastewater, while simultaneously evaluating the effects of differing nitrate concentrations {% cite chenImpactCarbonNitrogen2003 --file chassis %}.

This approach was motivated by the project's intended application in groundwater and wastewater environments, where readily available carbon sources may be limited or highly variable. Because carbon availability can directly influence bacterial growth and metabolic activity, it is important to characterize the limitations of the bacterial host under carbon-limited conditions {% cite chenImpactCarbonNitrogen2003 --file chassis %}. Evaluating NARK and NARU across these nutrient gradients will help determine whether the system can maintain nitrate-reduction activity when carbon availability is low. These results will provide important information for assessing the feasibility and performance of the system in long-term environmental applications.

## Design

T7 BL21(DE3) *Escherichia coli* cells were selected as the host strain during the experimental design phase to enable inducible expression of recombinant genes of interest under control of the T7 expression system. T7 express was selected because it provides the T7 RNA polymerase required for expression from T7 promoters and is a well-established host for recombinant protein production {% cite ProteinExpressionT7 --file chassis %}. Additionally, *E. coli* naturally possesses the *nar* gene family, which encodes components involved in nitrate reduction and provides a relevant endogenous system for investigating nitrate metabolism {% cite cleggRolesPolytopicMembrane2002c --file chassis %}.

The experimental design consisted of two complementary experiments designed to evaluate the effects of nitrogen and carbon availability on nitrate reduction. In the first experiment, carbon availability was held constant while nitrogen availability was systematically varied. A control condition was established using a growth medium without supplemental nitrate, representing the baseline condition. Experimental groups were then supplemented with sodium nitrate at stepwise concentrations, increasing in 1 mM increments. Glucose concentration and other growth conditions were maintained consistently across all treatment groups to minimize the effects of variables other than nitrate availability. This experimental design allowed changes in nitrate utilization and nitrite production to be evaluated as a function of increasing nitrate concentration {% cite cleggRolesPolytopicMembrane2002c --file chassis %}.

A second experiment was conducted in parallel using the inverse experimental design. In this experiment, nitrogen availability was held constant while the concentration of the primary carbon source, glucose, was systematically decreased. Glucose concentrations ranged from 2% to 0.01%, allowing the effect of carbon limitation on nitrate reduction to be evaluated while maintaining a consistent nitrogen environment. Comparing the two experimental conditions provides a means of determining whether nitrate reduction is primarily influenced by nitrogen availability, carbon availability, or the interaction between these two nutrients.

Following incubation, samples from each experimental condition were analyzed using a Griess assay to quantify nitrite production. The Griess reaction detects nitrite through the formation of a colored azo compound, with the resulting signal being proportional to the concentration of nitrite in the sample. Because nitrate must first be reduced to nitrite for this signal to be generated, increased nitrite levels relative to the nitrate-free control provide evidence of nitrate reduction by the cells. Comparison of nitrite concentrations across the nitrate and glucose gradients can therefore be used to assess how substrate availability affects nitrate-reducing activity.

Appropriate biological replicates and technical replicates should be included for each condition to account for biological variability and assay-to-assay variation. Growth measurements, such as optical density (OD600), should also be collected alongside the Griess assay when possible. Normalizing nitrite production to cell density would help distinguish changes in nitrate-reduction activity from differences caused simply by differences in bacterial growth .

# Directed Evolution

We directed the evolution of T7 BL21(DE3) *Escherichia coli* to ensure our engineered bacteria could survive the low temperatures they would face during implementation in wastewater or well systems. Naturally, these bacteria have an ideal growth temperature of 37°C, which is much warmer than the temperatures they would actually encounter, ranging from 11°C to 14°C, with wells running slightly warmer (1°C) for every 30-55 m in Oregon specifically . Directed evolution was chosen to accomplish this as it's a well established technique for improving growth conditions at lower, with the advantage of not directly altering genetics or introducing stressors [3]. Outside of temperature as a stressor. this allowed for no new additional proteins to be added or knockout genes. Which creates downstream opportunities to add novel proteins.

## Design

Our experiential design was quite straightforward, growing the *Escherichia coli* at decreasing temperatures, selecting for the bacteria that were still able to grow despite the sub-optimal conditions. This method relies on many rounds of iteration, such that the many generations of *Escherichia coli* will slowly adapt to the lowering temperature.

To start off the experiment, a T7 BL21(DE3) *Escherichia coli* lab stock **was streaked on plates as well as made into liquid cultures, then grown at 37°C for three rounds of iteration. These rounds with a stable, ideal temperature were to ensure our baseline bacteria had well established and consistent growth before the true experimentation started. In the following rounds of iteration, plates and cultures were grown in temperatures decreasing by 2°C each round, with three plates and cultures per round. These plates and cultures were always allowed to grow for 16 hours before being temporarily placed in a 4°C fridge. This allowed the bacteria to be harvested during the exponential growth phase, while keeping the experiment timing constant. At exponentially low temperatures the exponential phase shifted.

{% bibliography --file chassis --cited_in_order %}
