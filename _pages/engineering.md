---
layout: page
permalink: /engineering

title: Engineering
subtitle: This is the engineering page.
banner: https://static.igem.wiki/teams/6041/wiki/page-banners/banner-freezer.avif
---

This page outlines the DBTL cycles and data for some aspects of the project. For background information on our project modules, please refer to the corresponding pages ([chassis](/uoregon/chassis), [nitrogen storage](/uoregon/nitrogen-storage), and [flocculation](/uoregon/flocculation)).

# Engineering Objective 1: CphA

## Cycle 1.1

### Design 1.1

Synthesis of cyanophycin requires the expression of cyanophycin synthetase (CphA). We were able to find the well-characterized, effective, and recombinant homolog, TmCphA1. More details about the enzyme are described in the Nitrogen storage module. 

Now that an appropriate homolog had been found, designing the plasmid that TmCphA1 will reside was the next step. A pET21(+) expression vector from Twist was used because its well-characterized, includes a T7 expression system, and has a C-terminal HIS-tag. A C-terminal HIS-tag was chosen, opposed to an N-terminal one, in order to prevent folding interference with the protein's N domain. The N-terminus is where the polymer-binding domain resides, so sticking at HIS-tag here risks interference with the binding surface {% cite sharonCrypticThirdActive2022 --file engineering%}. This is especially relevant for TmCphA1 due to the protein's primer-independent behavior; TmCphA1 requires a small segment of cyanophycin (β-Asp-Arg) to begin the synthesis of a fully constructed cyanophycin polymer. We wouldn't want to risk compromising a functional feature that TmCphA1 can't work around. On the other hand, a C-terminal tag sits just beyond the protein's M domain, being analogous to the bacterial cell-wall ligase domain that has been shown to have negligible loss of function when HIS-tagged {% cite sharonStructuresFunctionAmino2021 --file engineering%}. Salis Lab was used to optimize a supplemented RBS. 

{% include figure.html
url="/uoregon/assets/svg_figures/engineering/engineering_TmCphA1_pET21.svg"
caption="Plasmid figure 1: TmCphA coding sequence embedded in a pET21(+) vector provided by Twist expression vectors."
alttext="Plasmid figure 1: TmCphA coding sequence embedded in a pET21(+) vector provided by Twist expression vectors."
label="plasmid1"
%} 

To first validate that TmCphA1 can express, the protein was purified via an IMAC purification protocol, which relies on the protein having a HIS-tag attached to it. A denaturing SDS-PAGE gel was used to quantify the purified protein's molecular weight (kDa). It is expected that the dyeing and heating step of an SDS-PAGE gel protocol will break the 400kDa TmCphA1 into its four, 100 kDa monomers—creating a single band at 100 kDa. 

The next step is to ensure that the TmCphA1 protein can express in our cells properly. Because our vector and strain are different from that of Swain et al.{% cite Swain et al. 2023 --file engineering%}, it is important to optimize protein expression conditions ourselves. Factors such as temperature of incubation, IPTG amount, and time expressing were differed between samples. 12 smaller samples were employed because this initial experiment is for expression optimization, not making a supply of the TmCphA1 protein. Refer to the *CphA 5mL expression conditions* for sample details and a procedure. 

### Build 1.1

Making a stock of the TmCphA1 plasmid required electroporation into 10-Beta E. coli cells, growing it up in LB broth, and the purifying it via miniprep. See *TmCphA1 stock protocol* for more details.

Purified TmCphA1 plasmid was transformed into T7 express cells and grown in LB broth until a target OD600 of 0.5-0.6. At this point in the cells' log growth phase, appropriate levels of IPTG were supplemented to the liquid media. Details on each sample's conditions, including incubation temperature, IPTG amount, and incubation duration can be found in the *CphA 5mL expression conditions protocol*. Cell pellets were collected after each sample's expression time and stored in the -20 freezer for a subsequent IMAC protein purification. 

### Test 1.1

To test the size of the 8104 bp CphA plasmid, a few colonies were sequenced to precisely determine our plasmid is present and identical to our designed version.  Sequencing of the purified TmCphA1 plasmid was done via Plasmidsaurus. Results showed a 100% pairwise match and the target base pair count of 8104 bp *TmCphA1 stock protocol*. 

The IMAC protein purification protocol, provided by Russel McLoughlin, was used to purify TmCphA1 in order to test expression levels via an SDS-PAGE protein gel. See the protein purification & SDS-PAGE protocol for more details.

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineering-se2-cpha-front.avif"
caption="Lysed cell and elution buffer fractions for samples 1,3,4, and 14. Samples 3 and 4 can be seen at the 100kDa target can be seen in the elution buffer fraction."
alttext="Results from an SDS-PAGE gel that show two bands at 100 kilodaltons."
label="Samples 1, 3, 4, and 14."
%}

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineering-se5-cphaopt.avif"
caption="Lysed cell and elution buffer fraction of samples 7, 8, and 9. One band can be seen for sample 8."
alttext="DESCRIPTION_FOR_PEOPLE_WHO_USE_SCREEN_READERS"
label="Samples 7, 8, and 9"
%}

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineering-se6-obj-4.avif"
caption="Lysed cell and elution buffer fraction of samples 10, 11, 12, and 13. No bands at 100 kDa can be seen for the elution buffer fration."
alttext="Lysed cell and elution buffer fraction of samples 10, 11, 12, and 13. No bands at 100 kDa can be seen for the elution buffer fration."
label="Samples 10, 11, 12, and 13"
%}

### Learn 1.1

It was verified that the TmCphA1-pET21(+) plasmid matched the original design [*TmCphA1 stock protocol]*(/uoregon/protocols#protocol-tmcpha-stock-protocol). 

Results of protein expression and purification show that the target bands of 100kDa are present for most lysed cell samples. Samples 4 and 8 (see *CphA 5mL expression conditions - cycle 1.1*) show target bands. It appears that—from our range of variability—growing cells at 30 C for 4 hr, with the addition of either 1mM or 0.1 mM IPTG prove to be optimal for CphA expression. Using these exact conditions, a larger liquid culture can be made with the goal of purifying a larger quantity of TmCphA1. Now, we can more easily ensure a TmCphA1 supply without wasting lab supplies.

## Cycle 1.2

### Design 1.2

Now that we know the condition for which TmCphA1 grows most optimally, a 50 mL liquid culture can be grown with exactly the optimal conditions of 30 C incubation for 4 hr, after 1mM IPTG induction. 

### Build 1.2

A starter culture from a TmCphA1 plasmid glycerol stock was made and diluted into the larger, 50 mL LB culture. 1mM IPTG (500 uL) was supplemented at 0.5 OD600 and growth was carried out for 4hr at 30 C. cell pellets were collected and stored in the -20 freezer for subsequent protein purification. See *CphA 50mL expression conditions* for more details.

### Test 1.2

The same IMAC protein purification protocol was used, and results are shown below. A buffer exchange was completed using the EB fraction, and the resulting protein sample was used for a Bradford Assay. The Bradford Assay revealed that TmCphA1 has a concentration of 2505.78 ug/mL. *Bradford assay protocol*.

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/cpha-50ml-gel.avif"
caption="SDS-PAGE gel results of the TmCphA1 protein with a band at 100 kDa"
alttext="SDS-PAGE gel results of the TmCphA1 protein with a band at 100 kilodaltons"
label="TmCphA1_50mL"
%}

### Learn 1.2

A band from the EB fraction can be seen around 100kDa, our expected protein size. The high concentration of 2505.78 ug/mL is likely inaccurate due to the standard protein ladder used only ranging up to ~2000 ug/mL. Anything over ~2000 ug/mL would prove to be inaccurate. However, this protein sample was used for an in-vitro test, which doesn't require accurate protein concentrations. It simply needs any amount of TmCphA1. 

# Engineering Objective 2: Cyanophycin

## Cycle 2.1

### Design 2.1

Synthesizing cyanophycin will first be verified via it's ability to precipitate out of solution during the cyanophycin purification process. A set of conditions were made with the purpose of figuring out which condition produces the most cyanophycin. Similar to the condition setup for the TmCphA expression cultures, these varied in expression temperature, IPTG amount, and time expressed. 

### Build & Test 2.1

TmCphA1 plasmid cells were plucked and grown in Terrific Broth (TB) for 48 hr each, with varying amounts of IPTG. Cell pellets were collected and stored in the -20 freezer for the purification step. See *Cyanophycin expression conditions* for more details.

A cyanophycin purification protocol was adapted from {% cite swainHeterologousProductionCyanophycin2023 --file engineering%}. The protocol takes advantage of the fact that cyanophycin is insoluble at neutral pH, so we're aiming to collect a pellet after HCl and NaOH have been added *Cyanophycin purification*. 

### Learn 2.1

Following the addition of HCl, the cell pellets weren't able to dissolve effectively. Furthermore, the insoluble fraction of cyanophycin wasn't able to precipitate out of solution following neutralization via NaOH. The small 5mL cultures could have contributed to the lack of cyanophycin seen. A pH reader was not used during the addition of NaOH, so there was no accurate way of determining when the solution was neutralized. Moving forward, cyanophycin will be grown in larger liquid cultures and a pH reader will be used to accurately determine at what point the solution will neutralize.

## Cycle 2.2

### Design 2.2

During the previous cyanophycin purification process, there was a lack of cyanophycin that precipitated out of solution. Now, 50 mL liquid cultures were used instead of the previous 5mL liquid cultures. Liquid cultures were grown for 48 hr at 30 C, following induction with 1mM IPTG. These conditions were decided based on both Swain et al. {% cite swainHeterologousProductionCyanophycin2023 --file engineering%} and the resulting optimized conditions seen from the TmCphA1 experiment. During the addition of NaOH, a pH reader was be used so that the amount of NaOH added can be adjusted for reaching neutral pH.

### Build & Test 2.2

TmCphA1 plasmid colonies were plucked and grown in Terrific Broth (TB) for 48 hr each, with 1mM IPTG. Cell pellets were collected and stored in the -20 freezer for the purification step. See *Cyanophycin 50mL expression conditions* for more details.

The cyanophycin purification protocol was conducted again, this time accounting for the larger liquid culture (*Cyanophycin purification)*.

### Learn 2.2

Following the addition of NaOH, and therefore solution-neutralization, a pellet was able to be collected via centrifugation. Because we know that cyanophycin precipitates out of the solution at neutral pH, this collected fraction is considered to be the insoluble cyanophycin fraction. However, after the addition of ethanol, no pellet was seen—this would have been the soluble fraction of cyanophycin. The soluble fraction of cyanophycin is not needed for our experimental purposes, so no further troubleshooting needs to be done. The resulting insoluble cyanophycin was lyophilized, weighed, and stored in the 4 C fridge for further experimentation. 

# Engineering Objective 3: In-vitro TmCphA functionality test

Expression of TmCphA has been confirmed, but the functionality of it had not. Furthermore, there hasn't been a more rigorous test to see if cyanophycin is actually being created. To fill these discrepancies in our experimental design, we decided to run an in-vitro experiment, using the purified TmCphA1 and cyanophycin from previous experiments. This way, once an SDS-PAGE gel is run on the finished reaction, we can determine if TmCphA1 can effectively synthesize cyanophycin. 

## Cycle 3.1
### Design 3.1

To further characterize the activity of TmCphA1 and production of cyanophycin, an in-vitro test was conducted with an SDS-PAGE gel to follow. Purified TmCphA1 and cyanophycin, from the previous experiments, were used. This version of TmCphA requires a cyanophycin primer (small sample of cyanophycin) because it lacks the cryptic metallopeptidase active site that can produce cyanophycin without a primer {% cite sharonCrypticThirdActive2022 --file engineering%}. Again, a 100kDa band signifies that TmCphA1 is active and expressing. Cyanophycin is expected to be represented as a smear around 25 kDa on the gel, as cyanophycin is considered polydisperse {% cite sharonStructuresFunctionAmino2021 --file engineering%}, {% cite swainHeterologousProductionCyanophycin2023 --file engineering%}. We'll also be able to determine the amount of reagents that will synthesize the most amount of cyanophycin, if any. 

A protocol was adapted from Swain et al. {% cite swainHeterologousProductionCyanophycin2023 --file engineering%} and the reagent details are in the In-vitro CphA activity assay protocol.

### Build 3.1

Four samples reactions were made according to the in-vitro CphA activity assay protocol. Reagents were compiled in their respective tubes. A simple incubation reaction was performed to allow purified TmCphA1 to synthesize cyanophycin, using the supplemented cyanophycin primer to start the reaction.

### Test 3.1

Following the in-vitro reaction, an SDS-PAGE gel was performed to test for the correct molecular weights of both CphA and cyanophycin (Protein purification & SDS-PAGE gel).

### Learn 3.1

The SDS-PAGE gel showed correctly sized bands at 100 kDa for each sample that contained TmCphA1 (first three lanes). However, no samples showed any smear around 25 kDa, signifying that cyanophycin is not present.

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineering-in-vitro-cpha1.avif"
caption="First iteration of the CphA in-vitro test. All samples except CphA- showed bands at 100kDa, as expected. No smear aorund 25kDa was seen for any sample, signifying that cyanophycin could not be seen."
alttext="First iteration of the CphA in-vitro test. All samples except CphA- showed bands at 100 kilodaltons, as expected. No smear around 25 kilodaltons was seen for any sample, signifying that cyanophycin could not be seen."
label="CphA in-vitro test 1"
%}


## Cycle 3.2
### Design 3.2

More cyanophycin was purified, this time with a more accurate pH measuremnt and NaOH addition. Another set of conditions for the in-vitro test were implemented, with the goal of visualizing cyanophycin on the SDS-PAGE gel—some of which altered the incubation temperature and length, supplemented excess cyanophycin and CphA, added β-mercaptoethanol, or provided various negative controls. A more detailed reaction setup can be seen in (In-vitro CphA activity assay).

### Build & Test 3.2

Reagents were all added to their respective 200 uL tubes and incubated for appropriate times. Following the in-vitro reaction, an SDS-PAGE gel was performed to test for the correct molecular weights of both CphA and cyanophycin (Protein purification & SDS-PAGE gel).

### Learn 3.2

As expected, and shown in cycle 3.1, 100kDa bands were seen throughout all samples—except the "no CphA" condition—signifying CphA is present. Yet again, the polydisperse cyanophycin could not be seen, as there was no 25 kDa smear. 

{% include figure.html
    url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineering-in-vitro3-2.avif"
    caption="Second iteration of the CphA in-vitro test. All samples that included CphA showed bands at 100kDa, as expected. No smear around 25kDa was seen for any sample, signifying that cyanophycin could not be seen."
    alttext="Second iteration of the CphA in-vitro test. All samples except 'no CphA' showed bands at 100kDa, as expected. No smear around 25kDa was seen for any samples, signifying that cyanophycin could not be seen."
    label="CphA-in-vitro-test2"
%}

We deduced that an absence of a 25 kDa smear on the gel could be a result of either (1) cyanophycin not being produced in the expression cultures prior to purification, (2) cyanophycin not being able to purify properly, (3) a faulty in-vitro reaction setup, (4) 1 M HCl being the wrong reagent to resuspend insoluble cyanophycin in, or (5) a combination of these. 

# Engineering Objective 4: Ammonium biosensor

## Cycle 4.1
### Design 4.1

Xiao et al, 2017 {% cite xiaoDevelopingGeneticallyEncoded2017 --file engineering%} developed an ammonium biosensor that is capable of regulating the expression of CphA via ammonium. The system takes advantage of two enzymes involved in the negative regulation of glutamine synthesis, GlnR and GlnA. *Lactococcus* natively uses GlnA, a glutamine synthetase that converts ammonium and glutamate into glutamine, At high enough ammonium concentration. Once enough glutamine has accumulated, it binds GlnA and acts as a chaperone that stabilizes the repressor, GlnR. Now, the GlnR-A complex is able to inhibit its own downstream genes via the glnR-sensitive promoter.

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineering-glnra-schematic.avif"
caption="Figure 1: General schematic of the GlnRA system with YFP as the output. glnA and glnR are regulated by a synthetic promoter, Plib. YFP is regulated by a synthetic promoter, PglnR, that triggers gene expression in the presence of the GlnA:GlnR complex, in the presence of high enough ammonium."
alttext="Figure 1: General schematic of the GlnRA system with YFP as the output. glnA and glnR are regulated by a synthetic promoter, Plib. YFP is regulated by a synthetic promoter, PglnR, that triggers gene expression in the presence of the GlnA:GlnR complex, in the presence of high enough ammonium."
label="GlnRA_schematic"
%}

They developed a library of promoters that regulate GlnR-A, YFP, RFP, and TetR expression. The biosensor was able to be transferred to other species effectively, namely E. coli. Once a few promoter candidates were filtered out from their larger libraries, Xiao et al. {% cite xiaoDevelopingGeneticallyEncoded2017 --file engineering%} applied their established ammonium biosensor to control cyanophycin biosynthesis. To accomplish this, YFP was replaced by the TetR repressor and a second plasmid regulated CphA expression via a PTet promoter (repressed by TetR). Now, when enough ammonium is present, transcription of TetR is turned off, so CphA is free to be transcribed.

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/nh4-sensor-cpha.avif"
caption="Schematic of the ammonium biosensor regulating CphA expression via the TetR sensitive promoter, pTet (Zhang et al.)."
alttext="Second iteration of the CphA in-vitro test. All samples except 'no CphA' showed bands at 100 kilodaltons, as expected. No smear around 25 kilodaltons was seen for any sample, signifying that cyanophycin could not be seen."
label="CphA in-vitro test 2"
%}

Sequences for GlnR, GlnA, PglnR, and Plib are provided in the paper's supporting information. A specific set of vectors were used to construct each of the plasmids. However, these vectors were not used because (1) the sequences could not be found in the paper nor anywhere online, (2) none of the authors responded to our request of these plasmid sequences, and (3) their goal of making this sensor for multiple species likely is a main reason for the use of multiple different vectors. Our goal is to apply this sensor to our system in E. coli, so our experiment only needs to only make use of the sequences mentioned before. 

#### Fluorescent Readout

As a preliminary test to ensure we can replicate the fundamental function of the biosensor, GFP will be the output. Varying levels of ammonium (and other nitrogen sources) will be supplemented, and fluorescence can be measured to determine the effectiveness of GlnR, GlnA, Plib, and PglnR. Once this is validated, GFP will be replaced by TetR, and a Ptet promoter will be placed upstream of our TmCphA1 CDS. 

A pTwist Kan Medium copy vector was used as the backbone when designing this version of the biosensor. GlnR and glnA were placed sequentially, under the constitutive plib promoter, designed by Xiao et al, 2017{% cite xiaoDevelopingGeneticallyEncoded2017  --file nitrogen-storage %}. Salis labs was used to design two optimized RBS sequences for glnR and glnA. GFP expression was designed to be run in the antisense direction, so in the opposite direction of the glnR and glnA module. PglnR2 is the ammonium-sensitive promoter, which was placed upstream of GFP and the Salis lab-optimized RBS. The BBa_B0012 Terminator was placed at the end of GlnR, GlnA, and GFP

{% include figure.html
url="/uoregon/assets/svg_figures/nitrogen-storage/nitrogen-storage_GlnRA-GFP_insert-in-pTwist-Kan-Medium-Copy.svg"
caption="Benchilng plasmid design for the ammonium biosensor with a GFP output."
alttext="Benchilng plasmid design for the ammonium biosensor with a GFP output."
label="Ammonium-sensor-plasmid-GFP-output"
%}

#### RT-qPCR

The paper used an SDS-PAGE gel to quantify and compare cyanophycin yield between conditions (e.g.  biosensor absent versus biosensor present). The ImageJ software was used to measure the opacity of each 25 kDa smear of cyanophycin. However, this method of quantification proves to be ineffective when attempting to compare conditions—it would only be sufficient if the test's goal were to find if cyanophycin can be synthesized at all.

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineering-xiao-cyphy-gel.avif"
caption="Xiao et al. measuring cyanophycin output as a result of the ammonium biosensor."
alttext="Xiao et al. measuring cyanophycin output as a result of the ammonium biosensor."
label="Xiao et al. measuring cyanophycin"
%}

The paper used an SDS-PAGE gel to quantify and compare cyanophycin yield between conditions (e.g.  biosensor absent versus biosensor present). The ImageJ software was used to measure the opacity of each 25 kDa smear of cyanophycin. However, this method of quantification proves to be ineffective when attempting to compare conditions—it would only be sufficient if the test's goal were to find if cyanophycin can be synthesized at all.

After consulting with our mentor, Calin Plesa, we have been advised to use a more robust method. To more accurately quantify the biosensor's effectiveness in regulating TmCphA1 expression, and therefore cyanophycin synthesis, RT-qPCR can be implemented. RT-qPCR will be used to quantify the amount of TmCphA1 that has been transcribed. A reverse transcriptase is first used to reverse transcribe the RNA of TmCPhA1, converting it to DNA. This DNA can be amplified with designed primers and measurement via a dye or probe based-approach {% cite BongBriefguideRTqPCR  --file nitrogen-storage %} {% cite AdamsBeginnerguidetoRTqPCR --file nitrogen-storage %}. Although this will not directly give us a way of determining how much cyanophycin yield can result, TmCphA1 transcription is a beneficial first way of figuring out how efficient and sensitive the biosensor is at producing TmCphA1.

A similar design structure was used for constructing the plasmid meant for TetR expression. Again, this would allow for de-repression of the pTet promoter that regulates TmCphA1 expression. Therefore, as ammonium levels increase, TetR expression will decrease, and TmCphA1 expression can increase.

{% include figure.html
url="/uoregon/assets/svg_figures/nitrogen-storage/nitrogen-storage_GlnRA-TetR_insert-in-pTwist-Kan-Medium-Copy.svg"
caption="Benchilng plasmid design for the ammonium biosensor with a TetR output."
alttext="Benchilng plasmid design for the ammonium biosensor with a TetR output."
label="Ammonium-sensor-plasmid-TetR-output"
%}

### Build 4.1

Our first objective is to measure GFP output as a result of varying ammonium levels. The practical setup in the end has a well-plate filled with cell samples and ammonium media, so a plate reader can detect GFP and OD levels as expression occurs. To make a stock of our cells, we need to grow up our cells (with the biosensor plasmid) in an LB media starter culture. This starter culture is then diluted into an M9 minimal media with supplemented ammonium. This is so our cells have an equal amount of repressed GFP going into the plate reader recording. A nitrogen source is also needed for grow to occur at all. After growing, the cells are washed free of the ammonium and resuspended in nitrogen-free M9. Now, the cells have been set to a "baseline" level of GFP expression and are ready for the plate-reader; the ammonium supplementation will be the only thing that should control GFP expression here on out. One part cells and one part M9 media (with varying ammonium levels). More details regarding experimental procedure can be seen in ammonium biosensor GFP.

### Test 4.1

A fluorescent plate reader was used to measure the GFP output and OD over a 16 hr time course. Readings were taken every 15 minutes. It was expected that as ammonium concentration rises, GFP output will fall. The first two rows of the plate reader are replicates of each other. Samples with 0 mM, 0.01 mM, and 10 mM were seen to have the highest measured GFP fluorescence throughout the time courrse. The first replicate with 0 mM did not show high levels of GFP. 

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineering-glnra-gfp-exp3-gfpovertime.avif"
caption="GFP fluorescence readings over 16 hr of incubation. " 
alttext="GFP fluorescence readings over 16 hr of incubation."
label="Fluorescence readings from GFP ammonium biosensor"
%} 

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineering-glnra-gfp-exp3-gfpchart.avif"
caption="Fluorescence readings at 0 hr. Ammonium levels rise from left to right. The first two rows have cells, and the first 7 columns of row 3 have cells." 
alttext="Fluorescence readings at 0 hr. Ammonium levels rise from left to right. The first two rows have cells, and the first 7 columns of row 3 have cells."
label="Fluorescence readings at time point 0 hr."
%}

% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineering-gfpod-glnra-gfp-exp3-time0.avif"
caption="Fluorescence readings at 0 hr standardized to each sample's respective OD measurements."
alttext="Fluorescence readings at 0 hr standardized to each sample's respective OD measurements."
label="Time 0 hr fluorescence / OD"
%}

% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineering-gfpod-glnra-gfp-exp3-time16.avif"
caption="Fluorescence readings at 16 hr standardized to each sample's respective OD measurements."
alttext="Fluorescence readings at 16 hr standardized to each sample's respective OD measurements."
label="Time 16 hr fluorescence / OD"
%}

### Learn 4.1

There are consistently high fluorescent readings for two low ammonium-concentrated samples. However, for one of the replicates at 0 mM ammonium, this is not the case. Furthermore, there is a sample at 10 mM ammonium that shows higher GFP levels than samples that were administered less ammonium. Although there is not a perfectly linear decrease of GFP output versus ammonium increase, our results give us a justification for repeating the experiment. For further experiments, we plan to alter various experimental conditions, add certain controls, and potentially re-design our plasmid and GlnRA-sensitive promoter. Cell and ammonium samples will be made fresh and added to wells immediately after making them. A positive constitutive GFP control needs to be added to decide if GFP output is a result of ammonium interacting with the biosensor or cell viability itself.  It could be that our proteins, GlnR and GlnA, are simply not expressing effectively. To validate their expression, a protein purification procedure needs to be implemented. The GlnRA-sensitive promoter could also prove to be ineffective in our plasmid or strain used. A library of promoters can be designed, built, and tested to account for this possibility. 

Many more trials and iterations need to occur before declaring the absolute efficacy of this sensor. For now, our design and collected data are enough to build off of. 

# Bibliography

{% bibliography --file engineering --cited_in_order %}

