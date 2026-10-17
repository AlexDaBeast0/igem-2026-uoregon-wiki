---
layout: page
permalink: /flocculation

title: Flocculation
subtitle: Collecting our bacteria for reuse.
banner: https://static.igem.wiki/teams/6041/wiki/page-banners/banner-gel.avif
---
Once nitrogen pollutants are stored intracellularly as biological polymer cyanophycin, the biomass must be collected from the system. To this end, our team reviewed the literature for a biological strategy which would allow for selective harvest of cyanophycin-rich cells. Existing methods for water filtration include anion exchange, carbon, ultrafiltration, and electrochemical filters, which suffer from inefficiency and maintenance difficulties{% cite guthModernWaterTreatment2025 --file flocculation %}.

To resolve this issue, the ability of *E. coli* to flocculate was identified as a promising strategy for removing engineered bacteria from water sources. “Flocs” are proteinaceous aggregates of bacteria associated with production of outer membrane vesicles, as investigated by Ojima et. al, 2016 {% cite ojimaFlocculationEscherichiaColi2015a --file flocculation %}. Flocculations can reach several millimeters in size, and are visible as thin, scrap-like formations. The study by Ojima et. al found that the flocculation and enhanced OMV production phenotype correlated with overexpression of the native gene bcsB component of the bacterial cellulose synthase complex. Though the specific relationship between BcsB overexpression and flocculation phenotype is yet unclear, this was used as a starting point for collection of the engineered host strain {% cite ojimaFlocculationEscherichiaColi2015a --file flocculation %}. Currently, this work aims to demonstrate inducible aggregation of engineered cells, with the long-term goal of selective harvesting of cyanophycin-rich biomass by porous filtration.

## Design Cycle 1

First, inducible flocculation of the host strain was demonstrated. To this end, the bcsB gene sequence (Uniprot P37652) was placed into vector pET-28(+) (Twist Bioscience) to produce test plasmid pET-28(+)-bcsB, which includes an N-terminal histidine tag for IMAC protein production. The test plasmid was cloned into host strain E. coli BL21(DE3). Separately, BL21(DE3) was transformed with pJUMP29-1A to produce a control strain for use in overexpression and flocculation experiments. Strains were cultured with 1 mM IPTG for 24 hr. SDS-PAGE was used to qualitatively measure BcsB expression. Methods and materials can be found in Protocols.

After demonstrating overexpression in the host strain, the histidine tag was removed from bcsB to minimize the possibility of interfering with protein function. The gene sequence was supplemented with an iGEM ribosome binding site (RBS) BBa_J426032 and the translation rate was predicted (Salis Lab RBS calculator) at 59,140. The sequence was inserted into pET-21a(+) (Twist Bioscience) to produce pET-21a(+)-bcsB and cloned into *E. coli* BL21 (DE3). Recombinant strain and control BL21(DE3) strains were cultured with 1mM IPTG. After 24 hr, solutions were removed and left to stand for 15 minutes at room temperature. Precipitates were resuspended in 0.9% NaCl solution and flocculations were imaged via light microscopy as described {% cite ojimaFlocculationEscherichiaColi2015a --file flocculation %}.

{% include figure.html
url="https://static.igem.wiki/teams/6041/wiki/flocculation/flocculation-salisbcsb.avif"
caption="Salis lab RBS calculator prediction for bcsB translation rates under BBa_J426032. Relative translation rate is predicted as 59,140 at the start codon, nucleotide position 30. "
alttext="Salis lab RBS calculator prediction for bcsB translation rates under BBa_J426032. Relative translation rate is predicted as 59,140 at the start codon, nucleotide position 30."
label="RBS Translation Rate Prediction"
%}


## Design Cycle 2

Flocculation has been shown to be inducible under ideal conditions, with a provided carbon source at 37 C. However, wastewater and agricultural runoff is typically around 10 C, poor in carbon and oxygen. Though E. coli may survive and grow under these conditions, metabolism switches to favor a more conservative anaerobic regime and slower growth {% cite vanheeswijkNitrogenAssimilationEscherichia2013a --file flocculation %}, posing an issue to real-world translation of our system. As such, our team performed directed evolution to obtain a Bl21(DE3) strain that could host our system in the target environment. Directed evolution resulted in a strain that successfully cultured at 33 C. The flocculation experiment above was repeated in this strain.

## Results and Future Directions

Here, overexpression of BcsB is shown to induce a flocculation phenotype in the host strain. It is our hope that future iGEM teams will benefit from the genetic machinery for a flocculation phenotype and inducible aggregation of E. coli.  Future research aims to design a mechanism by which flocculation is dependent on the presence of cyanophycin for selective harvesting of the engineered strain. However, there are no native pathways by which cyanophycin can regulate BcsB expression. As selective transcription is of great interest, split transcription factor systems have previously been explored that utilize novel binding domains for factor recruitment and activation dependent on the presence of metabolites or environmental triggers. To induce BcsB expression dependent on the presence of cyanophycin via a split transcription factor mechanism, binding domains of cyanophycin would be highly useful. As such, a suite of protein fragment scaffolds were designed *de novo* against cyanophycin to generate binding domains. This was done computationally, and methods and results of the project can be found here. Binding affinity and specificity of these domains for cyanophycin will be evaluated in wet lab next, followed by incorporation of the split transcription factor system to BcsB expression.

# Bibliography

{% bibliography --file flocculation --cited_in_order %}
