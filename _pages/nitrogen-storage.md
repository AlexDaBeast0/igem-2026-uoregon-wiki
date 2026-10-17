---
layout: page
permalink: /nitrogen-storage

title: Nitrogen Storage
subtitle: Storing the nitrogen that the bacteria capture.
banner: https://static.igem.wiki/teams/6041/wiki/page-banners/banner-electroporation.avif
---

# Cyanophycin

After identifying nitrate to be the main contributor to our problem, the first idea was to use bacteria capable of capturing this nitrate. However, following an extensive literature review, we found that this approach would not be very novel nor effective by itself. A common denominator with solutions dealing with nitrate runoff was that they would simply expel the nitrate into a benign form, such as nitrogen gas. Furthermore, existing nitrate-removal strategies can be costly, infrastructure-intensive, or focused on removal rather than nitrogen recovery.

This stemmed the idea to recycle the nitrogen from this incoming, excess nitrate. Nitrate is an intermediate rather than a stable intracellular storage form, so we sought to convert captured nitrogen into a more stable and recoverable product. For this to work, the nitrate needs to be stored in a stable enough form to be harvested and used as a fertilizer product. After searching and narrowing down various options, cyanophycin was deemed the best form of nitrogen storage. 

Cyanobacteria utilize a nitrogen-storage polymer, cyanophycin, to store excess nitrogen content for the long term. Cyanophycin is made up of a chain of 80-400 arginine and aspartate dipeptides. No enzyme or protease interacts with it, except cyanophycinase. Cyanophycinase is involved in the first step of cyanophycin catabolism, and is responsible for cleaving the polymer into its individual β-Asp-Arg dipeptides {% cite sharonStructuresFunctionAmino2021 --file engineering%} {% cite duEnhancedCyanophycinProduction2017 --file engineering%} {% cite swainHeterologousProductionCyanophycin2023 --file engineering%}. Cyanobacteria have utilized cyanophycin for storing nitrogen during periods of nitrogen fixation and nutrient stress, so it was perfect for storing the excess nitrogen from the incoming nitrate. Cyanophycin provided a way for our cells to maintain the excess nitrogen content and a create fertilizer alternative. 

Synthesis of cyanophycin is entirely dependent on the cyanophycin synthetase (CphA) enzyme, typically in an ATP-dependent manner. As a proof of concept, we aimed to find an appropriate CphA homolog, and ensure it can express and synthesize cyanophycin within our lab. A literature review was conducted to find a CphA homolog that is well characterized, produces high amounts of cyanophycin, and could be replicated. Swain et al.{% cite swainHeterologousProductionCyanophycin2023 --file nitrogen-storage %} demonstrated that TmCphA1 produced up to 2-fold greater insoluble cyanophycin yields than any other tested CphA1. It also had 10.8 times greater yields than the widely studied CphA1 from synechocystis sp. PCC6308 {% cite AboulmagdPurificationSynechocystisspStrainPCC63082001 --file nitrogen-storage %} {% cite ZieglerMolecularcharacterization1998 --file nitrogen-storage %}

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/nitrogen-storage/nitrogen-storage-tmcpha1-structure.avif"
caption="Structure of TmCphA1 with domains labeled. Sharon et al, 2021"
alttext="Structure of TmCphA1 with domains labeled. Sharon et al, 2021"
label="TmCphA1 protein structure"
%}

TmCphA1 is a 400 kDa tetramer with three functional domains that contribute to the production of cyanophycin. The G-domain extends the aspartic acid backbone, via an ATP-dependent catalytic reaction. The M-domain adds an arginine group to the sidechain of the aspartic acid backbone chain. Finally, the N-domain utilizes hydrogen bonding and salt bridges to hold the polymer in place—subunits of the growing polymer can be alternately attached by flipping between the G and M-domains more effectively this way.

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/nitrogen-storage/nitrogen-storgae-cyphy-synthesis.avif"
caption="**a**. Aspartate backbone (in yellow) is linked to two arginine residues on each of its side chains, through an isopeptide bond. **b.** To begin the reaction catalyzed by CphA1, the terminal carboxylate of the aspartate backbone is phosophorylated and extended by one aspartate group**.** After phosphorylation of this new aspartate residue, an arginine residue is attached to its side chain."
alttext="**a**. Aspartate backbone (in yellow) is linked to two arginine residues (in green) on each of its side chains, through an isopeptide bond. **b.** To begin the reaction catalyzed by CphA1, the terminal carboxylate of the aspartate backbone is phosophorylated and extended by one aspartate group**.** After phosphorylation of this new aspartate residue, an arginine residue is attached to its side chain. Sharon et al, 2021"
label="Cyanophycin synthesis."
%}

See the Engineering page for the design, build, test, and learn (DBTL) cycles involved in proving nitrate can be stored effectively.

# Ammonium biosensor

TmCphA1 is a large protein, one that will likely put our cell in extraneous metabolic burden when expressed, which could dramatically reduce supply for general cellular function and other elements of our project’s design. Currently, TmCphA1 is regulated via the T7 expression system for streamlined lab experiments. But to justify that this product has potential to be implemented along a well or subsurface drainage system, TmCphA1 needs to be regulated by something already present in its surrounding environment.

Nitrate will enter the cell, convert to nitrite, then ammonium, glutamine and glutamate, aspartate and arginine, and finally, cyanophycin. Of course, nitrogen metabolism converts nitrate, and said reduced versions, into forms that don’t funnel all their their nitrogen content into cyanophycin. However, this pathway is the only way for cyanophycin to utilize the incoming nitrate. TmCphA1 uses aspartate and arginine to synthesize cyanophycin. But before this synthesis step, each of the intermediates along the described path are contributing to an arginine and aspartate supply. Therefore, one of them can be used as a trigger for the expression of TmCphA1. Cyanophycin's purpose is to store the excess nitrogen from the incoming nitrate; we only want CphA to express when nitrate is present, otherwise it would be overexpressing unnecessarily. 

We were able to find a biosensor that is sensitive to ammonium. As ammonium levels rise, the circuit downregulates the expression of a gene. Ammonium is a big indicator of how much cyanophycin we would be able to produce, so we continued in development. See the engineering page for the design, build, test, and learn (DBTL) cycle involved in validating the efficacy of the ammonium biosensor. 

Xiao et al, 2017 {% cite xiaoDevelopingGeneticallyEncoded2017 --file nitrogen-storage %} developed an ammonium biosensor that is capable of regulating the expression of CphA via ammonium. The system takes advantage of two enzymes involved in the negative regulation of glutamine synthesis, GlnR and GlnA. *Lactococcus* natively uses GlnA, a glutamine synthetase that converts ammonium and glutamate into glutamine, At high enough ammonium concentration. Once enough glutamine has accumulated, it binds GlnA and acts as a chaperone that stabilizes the repressor, GlnR. Now, the GlnR-A complex is able to inhibit its own downstream genes via the glnR-sensitive promoter.

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineering-glnra-schematic.avif"
caption="Figure 1: General schematic of the GlnRA system with YFP as the output. glnA and glnR are regulated by a synthetic promoter, Plib. YFP is regulated by a synthetic promoter, PglnR, that triggers gene expression in the presence of the GlnA:GlnR complex, in the presence of high enough ammonium."
alttext="Figure 1: General schematic of the GlnRA system with YFP as the output. glnA and glnR are regulated by a synthetic promoter, Plib. YFP is regulated by a synthetic promoter, PglnR, that triggers gene expression in the presence of the GlnA:GlnR complex, in the presence of high enough ammonium."
label="GlnRA system"
%}

They developed a library of promoters that regulate GlnR-A, YFP, RFP, and TetR expression. The biosensor was able to be transferred to other species effectively, namely E. coli. Once a few promoter candidates were filtered out from their larger libraries, Xiao et al. {% cite xiaoDevelopingGeneticallyEncoded2017 --file nitrogen-storage %}. applied their established ammonium biosensor to control cyanophycin biosynthesis. To accomplish this, YFP was replaced by the TetR repressor and a second plasmid regulated CphA expression via a PTet promoter (repressed by TetR). Now, when enough ammonium is present, transcription of TetR is turned off, so CphA is free to be transcribed.

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineering-nh4-sensor-cpha.avif"
caption="Schematic of the ammonium biosensor regulating CphA expression via the TetR sensitive promoter, pTet (Zhang et al.)"
alttext="Schematic of the ammonium biosensor regulating CphA expression via the TetR sensitive promoter, pTet (Zhang et al.)"
label="GlnRA system regulating CphA"
%}

Sequences for GlnR, GlnA, PglnR, and Plib are provided in the paper's supporting information. A specific set of vectors were used to construct each of the plasmids. However, these vectors were not used because (1) the sequences could not be found in the paper nor anywhere online, (2) none of the authors responded to our request of these plasmid sequences, and (3) their goal of making this sensor for multiple species likely is a main reason for the use of multiple different vectors. Our goal is to apply this sensor to our system in E. coli, so our experiment only needs to only make use of the sequences mentioned before.

## Fluorescent Readout

As a preliminary test to ensure we can replicate the fundamental function of the biosensor, GFP will be the output. Varying levels of ammonium (and other nitrogen sources) will be supplemented, and fluorescence can be measured to determine the effectiveness of GlnR, GlnA, Plib, and PglnR. Once this is validated, GFP will be replaced by TetR, and a Ptet promoter will be placed upstream of our TmCphA1 CDS. 

A pTwist Kan Medium copy vector was used as the backbone when designing this version of the biosensor. GlnR and glnA were placed sequentially, under the constitutive plib promoter, designed by Xiao et al, 2017{% cite xiaoDevelopingGeneticallyEncoded2017 --file nitrogen-storage %}. Salis labs was used to design two optimized RBS sequences for glnR and glnA. GFP expression was designed to be run in the antisense direction, so in the opposite direction of the glnR and glnA module. PglnR2 is the ammonium-sensitive promoter, which was placed upstream of GFP and the Salis lab-optimized RBS. The BBa_B0012 Terminator was placed at the end of GlnR, GlnA, and GFP

{% include figure.html
url="/uoregon/assets/svg_figures/nitrogen-storage/nitrogen-storage_GlnRA-GFP_insert-in-pTwist-Kan-Medium-Copy.svg"
caption="Benchilng plasmid design for the ammonium biosensor with a GFP output."
alttext="Benchilng plasmid design for the ammonium biosensor with a GFP output."
label="Ammonium-sensor-plasmid-GFP-output"
%}

## RT-qPCR

The paper used an SDS-PAGE gel to quantify and compare cyanophycin yield between conditions (e.g.  biosensor absent versus biosensor present). The ImageJ software was used to measure the opacity of each 25 kDa smear of cyanophycin. However, this method of quantification proves to be ineffective when attempting to compare conditions—it would only be sufficient if the test's goal were to find if cyanophycin can be synthesized at all.

After consulting with our mentor, Calin Plesa, we have been advised to use a more robust method. To more accurately quantify the biosensor's effectiveness in regulating TmCphA1 expression, and therefore cyanophycin synthesis, RT-qPCR can be implemented. RT-qPCR will be used to quantify the amount of TmCphA1 that has been transcribed. A reverse transcriptase is first used to reverse transcribe the RNA of TmCPhA1, converting it to DNA. This DNA can be amplified with designed primers and measurement via a dye or probe based-approach {% cite BongBriefguideRTqPCR --file nitrogen-storage %} {% cite AdamsBeginnerguidetoRTqPCR --file nitrogen-storage %}. Although this will not directly give us a way of determining how much cyanophycin yield can result, TmCphA1 transcription is a beneficial first way of figuring out how efficient and sensitive the biosensor is at producing TmCphA1.

A similar design structure was used for constructing the plasmid meant for TetR expression. Again, this would allow for de-repression of the pTet promoter that regulates TmCphA1 expression. Therefore, as ammonium levels increase, TetR expression will decrease, and TmCphA1 expression can increase.

{% include figure.html
url="/uoregon/assets/svg_figures/nitrogen-storage/nitrogen-storage_GlnRA-TetR_insert-in-pTwist-Kan-Medium-Copy.svg"
caption="Benchilng plasmid design for the ammonium biosensor with a TetR output."
alttext="Benchilng plasmid design for the ammonium biosensor with a TetR output."
label="Ammonium-sensor-plasmid-TetR-output"
%}

# Bibliography

{% bibliography --file nitrogen-storage --cited_in_order %}
