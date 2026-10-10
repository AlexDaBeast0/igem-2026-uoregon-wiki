---
layout: page
permalink: /nitrogen-storage

title: Nitrogen Storage
subtitle: This is the nitrogen storage module page.
banner: https://static.igem.wiki/teams/6041/wiki/placeholders/petunias.avif
---

# REMOVE CONTRACTIONS

After identifying nitrate to be the main contributor to our problem, the first idea was to use bacteria capable of capturing this nitrate. However, following an extensive literature review, we found that this approach would not be very novel nor effective by itself. A common denominator with solutions dealing with nitrate runoff was that they would simply expel the nitrate into a benign form, such as nitrogen gas. Furthermore, possible solutions such as riparian buffers, anion exchange systems, distillation, and reverse osmosis systems are expensive, ineffective, time and labor intensive, and do not last long.

This stemmed the idea to recycle the nitrogen from this incoming, excess nitrate. Nitrate wont be able to stably reside in the cell long enough to recycle the nitrogen content. For this to work, the nitrate needs to be stored in a stable enough form to be harvested and used as a fertilizer product. After searching and narrowing down various options, cyanophycin was deemed the best form of nitrogen storage. Cyanophycin is a granule polypeptide consisting of 80-400 linked arginine and aspartate dipeptides {% cite sharonStructuresFunctionAmino2021 --file nitrogen-storage %}. Cyanobacteria have utilized cyanophycin for storing nitrogen during periods of nitrogen fixation and nutrient stress, so it was perfect for storing the excess nitrogen from the incoming nitrate.

Synthesis of cyanophycin is entirely dependent on the cyanophycin synthetase (CphA) enzyme, typically in an ATP-dependent manner. As a proof of concept, we aimed to find an appropriate CphA homolog, and ensure it can express and synthesize cyanophycin within our lab. A literature review was conducted to find a CphA homolog that is well characterized, produces high amounts of cyanophycin, and could be replicated. Swain et al.{% cite swainHeterologousProductionCyanophycin2023 --file nitrogen-storage %} demonstrated that TmCphA1 produced up to 2-fold greater insoluble cyanpphycin yields than any other tested CphA1. It also had 10.8 times greater yields than the widely studied CphA1 from synechocystis sp. PCC6308.

[insert image of CphA structure]

TmCphA1 is a 400 kDa tetramer with three functional domains that contribute to the production of cyanophycin. The G-domain extends the aspartic acid backbone, via an ATP-dependent catalytic reaction. The M-domain adds an arginine group to the sidechain of the aspartic acid backbone chain. Finally, the N-domain utilizes hydrogen bonding and salt bridges to hold the polymer in place—subunits of the growing polymer can be alternately attached by flipping between the G and M-domains more effectively this way.

[image on cyanophycin synthesis]

Cyanophycin's terminal carboxylate in its growing chain is first phosophorylated, and one aspartic acid residue is added.

See the engineering page for the design, build, test, and learn (DBTL) cycles involved in proving nitrate can be stored effectively.

# Ammonium biosensor

TmCphA1 is a large protein, one that will likely put our cell in extraneous metabolic burden when expressed, which could dramatically reduce supply for general cellular function and other elements of our project. Currently, TmCphA1 is regulated via the T7 expression system for streamlined lab experiments. But to justify that this product has potential to be implemented along a well or subsurface drainage system, TmCphA1 needs to be regulated by something already present in its surrounding environment.

Nitrate will enter the cell, convert to nitrite, then ammonium, glutamine and glutamate, aspartate and arginine, and finally, cyanophycin. Of course, TmCphA1 uses aspartate and arginine to synthesize cyanophycin. But before this synthesis step, each intermediate along the described path are contributing to the arginine and aspartate supply. Therefore, one of them can be used as a trigger for the expression of TmCphA1. Cyanophycin's purpose is to store the excess nitrogen from the incoming nitrate; we only want CphA to express when nitrate is present, otherwise it would be overexpressing unnecessarily.

**[insert nitrate pathway schematic]**

Xiao et al, 2017 {% cite xiaoDevelopingGeneticallyEncoded2017 --file nitrogen-storage %} developed an ammonium biosensor that is capable of regulating the expression of CphA via ammonium. The system takes advantage of two enzymes involved in the negative regulation of glutamine synthesis, GlnR and GlnA.  *Lactococcus* natively uses GlnA, a glutamine synthetase that converts ammonium and glutamate into glutamine, At high enough ammonium concentration. Once enough glutamine has accumulated, it binds GlnA and acts as a chaperone that stabilizes the repressor, GlnR. Now, the GlnR-A complex is able to inhibit its own downstream genes via the glnR-sensitive promoter.

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineering-glnra-schematic.avif"
caption="Figure 1: General schematic of the GlnRA system with YFP as the output. glnA and glnR are regulated by a synthetic promoter, Plib. YFP is regulated by a synthetic promoter, PglnR, that triggers gene expression in the presence of the GlnA:GlnR complex, in the presence of high enough ammonium."
alttext="Figure 1: General schematic of the GlnRA system with YFP as the output. glnA and glnR are regulated by a synthetic promoter, Plib. YFP is regulated by a synthetic promoter, PglnR, that triggers gene expression in the presence of the GlnA:GlnR complex, in the presence of high enough ammonium."
label="GlnRA_schematic"
%}

They developed a library of promoters that regulate GlnR-A, YFP, RFP, and TetR expression. The biosensor was able to be transferred to other species effectively, namely E. coli. Once a few promoter candidates were filtered out from their larger libraries, Xiao et al. {% cite xiaoDevelopingGeneticallyEncoded2017 --file nitrogen-storage %} applied their established ammonium biosensor to control cyanophycin biosynthesis. To accomplish this, YFP was replaced by the TetR repressor and a second plasmid regulated CphA expression via a PTet promoter (repressed by TetR). Now, when enough ammonium is present, transcription of TetR is turned off, so CphA is free to be transcribed.

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/pages/enginnering/engineering-nh4-sensor-cpha.avif"
caption="Schematic of the ammonium biosensor regulating CphA expression via the TetR sensitive promoter, pTet (Zhang et al.)"
alttext="Second iteration of the CphA in-vitro test. All samples except 'no CphA' showed bands at 100 kilodaltons, as expected. No smear around 25 kilodaltons was seen for any sample, signifying that cyanophycin could not be seen."
label="CphA in-vitro test 2"
%}

Sequences for GlnR, GlnA, PglnR, and Plib are provided in the paper's supporting information. A specific set of vectors were used to construct each of the plasmids. However, these vectors were not used because (1) the sequences could not be found in the paper nor anywhere online, (2) none of the authors responded to our request of these plasmid sequences, and (3) their goal of making this sensor for multiple species likely is a main reason for the use of multiple different vectors. Our goal is to apply this sensor to our system in E. coli, so our experiment only needs to only make use of the sequences mentioned before.



As a preliminary test to ensure we can replicate the fundamental function of the biosensor, GFP will be the output. Varying levels of ammonium (and other nitrogen sources) will be supplemented, and fluorescence can be measured to determine the effectiveness of GlnR, GlnA, Plib, and PglnR. Once this is validated, GFP will be replaced by TetR, and a Ptet promoter will be placed upstream of our TmCphA1 CDS.

The paper used an SDS-PAGE gel to quantify and compare cyanophycin yield between conditions (e.g.  biosensor absent versus biosensor present). The ImageJ software was used to measure the opacity of each 25 kDa smear of cyanophycin. However, this method of quantification proves to be ineffective when attempting to compare conditions—it would only be sufficient if the test's goal were to find if cyanophycin can be synthesized at all.

[Insert crappy SDS-PAGE image from paper??]

After consulting with our mentor, Calin Plesa, we've been advised to use a more robust method. To more accurately quantify the biosensor's effectiveness in regulating CphA, and therefore cyanophycin, RT-qPCR can be implemented. RT-qPCR will be used to quantify the amount of TmCphA1 that has been transcribed. Although this won't directly give us a way of determining how much cyanophycin yield can result from this, CphA transcription is a good first way of figuring out how efficient and sensitive the biosensor is at producing CphA.

Our first objective is to measure GFP output as a result of varying ammonium levels. The practical setup in the end has a well-plate filled with cell samples and ammonium media, so a plate reader can detect GFP and OD levels as expression occurs. To make a stock of our cells, we need to grow up our cells (with the biosensor plasmid) in an LB media starter culture. This starter culture is then diluted into an M9 minimal media with supplemented ammonium. This is so our cells have an equal amount of repressed GFP going into the plate reader recording. A nitrogen source is also needed to grow at all. After growing, the cells are washed free of the ammonium and resuspended in nitrogen-free M9. Now, the cells have been set to a "baseline" level of GFP expression and are ready for the plate-reader; the ammonium supplementation will be the only thing that can control GFP expression here on out. An stock of ammonium and nitrogen-free M9 is then made to be added to the wells of the plate reader.

For the main samples, each well of the plate reader will include ammonium stock and cell stock at a 1:1 ratio.



{% bibliography --file nitrogen-storage --cited_in_order %}
