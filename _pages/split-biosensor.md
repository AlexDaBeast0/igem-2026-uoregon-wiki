---
layout: page
permalink: /split-biosensor

title: Split cyanophycin biosensor
subtitle: De novo protein binders for detecting cyanophycin
banner: https://static.igem.wiki/teams/6041/wiki/placeholders/petunias.avif
---

Upon accumulation of our storage polymer (cyanophycin), a trigger is needed to stimulate the expression of flocculation genes. Due to the orthogonality of cyanophycin in E. Coli, very few solutions existed for detecting its presence or concentration, leaving us very little to work with.

Taking inspiration from two existing cyanophycin-binding proteins, CphA and CphB (used in cyanophycin anabolism and catabolism, respectively){% cite miyakawaStructuralBasesAspartate2022a --file split-biosensor %}, we directed our focus to developing a split transcription factor based on the native binding motif of these two proteins. Specifically, that of CphB, as the literature suggested that removal of CphA’s G-domain (catalytic domain) would have consequences regarding its role in substrate binding {% cite kitadokoroCrystalStructurePathogenic2020 --file split-biosensor %}.

# Development of inactive CphB

Inactive forms of [CphB](https://www.wwpdb.org/pdb?id=pdb_00003en0), a serine protease responsible for the hydrolysis of cyanophycin, were developed through various point mutations of the catalytic serine (*SER 132*). Structures of mutated sequences, as well as native cyanophycinase, were predicted using RosettaFold-3 (RF3){% cite corleyAcceleratingBiomolecularModeling2025 --file split-biosensor %}; root-mean-squared deviation (RMSD) calculations between mutant and native structure binding sites were used to determine the degree of alteration to binding-site geometry. The S132A mutant produced the lowest binding-site RMSD (~0.063 Å) compared to other mutations (consistent with literature).

{% include figure.html
    url="https://static.igem.wiki/teams/6041/wiki/pages/split-cyanophycin-biosensor/split-cyanophycin-biosensor-rmsd-plddt-plot.avif"
    caption="Plots Containing RMSD comparisons of predicted mutant and native CphB for both total structure residue backbones (N, CA, C, O atoms) (left) and binding residue backbones (right). The S132A mutation shows the most similarity to the native structure in both plots."
    alttext="Plots containing RMSD comparisons of predicted mutant and native CphB for both total structure residue backbones (N, CA, C, O atoms) (left) and binding residue backbones (right). The S132A mutation shows the most similarity to the native structure in both plots."
    label="split-cyanophycin-biosensor-rmsd-plddt-plot"
%}
{% include figure.html 
    url="https://static.igem.wiki/teams/6041/wiki/pages/split-cyanophycin-biosensor/split-cyanophycin-biosensor-s132a-mut.avif"
    caption="Predicted structure of CphB S132A mutant"
    alttext="Predicted structure of CphB S132A mutant" 
    label="split-cyanophycin-biosensor_S132A-mut"
%}


# Development of De Novo Binders

Residues involved in the binding domain of the S132A mutant were selected to be fixed and designed around using RFdiffusion3 (RFD3){% cite butcherNovoDesignAllatom2025 --file split-biosensor %}, producing protein backbones containing only the S132A binding site. The binding sites of protein backbones created by RFD3 were scored for Solvent Accessible Surface Area (SASA). Scores for binding residue energies were also evaluated using the standard Rosetta energy function, ref2015, and the `fa_dun` term {% cite alfordRosettaAllatomEnergy2017 --file split-biosensor %}. Statistical probabilities and internal energies based on the Dunbrack rotamer library were calculated (DBR). SASA and DBR scores were used as criteria for filtering out poor backbones (SASA > 5 Å², DBR < 5 REU).

Sequences were designed for all non-fixed residues for all passing backbones using ProteinMPNN {% cite dauparasRobustDeepLearning2022 --file split-biosensor %}. Sequences were validated via structure prediction using RF3. SASA was calculated for the predicted structure, along with binding site RMSD between the backbone and the predicted structure, and predicted model confidence (pLDDT). Scores were used as filter criteria (SASA > 5 Å², RMSD < 0.5 Å, pLDDT > 0.85).

Inputs from designs passing all filters are then recycled through the pipeline to maximize predicted confidence. These final designs are then selected for in vitro testing and characterization.

{% include figure.html
    url="/uoregon/assets/svg_figures/split-biosensor/split-cyanophycin-biosensor_pipeline.svg"
    caption="Schematic of computational design pipeline used to create cyanophycin binders"
    alttext="Schematic of computational design pipeline used to create cyanophycin binders"
    label="split-cyanophycin-biosensor_pipeline"
%}

# Bibliography

{% bibliography --file split-biosensor --cited_in_order %}
