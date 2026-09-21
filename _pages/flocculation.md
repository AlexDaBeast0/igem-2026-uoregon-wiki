---
layout: page
permalink: /flocculation

title: Flocculation
subtitle: This is the flocculation module page.
banner: https://static.igem.wiki/teams/6041/wiki/placeholders/petunias.avif
---

# Background

To collect stored nitrogen, we needed a method that would both be responsive to accumulated cyanophycin and practical to implement. To this end, our team reviewed the literature for a biological strategy which would allow for rapid harvest of cyanophycin-rich bacteria. We identified the ability of *E. coli* to flocculate as a promising strategy. “Flocs” are proteinaceous aggregates of bacteria associated with production of outer membrane vesicles, as investigated by Ojima et. al, 2016 {% cite ojimaFlocculationEscherichiaColi2015a --file flocculation %}. Flocculations are observed to be several millimeters in size, and are visible as thin, scrap-like formations. As such, they are large enough to be filtered from solution using mechanical methods, rather than the intensive and constantly chemical extractions which may be employed on free nitrates in wastewater, such as anion exchange filters, or harvesting individual cyanophycin-rich cells using micron-scale pores. Instead, we envisioned the ability to easily separate large cellular aggregates from our target water source.

The study by Ojima et. al found that the native E. coli gene bcsB is primarily responsible for flocculation, as the phenomenon can be replicated in culture simply by inducing the recombinant gene’s overexpression in multiple common laboratory E. coli strains, including B strains. To employ flocculation in our system, we needed to not only ensure the overexpression of bcsB, but set it to do so only at the point when our engineered strains had captured and stored a sufficient amount of nitrate.

# Design Cycle 1

To test expression of the bcsB monomeric protein, we placed the gene (Uniprot P37652) under control of a T7 promoter system and cloned into the well-characterized pET-21(+) vector with a supplemented RBS using Golden Gate assembly, as well as an N-terminal his-tag for downstream purification.

[plasmid picture/RBS prediction]


{% include figure.html
    url="URL,_IN_QUOTES"
    caption="CAPTION_GOES_HERE"
    alttext="DESCRIPTION_FOR_PEOPLE_WHO_USE_SCREEN_READERS"
    label="LABEL"
%}


BL21(DE3) cells were then transformed with the cloned plasmid and cultured. Cells were lysed and IMAC was used to purify the his-tagged protein. SDS PAGE verified the presence of bcsB, with a band at approximately 86 kDa.

[picture of gel].


{% include figure.html
    url="URL,_IN_QUOTES"
    caption="CAPTION_GOES_HERE"
    alttext="DESCRIPTION_FOR_PEOPLE_WHO_USE_SCREEN_READERS"
    label="LABEL"
%}


To test flocculation, the bcsB gene block was ordered without the N-terminal his tag, as flocculation relies on formation of a hexameric complex. The gene block was again cloned into the pET-21(+) plasmid, then transformed BL21(DE3). Cells were cultured for 24 hours at 37 C to produce flocculations as previously described by Ojima et. al.. Flocculations were imaged via light microscopy.

[insert flocculation data/images]


{% include figure.html
    url="URL,_IN_QUOTES"
    caption="CAPTION_GOES_HERE"
    alttext="DESCRIPTION_FOR_PEOPLE_WHO_USE_SCREEN_READERS"
    label="LABEL"
%}


Although flocculation has been shown to be inducible under ideal conditions, with a provided carbon source at 37 C. However, wastewater and agricultural runoff is typically around 4 C, poor in carbon and oxygen. Though E. coli may survive and grow under these conditions, metabolism switches to favor a more conservative anaerobic regime and slower growth. As such, our team performed directed evolution to obtain a strain that could efficiently assimilate nitrogen, reproduce, and form flocs in the target environment. *directed evolution when those results come in. Ideally there will be pictures of plates.

# Design Cycle 2

[add revisions when ready–hopefully with a directed evolution e coli strain]

# Conclusions

The bcsB gene can be cloned and successfully produce flocculations in the target bacterial strain. However, as a last major design consideration, we had to consider how flocculation by overexpression of the bcsB gene could be responsive to cyanophycin, so that cells could be harvested only after accumulating nitrogen. There are no known binders of cyanophycin which could be utilized as a transcription factor upstream of the recombinant bcsB. As such, our team elected to computationally design a suite of split transcription factors. These were designed to bind to lysine and arginine side chains in close proximity, as present in the cyanophycin polymer. Upon binding, the transcription factor is activated and triggers bcsB transcription. More information can be found on the computational page.

Should future teams seek to employ flocculation in their own systems, the bcsB part engineered and leveraged by our team can be found here [link to part database].

# Bibliography

{% bibliography --file flocculation --cited_in_order %}


