---
layout: page
permalink: /engineering

title: Engineering
subtitle: This is the engineering page.
banner: https://static.igem.wiki/teams/6041/wiki/placeholders/petunias.avif
---

### Engineering introduction

### Module 2 - Storage

- **1st cycle set - CphA plasmid**
    
    ### Design 1
    
    Synthesis of cyanophycin requires the expression of cyanophycin synthetase (CphA). A literature review was conducted to find a CphA coding sequence that is well characterized, produces high amounts of cyanophycin, and could be replicated with our resources. Nannenga et al. (2023) demonstrated that TmCphA1 produced up to 2-fold greater insoluble cyanophycin yields than any other tested CphA1. It also had 10.8-times greater yields than the widely studied CphA1 from Synechocystis sp. PCC6308 (). 
    
    In order to first validate that TmCphA1 can simply express, the plan is to purify the protein via an IMAC purification protocol, which relies on the protein having a HIS-tag attached to it. A denaturing SDS-PAGE gel will then be used to quantify the purified protein’s molecular weight (kDa). It is expected that the dying and heating step of an SDS-PAGE gel protocol will break the 400kDa TmCphA1 into its four, 100kDa monomers—creating a single band at 100kDa. 
    
    When designing the plasmid that TmCphA1 will reside, a pET21(+) expression vector from Twist was used because its well-characterized, includes a T7 expression system, and has a C-terminal HIS-tag. A C-terminal HIS-tag was chosen, opposed to an N-terminal one, in order to prevent folding interference with the protein’s [ ] domain. An RBS was supplemented to the construct (), and the Salis lab RBS calculator was used to optimize expression rates of the open reading frame. 
    
    [insert benchling plasmid construct] 
    
    *description of plasmid & parts*
    
    [link to iGEM registry coding sequence] 
    
    ### Build 1
    
    Making a stock of the TmCphA1 plasmid required electroporation () into 10-Beta E. coli cells, growing it up in LB broth, and the purifying it via miniprep (). 
    
    ### Test 1
    
    To test the size of the 8102 bp CphA plasmid, a gel electrophoresis was run and bands at around the target length. 
    
    [insert gel image] 
    
    A few colonies were sequences to precisely determine our plasmid is present and identical to our designed version. 
    
    [insert plasmidsaurus results/benchling alignment] 
    
    ### Learn 1
    
    It is now verified that the TmCphA1-pET21(+) plasmid matches the original design and can be implemented into 10-Beta cells. Further experiments can now be conducted, such as validating TmCphA1 expression. 
    
- **2nd cycle set - CphA expression & purification**
    - cycle 2.1
        
        ### Design 2.1
        
        We now need to ensure that the TmCphA1 protein can express in our cells appropriately. Because our vector and strain are different from Nennenga et al. (2023), it is important to optimize protein expression conditions ourselves. Factors such as temperature of incubation, IPTG amount, and time expressing were differed between samples. Numerous smaller samples were employed because this initial experiment is for expression optimization, not making a supply of TmCphA1. 
        
        | Sample | Temperature (C) | IPTG amount () | Expression time (hr)  |
        | --- | --- | --- | --- |
        |  |  |  |  |
        |  |  |  |  |
        
        ### Build 2.1
        
        TmCphA1 plasmid was tranformed into T7 express cells and grown in LB broth until a target OD600 of 0.5-0.6. At this poitn in the cells’ log growth phase, appropriate levels of IPTG were supplemented to the liquid media. Cell pellets were collected after each sample’s expression time and stoered in the -20 freezer for a subsequent IMAC protein purification. 
        
        ### Test 2.1
        
        The IMAC protein purification protocol, provided by Russel McSomething, was used to purify TmCphA1 in order to test expression levels via an SDS-PAGE protein gel. See [protocol 2] for more details. 
        
        CHANGE IMAGE FORMAT
        
        ![CphA_gel1_front (2).png](Project%20Engineering/CphA_gel1_front_(2).png)
        
        *SE2 results*
        
        ![CphA_gel1_back.png](Project%20Engineering/CphA_gel1_back.png)
        
        *SE2 results*
        
        ![26.07.30_purCphA_remsamples_imageJ.tif](Project%20Engineering/26.07.30_purCphA_remsamples_imageJ.tif)
        
        *SE5 results*
        
        ![26.08.06_20 (1).tif](Project%20Engineering/26.08.06_20_(1).tif)
        
        *SE6 3rd objective results*
        
        ### Learn 2.1
        
        Results show that the target bands of 100kDa are present for most lysed cell samples. Samples [] show target bands. It appears that—from our range of variability—growing cells at 30 C for 4 hr, with the addition of either 1mM or 0.1 mM IPTG prove to be optimal for CphA expression. Using these exact conditions, a larger liquid culture can be made with the goal of purifying a larger quantity of TmCphA1. Now, we can more easily ensure a TmCphA1 supply without wasting many lab supplies. 
        
    - cycle 2.2
        
        ### Design 2.2
        
        Now that we know the condition for which TmCphA1 grows most optimally, a 50 mL liquid culture can be grown with exactly the optimal conditions of 30 C incubation for 4 hr, post 1mM IPTG (500 uL) induction. 
        
        ### Build 2.2
        
        A starter culture from a TmCphA1 plasmid glycerol stock was made and diluted into the larger, 50 mL LB culture. 1mM IPTG (500 uL) was supplemented at 0.5 OD600 and growth was carried out for 4hr at 30 C. cell pellets were collected and stored in the -20 freezer for subsequent protein purification. See protocol SE6 fourth objective Newerer for further details. 
        
        ### Test 2.2
        
        The IMAC protein purification protocol, provided by Russel McSomething, was used to purify TmCphA1 in order to test expression levels via an SDS-PAGE protein gel. See [protein purifcation] for more details. A buffer exchange was compleeted using the EB fraction, and the resulting protein sample was used for a Bradford Assay. The Bradford Assay revealed that TmCphA1 has a concentration of 2505.78 ug/mL. see google notebook details with details. 
        
        ![26.08.17_50mLCphA_30C_4hr_imageJ (1).tif](Project%20Engineering/26.08.17_50mLCphA_30C_4hr_imageJ_(1).tif)
        
        *SE6 fourth objective results*
        
        ### Learn 2.2
        
        A band from the EB fraction can be seen around 100kDa, our expected protein size. The high concentration of 2505.78 ug/mL is likely inaccurate due to the standard protein ladder used only ranging up to ~2000 ug/mL. Anything over ~2000 ug/mL would prove to be inaccurate. 
        
- **3rd cycle set - cyanophycin synthesis**
    - cycle 3.1
        
        ### **Design 3.1**
        
        Synthesizing cyanophycin will first be verified via it’s ability to precipitate out of solution during the cyanophycin purification process . A set of conditions were made with the purpose of figuring out which condition produces the most cyanophycin
        
        | Sample | Temperature | IPTG amount | Time expressed |
        | --- | --- | --- | --- |
        |  |  |  |  |
        |  |  |  |  |
        |  |  |  |  |
        |  |  |  |  |
        |  |  |  |  |
        |  |  |  |  |
        
        ### **Build & Test 3.1**
        
        TmCphA1 plasmid colonies were plucked and grown in Terrific Broth (TB) for 48 hr each, with varying amounts of IPTG. Cell pellets were collected and stored in the -20 freezer for the purification step. See cyanophycin expression protocol for more details. 
        
        A cyanophycin purification protocol was adapted from [ ]. The protocol takes advantage of the fact that cyanophycin is insoluble at neutral pH, so we’re aiming to collect a pellet after HCl and NaOH have been added. See the cyanophycin purification protocol for more details (SE6 third objective). 
        
        ### **Learn 3.1**
        
        Following the addition of HCl, the cell pellets weren’t able to dissolve effectively. Furthermore, the insoluble fraction of cyanophycin wasn’t able to precipitate out of solution following neutralization via NaOH. The small 5mL cultures could have contributed to the lack of cyanophycin seen. A pH reader was not used during the addition of NaOH, so there was no accurate way of determining when the solution was neutralized. Moving forward, cyanophycin will be grown in larger liquid cultures and a pH reader will be used to accurately determine at what point the solution will neutralize. 
        
    - cycle 3.2
        
        ### Design 3.2
        
        During the cyanophycin purification process, there was a lack of cyanophycin that precipitated out of solution. 50 mL liquid cultures will now be used instead of the previous 5mL liquid cultures. Liquid cultures were grown for 48 hr at 30 C, following induction with 1mM IPTG. These conditions were decided based on both Nennenga et al. (2023) and the resulting optimized conditions seen from the TmCphA1 experiment. During the addition of NaOH, a pH reader will be used so that the amount of NaOH added can be adjusted for reaching neutral pH. 
        
        ### Build & Test 3.2
        
        TmCphA1 plasmid colonies were plucked and grown in Terrific Broth (TB) for 48 hr each, with 1mM IPTG. Cell pellets were collected and stored in the -20 freezer for the purification step. See cyanophycin expression protocol for more details. 
        
        A cyanophycin purification protocol was adapted from [ ]. The protocol takes advantage of the fact that cyanophycin is insoluble at neutral pH, so we’re aiming to collect a pellet after HCl and NaOH have been added. The resulting in=soluble cyanophycin was lyophilized, weighed, and stored in the 4 C fridge for further experimentation. See the cyanophycin purification protocol for more details (SE6 fourth objective). 
        
        ### Learn 3.2
        
        Following the addition of NaOH, and therefore solution-neutralization, a pellet was able to be collected via centrifugation. Because we know that cyanophycin precipitates out of the solution at neutral pH, this collected fraction is considered the insoluble cyanophycin fraction. However, after the addition of ethanol, no pellet was seen—this would have been the soluble fraction of cyanophycin. The soluble fraction of cyanophycin is not needed for our experimental purposes, so on further troubleshooting needs to be done. 
        
    
- **4th cycle set - *in-vitro* CphA + cyanophycin test**
    
    ### Design 4.1
    
    To further characterize the activity of TmCphA1 and production of cyanophycin, an in-vitro test will be conducted with an SDS-PAGE gel to follow. Purified TmCphA1 and cyanophycin, from the previous experiments, will be used. This version of CphA requires a cyanophycin primer because it lacks the cryptic metallopeptidase active site that can produce cyanophycin without a primer. Again, a 100kDa band will signify TmCphA1 is active and expressing. Cyanophycin is expected to be represented as a smear around 25kDa on the gel, as cyanophycin is considered polydisperse. We’ll also be able to determine the amount of reagents that will synthesize the most amount of cyanophycin, if any. 
    
    A protocol was adapted from [] and the regeant details are listed here: 
    
    | Reagent | Stock concentration | Final concentration | Volume to add (uL) |
    | --- | --- | --- | --- |
    | Tris-HCl pH 8.0 | 1 M  | 100 mM  | 5 uL |
    | ATP | 100 mM  | 12.5 mM  | 6.25 uL |
    | MgCl2*** | 1 M | 2 mM  | 0.1 uL* |
    | L-aspartic acid | 200 mM  | 12.5 mM  | 3.1 uL*  |
    | L-arginine** | 1 M  | 12.5 mM  | 0.6 uL* |
    | KCl*** | 3 M | 12.5 mM  | 0.2 uL* |
    | Cyanophycin primer | 15 mg/mL  | 1.5 mg/mL | 5 uL |
    | TmCphA1 | 2505.78 | 100 ug/mL | 2 uL  |
    | Water | — | — | to 50uL  |
    
    Varying levels of TmCphA1 and cyanophycin will be supplemented, as detailed in [in-vitro protocol 1]. 
    
    ### Build 4.1
    
    A simple incubation reaction was performed to allow purified TmCphA1 to synthesize cyanophycin, using the supplemented cyanophycin primer to start the synthesis reaction. See details in the [in-vitro protocol 1]. 
    
    ### Test 4.1
    
    Following the in-vitro reaction, an SDS-PAGE gel was performed to test for the correct molecular weights of both CphA and cyanophycin. 
    
    ### Learn 4.1
    
    [waiting on experiment to be carried out (9/13/26)]
    
- **5th cycle set - Ammonium Biosensor**
    
    ### Design 5.1
    
    TmCphA1 is a large protein, one that will likely put our cell in extraneous metabolic burden when expressed, which could dramatically reduce supply for general cellular function and other elements of our project. Currently, TmCphA1 is regulated via the T7 expression system for a streamlined lab experiment. But to justify the potential for this product to be implemented along a well or subsurface drainage system, TmCphA1 needs to be regulated by something already occurring in its surrounding environment. 
    
    Nitrate will enter the cell, convert to nitrite, then ammonium, glutamine and glutamate, aspartate and arginine, and finally, cyanophycin. Of course, TmCphA1 uses aspartate and arginine to synthesize cyanophycin. But before this synthesis step, each of the intermediates along the described path are contributing to the arginine and aspartate supply. Therefore, one of them can be used as a trigger for the expression of TmCphA1. Cyanophycin’s purpose is to store the excess nitrogen from the incoming nitrate; we only want CphA to express when nitrate is present, otherwise it would be overexpressing unnecessarily. 
    
    [insert nitrate pathway schematic] 
    
    Zhang et al. (2017) developed an ammonium biosensor that is capable of regulating the expression of CphA via ammonium. The system takes advantage of two enzymes involved in the negative regulation of glutamine synthesis, GlnR and GlnA.  *Lactococcus natively uses* GlnA, a glutamine synthetase that converts ammonium and glutamate into glutamine, At high enough ammonium concentration. Once enough glutamine has accumulated, it binds GlnA and acts as a chaperone that stabilizes the repressor, GlnR. Now, the GlnRA complex is able to inhibit its own downstream genes via the glnR-sensitive promoter. 
    
    ![image.png](Project%20Engineering/image.png)
    
    *Figure 1: General schematic of the GlnRA system with YFP as the output. glnA and glnR are regulated by a synthetic promoter, Plib. YFP is regulated by a synthetic promoter, PglnR, that triggers gene expression in the presence of the GlnA:GlnR complex, in the presence of high enough ammonium.* 
    
    They developed a library of promoters that regulate GlnRA, YFP, RFP, and TetR expression. The biosensor was able to be transferred to other species effectively, namely E. coli. Once a few promoter candidates were filtered out from  their larger libraries, Nennenga et al. applied their established ammonium biosensor to control cyanophycin biosynthesis. To accomplish this, YFP was replaced by the TetR repressor and a second plasmid regulated CphA expression via a PTet promoter (repressed by TetR). Now, when enough ammonium is present, transcription of TetR is turned off, so CphA is free to be transcribed. 
    
    [Insert CphA biosensor system image] 
    
    Sequences for GlnR, GlnA, PglnR, and Plib are provided in the paper’s supporting information. A specific set of vectors were used to construct each of the plasmids. However, these vectors were not used because (1) The sequences could not be found in the paper nor anywhere online, (2) none of the authors responded to our request of these plasmid sequences, and (3) their goal of making this sensor for multiple species likely is a main reason for the use of multiple different vectors. Our goal is to apply this sensor to our system in E. coli, so our experiment only needs to only make use of the sequences mentioned before. 
    
    [insert benchling design] 
    
    As a preliminary test to ensure we can replicate the fundamental function of the biosensor, GFP will be the output. Varying levels of ammonium (and other nitrogen sources) will be supplemented, and fluorescence can be measured to determine the effectiveness of GlnR, GlnA, Plib, and PglnR. 
    
    Once this is validated, GFP will be replaced by TetR and a Ptet promoter will be placed upstream of our TmCphA1 CDS. The paper used an SDS-PAGE gel to quantify nad compare cyanophycin yield between conditions (e.g.  biosensor absent versus biosensor present). The ImageJ software was used to measure the opacity of each 25 kDa smear of cyanophycin. However, this method of quantification proves to be ineffective when attempting to compare conditions—it would only be sufficient if the test’s goal were to find if cyanophycin can be synthesized at all. 
    
    [Insert crappy SDS-PAGE image from paper??]
    
    After consulting with our mentor, Calin Plesa, we’ve been advized to use a more robust method. To more accurately quantify the biosensor’s effectiveness in regulating CphA, and therefore cyanophycin, RTQPCR
    

Questions David has (me) 

1. What can be considered a cycle? Do I need multiple iterations or just one? How do I organize this?
2. Should I combine some design & build or test & learn for some cycles? All of them to make it consistent? 
3. How much experiments setup should be included? Include sample charts? Direct stuff to protocols?
4. How detailed should the protocols be in DBTL? Leave most info for the protocols page?
5. The more sources included the better? Maximize the amount of times were mention we given advice on something (it’s mostly Calin)? 

• Module 3
