---
layout: page
permalink: /engineering

title: Engineering
subtitle: This is the engineering page.
banner: https://static.igem.wiki/teams/6041/wiki/placeholders/petunias.avif
---

# Cycle 1: CphA

## Background

Storing the incoming nitrate in a stable and harvestable form required utilizing the nitrogen content from nitrate, without leaving it in a form that can be swallowed up by various metabolic pathways. Nitrate enters the cell and is eventually converted into various reduced forms such as nitrite, ammonium, and various amino acids ({% cite vanheeswijkNitrogenAssimilationEscherichia2013 --file engineering%} {% cite bessonNitriteReductionBacteria2022 --file engineering%} {% cite maNitrogenRecoveryDissimilatory2025 --file engineering%}). Our goal is to create a usable fertilizer, which requires an inert form of nitrogen to reside intracellularly long enough for harvesting and purification to occur. Simply harvesting the intracellular content wouldn’t provide an effective and robust fertilizer. 

Cyanobacteria utilize a nitrogen-storage polymer, cyanophycin, to store excess nitrogen content for the long term. Cyanophycin is made up of a chain of 80-400 arginine and aspartate dipeptides. No enzyme or protease interacts with it, except cyanophycinase. Cyanophycinase is involved in the first step of cyanophycin catabolism, and is responsible for cleaving the polymer into its individual β-Asp-Arg dipeptides {% cite sharonStructuresFunctionAmino2021 --file engineering%} {% cite duEnhancedCyanophycinProduction2017 --file engineering%} {% cite swainHeterologousProductionCyanophycin2023 --file engineering%}) Point being, cyanophycin provided a way for our cells to maintain the excess nitrogen content and a fertilizer alternative. 

### Design 1.1

Synthesis of cyanophycin requires the expression of cyanophycin synthetase (CphA). We were able to find the well-characterized, effective, and recombinant homolog, TmCphA1. More details about the enzyme are described in the [nitrogen storage module](/uoregon/nitrogen-storage).

Now that an appropriate homolog had been found, designing the plasmid that TmCphA1 will reside was the next step. A pET21(+) expression vector from Twist was used because its well-characterized, includes a T7 expression system, and has a C-terminal HIS-tag. A C-terminal HIS-tag was chosen, opposed to an N-terminal one, in order to prevent folding interference with the protein’s N domain. The N-terminus is where the polymer-binding domain resides, so sticking at HIS-tag here risks interference with the binding surface {% cite sharonCrypticThirdActive2022 --file engineering%}. This is especially relevant for TmCphA1 due to the protein’s primer-independent behavior; TmCphA1 requires a small segment of cyanophycin (β-Asp-Arg) to begin the synthesis of a fully constructed cyanophycin polymer. We wouldn’t want to risk compromising a functional feature that TmCphA1 can’t work around. On the other hand, a C-terminal tag sits just beyond the protein’s M domain, being analogous to the bacterial cell-wall ligase domain that has been shown to have negligible loss of function when HIS-tagged {% cite sharonStructuresFunctionAmino2021 --file engineering%}. Salis Lab was used to optimize a supplemented RBS. 

{% include figure.html
url="/uoregon/assets/svg_figures/engineering/engineering_TmCphA1_pET21.svg"
caption="Plasmid figure 1: TmCphA coding sequence embedded in a pET21(+) vector provided by Twist expression vectors."
alttext="Plasmid figure 1: TmCphA coding sequence embedded in a pET21(+) vector provided by Twist expression vectors."
label="plasmid1"
%} 

To first validate that TmCphA1 can express, the protein was purified via an IMAC purification protocol, which relies on the protein having a HIS-tag attached to it. A denaturing SDS-PAGE gel was used to quantify the purified protein’s molecular weight (kDa). It is expected that the dyeing and heating step of an SDS-PAGE gel protocol will break the 400kDa TmCphA1 into its four, 100 kDa monomers—creating a single band at 100 kDa. 

The next step is to ensure that the TmCphA1 protein can express in our cells properly. Because our vector and strain are different from that of Swain et al.{% cite Swain et al. 2023 --file engineering%}, it is important to optimize protein expression conditions ourselves. Factors such as temperature of incubation, IPTG amount, and time expressing were differed between samples. 12 smaller samples were employed because this initial experiment is for expression optimization, not making a supply of the TmCphA1 protein. Refer to the *CphA 5mL expression conditions* for sample details and a procedure. 

### Build 1.1

Making a stock of the TmCphA1 plasmid required electroporation into 10-Beta E. coli cells, growing it up in LB broth, and the purifying it via miniprep. See *TmCphA1 stock protocol* for more details.

Purified TmCphA1 plasmid was transformed into T7 express cells and grown in LB broth until a target OD600 of 0.5-0.6. At this point in the cells’ log growth phase, appropriate levels of IPTG were supplemented to the liquid media. Details on each sample’s conditions, including incubation temperature, IPTG amount, and incubation duration can be found in the *CphA 5mL expression conditions protocol*. Cell pellets were collected after each sample’s expression time and stored in the -20 freezer for a subsequent IMAC protein purification. 

### Test 1.1

To test the size of the 8104 bp CphA plasmid, a few colonies were sequenced to precisely determine our plasmid is present and identical to our designed version.  Sequencing of the purified TmCphA1 plasmid was done via Plasmidsaurus. Results showed a 100% pairwise match and the target base pair count of 8104 bp *TmCphA1 stock protocol*. 

The IMAC protein purification protocol, provided by Russel McLoughlin, was used to purify TmCphA1 in order to test expression levels via an SDS-PAGE protein gel. See the protein purification & SDS-PAGE protocol for more details.

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineering-se2-cpha-front-labeled.avif"
caption="Lysed cell and elution buffer fractions for samples 1,3,4, and 14. Samples 3 and 4 can be seen at the 100kDa target can be seen in the elution buffer fraction."
alttext="Results from an SDS-PAGE gel that show two bands at 100 kilodaltons."
label="Samples 1, 3, 4, and 14."
%}

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineering-se5-cphaopt-labeled.avif"
caption="Lysed cell and elution buffer fraction of samples 7, 8, and 9. One band can be seen for sample 8."
alttext="DESCRIPTION_FOR_PEOPLE_WHO_USE_SCREEN_READERS"
label="Samples 7, 8, and 9"
%}


{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineering-se6-obj3-labeled.avif"
caption="Lysed cell and elution buffer fraction of samples 10, 11, 12, and 13. No bands at 100 kDa can be seen for the elution buffer fration."
alttext="Lysed cell and elution buffer fraction of samples 10, 11, 12, and 13. No bands at 100 kDa can be seen for the elution buffer fration."
label="Samples 10, 11, 12, and 13"
%}

### Learn 1.1

It was verified that the TmCphA1-pET21(+) plasmid matched the original design [*TmCphA1 stock protocol*](/uoregon/protocols#protocol-tmcpha-stock-protocol). 

Results of protein expression and purification show that the target bands of 100kDa are present for most lysed cell samples. Samples 4 and 8 (see *CphA 5mL expression conditions - cycle 1.1*) show target bands. It appears that—from our range of variability—growing cells at 30 C for 4 hr, with the addition of either 1mM or 0.1 mM IPTG prove to be optimal for CphA expression. Using these exact conditions, a larger liquid culture can be made with the goal of purifying a larger quantity of TmCphA1. Now, we can more easily ensure a TmCphA1 supply without wasting lab supplies.

## 1.2

### Design 1.2

Now that we know the condition for which TmCphA1 grows most optimally, a 50 mL liquid culture can be grown with exactly the optimal conditions of 30 C incubation for 4 hr, after 1mM IPTG induction. 

### Build 1.2

A starter culture from a TmCphA1 plasmid glycerol stock was made and diluted into the larger, 50 mL LB culture. 1mM IPTG (500 uL) was supplemented at 0.5 OD600 and growth was carried out for 4hr at 30 C. cell pellets were collected and stored in the -20 freezer for subsequent protein purification. See *CphA 50mL expression conditions* for more details.

### Test 1.2

The same IMAC protein purification protocol was used, and results are shown below. A buffer exchange was completed using the EB fraction, and the resulting protein sample was used for a Bradford Assay. The Bradford Assay revealed that TmCphA1 has a concentration of 2505.78 ug/mL. *Bradford assay protocol*.

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineer-cpha-50ml-gel.avif"
caption="SDS-PAGE gel results of the TmCphA1 protein with a band at 100 kDa"
alttext="SDS-PAGE gel results of the TmCphA1 protein with a band at 100 kilodaltons"
label="TmCphA1_50mL"
%}

### Learn 1.2

A band from the EB fraction can be seen around 100kDa, our expected protein size. The high concentration of 2505.78 ug/mL is likely inaccurate due to the standard protein ladder used only ranging up to ~2000 ug/mL. Anything over ~2000 ug/mL would prove to be inaccurate. However, this protein sample was used for an in-vitro test, which doesn’t require accurate protein concentrations. It simply needs any amount of TmCphA1. 

# Cycle 2: Cyanophycin

## 2.1

### Design 2.1

Synthesizing cyanophycin will first be verified via it’s ability to precipitate out of solution during the cyanophycin purification process. A set of conditions were made with the purpose of figuring out which condition produces the most cyanophycin. Similar to the condition setup for the TmCphA expression cultures, these varied in expression temperature, IPTG amount, and time expressed. 

### Build & Test 2.1

TmCphA1 plasmid cells were plucked and grown in Terrific Broth (TB) for 48 hr each, with varying amounts of IPTG. Cell pellets were collected and stored in the -20 freezer for the purification step. See *Cyanophycin expression conditions* for more details.

A cyanophycin purification protocol was adapted from {% cite swainHeterologousProductionCyanophycin2023 --file engineering%}. The protocol takes advantage of the fact that cyanophycin is insoluble at neutral pH, so we’re aiming to collect a pellet after HCl and NaOH have been added *Cyanophycin purification*. 

### Learn 2.1

Following the addition of HCl, the cell pellets weren’t able to dissolve effectively. Furthermore, the insoluble fraction of cyanophycin wasn’t able to precipitate out of solution following neutralization via NaOH. The small 5mL cultures could have contributed to the lack of cyanophycin seen. A pH reader was not used during the addition of NaOH, so there was no accurate way of determining when the solution was neutralized. Moving forward, cyanophycin will be grown in larger liquid cultures and a pH reader will be used to accurately determine at what point the solution will neutralize.

## 2.2

### Design 2.2

During the previous cyanophycin purification process, there was a lack of cyanophycin that precipitated out of solution. Now, 50 mL liquid cultures were used instead of the previous 5mL liquid cultures. Liquid cultures were grown for 48 hr at 30 C, following induction with 1mM IPTG. These conditions were decided based on both Swain et al. {% cite swainHeterologousProductionCyanophycin2023 --file engineering%} and the resulting optimized conditions seen from the TmCphA1 experiment. During the addition of NaOH, a pH reader was be used so that the amount of NaOH added can be adjusted for reaching neutral pH.

### Build & Test 2.2

TmCphA1 plasmid colonies were plucked and grown in Terrific Broth (TB) for 48 hr each, with 1mM IPTG. Cell pellets were collected and stored in the -20 freezer for the purification step. See *Cyanophycin 50mL expression conditions* for more details.

The cyanophycin purification protocol was conducted again, this time accounting for the larger liquid culture (*Cyanophycin purification)*.

### Learn 2.2

Following the addition of NaOH, and therefore solution-neutralization, a pellet was able to be collected via centrifugation. Because we know that cyanophycin precipitates out of the solution at neutral pH, this collected fraction is considered to be the insoluble cyanophycin fraction. However, after the addition of ethanol, no pellet was seen—this would have been the soluble fraction of cyanophycin. The soluble fraction of cyanophycin is not needed for our experimental purposes, so no further troubleshooting needs to be done. The resulting insoluble cyanophycin was lyophilized, weighed, and stored in the 4 C fridge for further experimentation. 

# Cycle 3: *In-vitro* TmCphA functionality test

Expression of TmCphA has been confirmed, but the functionality of it had not. Furthermore, there hasn’t been a more rigorous test to see if cyanophycin is actually being created. To fill these discrepancies in our experimental design, we decided to run an in-vitro experiment, using the purified TmCphA1 and cyanophycin from previous experiments. This way, once an SDS-PAGE gel is run on the finished reaction, we can determine if TmCphA1 can effectively synthesize cyanophycin. 

## Design 3.1

To further characterize the activity of TmCphA1 and production of cyanophycin, an in-vitro test was conducted with an SDS-PAGE gel to follow. Purified TmCphA1 and cyanophycin, from the previous experiments, were used. This version of TmCphA requires a cyanophycin primer (small sample of cyanophycin) because it lacks the cryptic metallopeptidase active site that can produce cyanophycin without a primer {% cite sharonCrypticThirdActive2022 --file engineering%} Again, a 100kDa band signifies that TmCphA1 is active and expressing. Cyanophycin is expected to be represented as a smear around 25 kDa on the gel, as cyanophycin is considered polydisperse {% cite sharonStructuresFunctionAmino2021 --file engineering%}, {% cite swainHeterologousProductionCyanophycin2023 --file engineering%}. We’ll also be able to determine the amount of reagents that will synthesize the most amount of cyanophycin, if any. 

A protocol was adapted from Swain et al. {% cite swainHeterologousProductionCyanophycin2023 --file engineering%} and the reagent details are in the In-vitro CphA activity assay protocol.

## Build 3.1

Four samples reactions were made according to the in-vitro CphA activity assay protocol. Reagents were compiled in their respective tubes. A simple incubation reaction was performed to allow purified TmCphA1 to synthesize cyanophycin, using the supplemented cyanophycin primer to start the reaction.

## Test 3.1

Following the in-vitro reaction, an SDS-PAGE gel was performed to test for the correct molecular weights of both CphA and cyanophycin (Protein purification & SDS-PAGE gel).

## Learn 3.1

The SDS-PAGE gel showed correctly sized bands at 100 kDa for each sample that contained TmCphA1 (first three lanes). However, no samples showed any smear around 25 kDa, signifying that cyanophycin is not present.

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineering-in-vitro-cpha1.avif"
caption="First iteration of the CphA in-vitro test. All samples except CphA- showed bands at 100kDa, as expected. No smear aorund 25kDa was seen for any sample, signifying that cyanophycin could not be seen."
alttext="First iteration of the CphA in-vitro test. All samples except CphA- showed bands at 100 kilodaltons, as expected. No smear around 25 kilodaltons was seen for any sample, signifying that cyanophycin could not be seen."
label="CphA in-vitro test 1"
%}

## Design 3.2

More cyanophycin was purified, this time with a more accurate pH measuremnt and NaOH addition. Another set of conditions for the in-vitro test were implemented, with the goal of visualizing cyanophycin on the SDS-PAGE gel—some of which altered the incubation temperature and length, supplemented excess cyanophycin and CphA, added β-mercaptoethanol, or provided various negative controls. A more detailed reaction setup can be seen in (In-vitro CphA activity assay).

## Build & Test 3.2

Reagents were all added to their respective 200 uL tubes and incubated for appropriate times. Following the in-vitro reaction, an SDS-PAGE gel was performed to test for the correct molecular weights of both CphA and cyanophycin (Protein purification & SDS-PAGE gel).

## Learn 3.2

As expected, and shown in cycle 3.1, 100kDa bands were seen throughout all samples—except the “no CphA” condition—signifying CphA is present. Yet again, the polydisperse cyanophycin could not be seen, as there was no 25 kDa smear. 

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineering-in-vitro3-2.avif"
caption="Second iteration of the CphA in-vitro test. All samples that included CphA showed bands at 100kDa, as expected. No smear around 25kDa was seen for any sample, signifying that cyanophycin could not be seen."
alttext="Second iteration of the CphA in-vitro test. All samples except “no CphA” showed bands at 100 kilodaltons, as expected. No smear around 25 kilodaltons was seen for any sample, signifying that cyanophycin could not be seen."
label="CphA in-vitro test 2"
%}

We deduced that an absence of a 25 kDa smear on the gel could be a result of either (1) cyanophycin not being produced in the expression cultures prior to purification, (2) cyanophycin not being able to purify properly, (3) a faulty in-vitro reaction setup, (4) 1 M HCl being the wrong reagent to resuspend insoluble cyanophycin in, or (5) a combination of these. 

## Bibliography

{% bibliography --file engineering --cited_in_order %}
